from graphviz import Digraph
import os
os.environ["PATH"] += os.pathsep + r"C:\Program Files\Graphviz\bin"

class Nodo:
    #constructor
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None #hijo menor 
        self.derecha = None #hijo mayor

class ArbolBinario:
    def __init__(self):
        self.raiz = None
    
    def insertar(self,valor):
        if self.raiz is None:
            self.raiz = Nodo(valor)
        else:
            self._insertar(valor, self.raiz)

    def _insertar(self, valor , nodo):
        if valor < nodo.valor:
            if nodo.izquierda is None:
                nodo.izquierda = Nodo(valor)
            else:
                self._insertar(valor,nodo.izquierda)
        else:
            if nodo.derecha is None:
                nodo.derecha = Nodo(valor)
            else:
                self ._insertar(valor, nodo.derecha)
            
    def buscar (self, valor):
        return self._buscar(valor, self.raiz)
    
    def _buscar(self, valor, nodo):
        if nodo is None:
            return False
        if valor == nodo.valor:
            return True
        elif valor < nodo.valor:
            return self._buscar(valor, nodo.izquierda)
        else:
            return self._buscar(valor, nodo.derecha)
    def eliminar(self, valor):
        self.raiz = self._eliminar(valor, self.raiz)    
    def _eliminar(self, valor, nodo):
        if nodo is None:
            return nodo
        if valor < nodo.valor:
            nodo.izquierda = self._eliminar(valor, nodo.izquierda)
        elif valor > nodo.valor:
            nodo.derecha = self._eliminar(valor, nodo.derecha)
        else:
            if nodo.izquierda is None:
                return nodo.derecha
            elif nodo.derecha is None:
                return nodo.izquierda
            temp = self._minimo(nodo.derecha)
            nodo.valor = temp.valor
            nodo.derecha = self._eliminar(temp.valor, nodo.derecha)
        return nodo
    def _minimo(self, nodo):
        actual = nodo
        while actual.izquierda is not None:
            actual = actual.izquierda
        return actual

    def graficar(self):
        dot = Digraph()
        def recorrer(nodo):
            if nodo:
                dot.node(str(id(nodo.valor)), str(nodo.valor))
                if nodo.izquierda:
                    dot.node(str(id(nodo.izquierda.valor)), str(nodo.izquierda.valor))
                    dot.edge(str(id(nodo.valor)), str(id(nodo.izquierda.valor)))
                    recorrer(nodo.izquierda)
                if nodo.derecha:
                    dot.node(str(id(nodo.derecha.valor)), str(nodo.derecha.valor))
                    dot.edge(str(id(nodo.valor)), str(id(nodo.derecha.valor)))
                    recorrer(nodo.derecha)
        recorrer(self.raiz)
        dot.render("arbol_biario", view=True)
    
    def cargar_archivo(self, nombre_archivo):

      with open(nombre_archivo, 'r') as archivo:

        for linea in archivo:

            numeros = linea.replace(',', ' ').split()

            for numero in numeros:

                try:
                    self.insertar(int(numero))
                except:
                    pass
def menu():

    arbol = ArbolBinario()

    while True:

        print("\n**********MENU***********")
        print("1. INSERTAR NODO")
        print("2. BUSCAR NODO")
        print("3. ELIMINAR NODO")
        print("4. CARGAR ARCHIVO")
        print("5. MOSTRAR ARBOL")
        print("6. SALIR")

        opcion = input("SELECCIONE UNA OPCION: ")

        if opcion == "1":
            num = int(input("Ingrese Numero: "))
            arbol.insertar(num)
            print("Nodo insertado correctamente")

        elif opcion == "2":
            num = int(input("Ingrese Numero: "))
            if arbol.buscar(num):
                print("Nodo encontrado")
            else:
                print("Nodo no encontrado")

        elif opcion == "3":
            num = int(input("Ingrese Numero para eliminar: "))
            arbol.eliminar(num)
            print("Nodo eliminado correctamente")

        elif opcion == "4":
            nombre_archivo = input("Ingrese el nombre del archivo: ").strip('"')

            if not nombre_archivo.endswith(".txt"):
                nombre_archivo += ".txt"

            try:
                arbol.cargar_archivo(nombre_archivo)
                print("Archivo cargado correctamente")
            except FileNotFoundError:
                print("Error: el archivo no se encontró")

        elif opcion == "5":
            arbol.graficar()

        elif opcion == "6":
            print("Saliendo del programa...")
            break

        else:
            print("Opcion invalida")


menu()