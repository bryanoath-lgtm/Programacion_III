from graphviz import Digraph
import csv
import math


class Nodo:
    def __init__(self, grado, hoja=False):
        self.grado = grado
        self.hoja = hoja
        self.claves = []
        self.hijos = []


class ArbolB:
    def __init__(self, grado):
        self.grado = grado
        self.max_claves = grado - 1
        self.min_claves = math.ceil(grado / 2) - 1
        self.raiz = Nodo(grado, hoja=True)

    def buscar(self, k, nodo=None):
        if nodo is None:
            nodo = self.raiz

        i = 0

        while i < len(nodo.claves) and k > nodo.claves[i]:
            i += 1

        if i < len(nodo.claves) and k == nodo.claves[i]:
            return True

        if nodo.hoja:
            return False

        return self.buscar(k, nodo.hijos[i])

    def insertar(self, k):
        resultado = self._insertar_recursivo(self.raiz, k)

        if resultado is not None:
            clave_media, nuevo_derecho = resultado

            nueva_raiz = Nodo(self.grado, hoja=False)
            nueva_raiz.claves = [clave_media]
            nueva_raiz.hijos = [self.raiz, nuevo_derecho]

            self.raiz = nueva_raiz

    def _insertar_recursivo(self, nodo, k):
        if nodo.hoja:
            self._insertar_ordenado(nodo.claves, k)

            if len(nodo.claves) > self.max_claves:
                return self._dividir_nodo(nodo)

            return None

        i = 0

        while i < len(nodo.claves) and k > nodo.claves[i]:
            i += 1

        resultado = self._insertar_recursivo(nodo.hijos[i], k)

        if resultado is not None:
            clave_media, nuevo_derecho = resultado

            nodo.claves.insert(i, clave_media)
            nodo.hijos.insert(i + 1, nuevo_derecho)

            if len(nodo.claves) > self.max_claves:
                return self._dividir_nodo(nodo)

        return None

    def _insertar_ordenado(self, lista, k):
        i = len(lista) - 1
        lista.append(None)

        while i >= 0 and k < lista[i]:
            lista[i + 1] = lista[i]
            i -= 1

        lista[i + 1] = k

    def _dividir_nodo(self, nodo):
        medio = len(nodo.claves) // 2
        clave_media = nodo.claves[medio]

        nuevo_derecho = Nodo(self.grado, hoja=nodo.hoja)

        nuevo_derecho.claves = nodo.claves[medio + 1:]
        nodo.claves = nodo.claves[:medio]

        if not nodo.hoja:
            nuevo_derecho.hijos = nodo.hijos[medio + 1:]
            nodo.hijos = nodo.hijos[:medio + 1]

        return clave_media, nuevo_derecho

    def eliminar(self, k):
        if not self.buscar(k):
            return False

        claves = self.recorrer()
        claves.remove(k)

        self.raiz = Nodo(self.grado, hoja=True)

        for clave in claves:
            self.insertar(clave)

        return True

    def _eliminar_recursivo(self, nodo, k):
        i = 0

        while i < len(nodo.claves) and k > nodo.claves[i]:
            i += 1

        if i < len(nodo.claves) and nodo.claves[i] == k:
            if nodo.hoja:
                nodo.claves.pop(i)
                return True

            return self._eliminar_de_nodo_interno(nodo, i)

        if nodo.hoja:
            return False

        eliminado = self._eliminar_recursivo(nodo.hijos[i], k)

        if eliminado and nodo.hijos[i] != self.raiz and len(nodo.hijos[i].claves) < self.min_claves:
            self._arreglar_hijo(nodo, i)

        return eliminado

    def _eliminar_de_nodo_interno(self, nodo, indice):
        clave = nodo.claves[indice]
        hijo_izquierdo = nodo.hijos[indice]
        hijo_derecho = nodo.hijos[indice + 1]

        if len(hijo_izquierdo.claves) > self.min_claves:
            predecesor = self._obtener_predecesor(hijo_izquierdo)
            nodo.claves[indice] = predecesor
            self._eliminar_recursivo(hijo_izquierdo, predecesor)

            if len(hijo_izquierdo.claves) < self.min_claves:
                self._arreglar_hijo(nodo, indice)

            return True

        elif len(hijo_derecho.claves) > self.min_claves:
            sucesor = self._obtener_sucesor(hijo_derecho)
            nodo.claves[indice] = sucesor
            self._eliminar_recursivo(hijo_derecho, sucesor)

            if len(hijo_derecho.claves) < self.min_claves:
                self._arreglar_hijo(nodo, indice + 1)

            return True

        else:
            # Se elimina la clave interna fusionando sus dos hijos sin conservar la clave eliminada.
            hijo_izquierdo.claves.extend(hijo_derecho.claves)

            if not hijo_izquierdo.hoja:
                hijo_izquierdo.hijos.extend(hijo_derecho.hijos)

            nodo.claves.pop(indice)
            nodo.hijos.pop(indice + 1)

            return True

    def _obtener_predecesor(self, nodo):
        actual = nodo

        while not actual.hoja:
            actual = actual.hijos[-1]

        return actual.claves[-1]

    def _obtener_sucesor(self, nodo):
        actual = nodo

        while not actual.hoja:
            actual = actual.hijos[0]

        return actual.claves[0]

    def _arreglar_hijo(self, padre, indice):
        hijo = padre.hijos[indice]

        if indice > 0 and len(padre.hijos[indice - 1].claves) > self.min_claves:
            self._prestar_de_izquierdo(padre, indice)

        elif indice < len(padre.hijos) - 1 and len(padre.hijos[indice + 1].claves) > self.min_claves:
            self._prestar_de_derecho(padre, indice)

        else:
            if indice > 0:
                self._fusionar_con_izquierdo(padre, indice)
            else:
                self._fusionar_con_derecho(padre, indice)

    def _prestar_de_izquierdo(self, padre, indice):
        hijo = padre.hijos[indice]
        hermano = padre.hijos[indice - 1]

        hijo.claves.insert(0, padre.claves[indice - 1])
        padre.claves[indice - 1] = hermano.claves.pop()

        if not hermano.hoja:
            hijo.hijos.insert(0, hermano.hijos.pop())

    def _prestar_de_derecho(self, padre, indice):
        hijo = padre.hijos[indice]
        hermano = padre.hijos[indice + 1]

        hijo.claves.append(padre.claves[indice])
        padre.claves[indice] = hermano.claves.pop(0)

        if not hermano.hoja:
            hijo.hijos.append(hermano.hijos.pop(0))

    def _fusionar_con_izquierdo(self, padre, indice):
        hijo = padre.hijos[indice]
        hermano = padre.hijos[indice - 1]

        hermano.claves.append(padre.claves.pop(indice - 1))
        hermano.claves.extend(hijo.claves)

        if not hijo.hoja:
            hermano.hijos.extend(hijo.hijos)

        padre.hijos.pop(indice)

    def _fusionar_con_derecho(self, padre, indice):
        hijo = padre.hijos[indice]
        hermano = padre.hijos[indice + 1]

        hijo.claves.append(padre.claves.pop(indice))
        hijo.claves.extend(hermano.claves)

        if not hermano.hoja:
            hijo.hijos.extend(hermano.hijos)

        padre.hijos.pop(indice + 1)

    def recorrer(self, nodo=None):
        if nodo is None:
            nodo = self.raiz

        resultado = []

        for i in range(len(nodo.claves)):
            if not nodo.hoja:
                resultado.extend(self.recorrer(nodo.hijos[i]))

            resultado.append(nodo.claves[i])

        if not nodo.hoja:
            resultado.extend(self.recorrer(nodo.hijos[len(nodo.claves)]))

        return resultado

    def cargar_csv(self, archivo):
        cargadas = 0
        duplicadas = 0
        invalidas = 0

        with open(archivo, newline='', encoding='utf-8') as file:
            lector = csv.reader(file)

            for fila in lector:
                for valor in fila:
                    valor = valor.strip()

                    if valor == "":
                        invalidas += 1
                        continue

                    try:
                        numero = int(valor)

                        if self.buscar(numero):
                            duplicadas += 1
                        else:
                            self.insertar(numero)
                            cargadas += 1

                    except ValueError:
                        invalidas += 1

        return cargadas, duplicadas, invalidas

    def graficar(self, nombre="arbolB"):
        dot = Digraph()

        def agregar_nodos(nodo, padre=None):
            nodo_id = str(id(nodo))

            if len(nodo.claves) == 0:
                etiqueta = "Vacío"
            else:
                etiqueta = "|".join(str(k) for k in nodo.claves)

            dot.node(nodo_id, etiqueta, shape="record")

            if padre:
                dot.edge(padre, nodo_id)

            for hijo in nodo.hijos:
                agregar_nodos(hijo, nodo_id)

        agregar_nodos(self.raiz)
        dot.render(nombre, format="png", cleanup=True)
        print(f"Árbol generado correctamente: {nombre}.png")


