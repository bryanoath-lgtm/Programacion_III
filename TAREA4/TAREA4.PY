from graphviz import Digraph #sirve para dibujar estructuras en forma de árbol
import csv #sirve para los archivos csv
import os #sirve para manejar archivos

class Nodo:
    def __init__(self,valor):
        self.valor =valor
        self.izquierda = None # hijo izquierdo
        self.derecha = None #hijo derecho
        self.altura = 1 # balance del arbol

class ArbolABB:
    def __init__(self):
        self.raiz = None

    def buscar(self,raiz, valor):
        if raiz is None or raiz.valor == valor:
            return raiz
        if valor < raiz.valor: #si el valor es menor que la raiz
            return self.buscar(raiz.izquierda, valor)  #va a la izquierda
        else:
            return self.buscar(raiz.derecha, valor) #mayor va a la derecha

class ArbolAVL(ArbolABB):

    def altura(self, nodo):
        return nodo.altura if nodo else 0 #devuelve la altura del nodo, si el nodo es None devuelve 0

    #balances
    def obtener_balance(self, nodo):
        return self.altura(nodo.izquierda) - self.altura(nodo.derecha) #izquierda menos derecha

    #Rotaciones
    def rotacion_derecha(self, y):
        x = y.izquierda #hijo izquierdo de y
        T2 = x.derecha #hijo derecho de x

        #realizar rotacion
        x.derecha = y
        y.izquierda = T2

        #actualizar alturas
        y.altura = 1 + max(self.altura(y.izquierda), self.altura(y.derecha))
        x.altura = 1 + max(self.altura(x.izquierda), self.altura(x.derecha))
        return x #nueva raiz ya no es y sino x

    def rotacion_izquierda(self, x):
        y = x.derecha #hijo derecho de x
        T2 = y.izquierda #hijo izquierdo de y

        #realizar rotacion
        y.izquierda = x
        x.derecha = T2

        #actualizar alturas
        x.altura = 1 + max(self.altura(x.izquierda), self.altura(x.derecha))
        y.altura = 1 + max(self.altura(y.izquierda), self.altura(y.derecha))
        return y #nueva raiz ya no es x sino y

    def insertar(self, raiz, valor):#inserta un nuevo nodo con el valor dado en el árbol AVL
        if not raiz:
            return Nodo(valor) #si la raiz es None, se crea un nuevo nodo con el valor dado
        elif valor < raiz.valor:
            raiz.izquierda = self.insertar(raiz.izquierda, valor) #si el valor es menor que la raiz, se inserta en el subarbol izquierdo
        else:
            raiz.derecha = self.insertar(raiz.derecha, valor) #si el valor es mayor que la raiz, se inserta en el subarbol derecho

        #actualizar altura del ancestro
        raiz.altura = 1 + max(self.altura(raiz.izquierda), self.altura(raiz.derecha))
        balance = self.obtener_balance(raiz)

        #caso izquierda izquierda
        if balance > 1 and valor < raiz.izquierda.valor:
            return self.rotacion_derecha(raiz)

        #caso derecha derecha
        if balance < -1 and valor > raiz.derecha.valor:
            return self.rotacion_izquierda(raiz)

        #caso izquierda derecha
        if balance > 1 and valor > raiz.izquierda.valor:
            raiz.izquierda = self.rotacion_izquierda(raiz.izquierda)
            return self.rotacion_derecha(raiz)

        #caso derecha izquierda
        if balance < -1 and valor < raiz.derecha.valor:
            raiz.derecha = self.rotacion_derecha(raiz.derecha)
            return self.rotacion_izquierda(raiz)

        return raiz

    def minimo(self, nodo):
        while nodo.izquierda:# mientras el nodo tenga un hijo a la izquierda se mueve a la izquierda
            nodo = nodo.izquierda
        return nodo

    def eliminar(self, raiz, valor):
        if not raiz:
            return raiz
        if valor < raiz.valor: # si el valor es menor que la raiz, se elimina del subarbol izquierdo
            raiz.izquierda = self.eliminar(raiz.izquierda, valor)
        elif valor > raiz.valor: #si el valor es mayor que la raiz, se elimina del subarbol derecho
            raiz.derecha = self.eliminar(raiz.derecha, valor)
        else: 
            if not raiz.izquierda: #si la raiz no tiene hijo izquierdo, se devuelve el hijo derecho
                return raiz.derecha
            elif not raiz.derecha: #si la raiz no tiene hijo derecho, se devuelve el hijo izquierdo
                return raiz.izquierda

            temp = self.minimo(raiz.derecha) #si la raiz tiene dos hijos
            raiz.valor = temp.valor
            raiz.derecha = self.eliminar(raiz.derecha, temp.valor)

        raiz.altura = 1 + max(self.altura(raiz.izquierda), self.altura(raiz.derecha))
        balance = self.obtener_balance(raiz)

        if balance > 1 and self.obtener_balance(raiz.izquierda) >= 0:
            return self.rotacion_derecha(raiz)

        if balance > 1 and self.obtener_balance(raiz.izquierda) < 0:
            raiz.izquierda = self.rotacion_izquierda(raiz.izquierda)
            return self.rotacion_derecha(raiz)

        if balance < -1 and self.obtener_balance(raiz.derecha) <= 0:
            return self.rotacion_izquierda(raiz)

        if balance < -1 and self.obtener_balance(raiz.derecha) > 0:
            raiz.derecha = self.rotacion_derecha(raiz.derecha)
            return self.rotacion_izquierda(raiz)

        return raiz

    def graficar(self, raiz):
        dot = Digraph()

        def recorrer(nodo):
            if nodo:
                # usar id único para evitar errores de conexión
                dot.node(str(id(nodo)), str(nodo.valor)) #crea un nodo con el valor del nodo

                if nodo.izquierda:
                    dot.edge(str(id(nodo)), str(id(nodo.izquierda)))
                    recorrer(nodo.izquierda)

                if nodo.derecha:
                    dot.edge(str(id(nodo)), str(id(nodo.derecha)))
                    recorrer(nodo.derecha)

        recorrer(raiz)
        dot.render('arbol_avl', format='png', view=True) #genera un archivo png con el arbol AVL

    def cargar_csv(self, ruta):
        with open(ruta, newline='') as archivo:
            reader = csv.reader(archivo)
            for fila in reader:
                for valor in fila:
                    self.raiz = self.insertar(self.raiz, int(valor)) #inserta cada valor del archivo csv en el arbol AVL