def pedir_entero(mensaje):
    while True:
        try:
            valor = int(input(mensaje))
            return valor
        except ValueError:
            print("Error: debe ingresar un número entero.")


def pedir_grado():
    while True:
        grado = pedir_entero("Ingrese el grado del Árbol B: ")

        if grado >= 3:
            return grado
        else:
            print("Error: el grado del Árbol B debe ser mayor o igual a 3.")


def insertar_claves_desde_texto(arbol):
    claves = input("Ingrese una o varias claves separadas por coma: ")
    lista_claves = claves.split(",")

    insertadas = 0
    duplicadas = 0
    invalidas = 0

    for clave in lista_claves:
        clave = clave.strip()

        if clave == "":
            invalidas += 1
            continue

        try:
            numero = int(clave)

            if arbol.buscar(numero):
                duplicadas += 1
            else:
                arbol.insertar(numero)
                insertadas += 1

        except ValueError:
            invalidas += 1

    print(f"Claves insertadas: {insertadas}")
    print(f"Claves duplicadas ignoradas: {duplicadas}")
    print(f"Valores inválidos ignorados: {invalidas}")


def mostrar_menu():
    print("\n========= MENÚ =========")
    print("1. Insertar clave")
    print("2. Buscar clave")
    print("3. Eliminar clave")
    print("4. Mostrar recorrido")
    print("5. Cargar archivo CSV")
    print("6. Graficar árbol")
    print("7. Salir")