def menu():
    arbol = ArbolAVL()

    while True:
        print("1. Cargar datos desde CSV")
        print("2. Insertar un valor")
        print("3. buscar un valor")
        print("4. Eliminar un valor")
        print("5. Graficar el árbol")
        print("6. Salir")

        opcion = input("seleciones una opcion:   ")

        if opcion == '1':
            ruta = input("Ingrese la ruta del archivo CSV: ").strip().replace('"', '')
            arbol.cargar_csv(ruta)

        elif opcion == '2':
            valor = int(input("Ingrese el valor a insertar:    "))
            arbol.raiz = arbol.insertar(arbol.raiz, valor)

        elif opcion == '3':
            valor = int(input("Ingrese el valor a buscar: "))
            nodo = arbol.buscar(arbol.raiz, valor)
            if nodo:
                print(f"Valor {valor} encontrado en el árbol.")
            else:
                print(f"Valor {valor} no encontrado en el árbol.")

        elif opcion == '4':
            valor = int(input("Ingrese el valor a eliminar: "))
            arbol.raiz = arbol.eliminar(arbol.raiz, valor)

        elif opcion == '5':
            arbol.graficar(arbol.raiz)

        elif opcion == '6':
            break

        else:
            print("Opción no válida. Por favor, seleccione una opción del 1 al 6.")


menu()