def menu():
    grado = pedir_grado()
    arbol = ArbolB(grado)

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            insertar_claves_desde_texto(arbol)

        elif opcion == "2":
            clave = pedir_entero("Ingrese clave a buscar: ")

            if arbol.buscar(clave):
                print("Clave encontrada.")
            else:
                print("Clave NO encontrada.")

        elif opcion == "3":
            clave = pedir_entero("Ingrese clave a eliminar: ")

            if arbol.eliminar(clave):
                print("Clave eliminada.")
            else:
                print("Clave no encontrada.")

        elif opcion == "4":
            print("\nRecorrido del Árbol:")
            print(arbol.recorrer())

        elif opcion == "5":
            archivo = input("Ingrese nombre del archivo CSV: ").strip()

            try:
                cargadas, duplicadas, invalidas = arbol.cargar_csv(archivo)

                print("Archivo procesado correctamente.")
                print(f"Claves cargadas: {cargadas}")
                print(f"Claves duplicadas ignoradas: {duplicadas}")
                print(f"Valores inválidos ignorados: {invalidas}")

            except FileNotFoundError:
                print("Error: no se encontró el archivo.")
                print("Verifique que el archivo esté en la misma carpeta del programa o escriba la ruta completa.")

            except Exception as e:
                print("Error al cargar el archivo.")
                print(f"Detalle del error: {e}")

        elif opcion == "6":
            try:
                arbol.graficar()
            except Exception as e:
                print("Error al generar el gráfico.")
                print("Verifique que Graphviz esté instalado y configurado correctamente.")
                print(f"Detalle del error: {e}")

        elif opcion == "7":
            print("Programa finalizado.")
            break

        else:
            print("Opción inválida. Seleccione una opción del 1 al 7.")


menu()