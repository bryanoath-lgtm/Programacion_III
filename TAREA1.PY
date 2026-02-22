from graphviz import Digraph


class Nodo:
    """
    Nodo de una Lista Doblemente Enlazada
    """
    def __init__(self, nombre, apellido, carnet):
        self.nombre = nombre
        self.apellido = apellido
        self.carnet = carnet
        self.siguiente = None
        self.anterior = None

    def __str__(self):
        return f"[{self.nombre} {self.apellido} ({self.carnet})]"


class ListaDoble:
    def __init__(self):
        self.inicio = None
        self.fin = None  # cola para inserción rápida al final

    def insertar_al_principio(self, nombre, apellido, carnet):
        nuevo = Nodo(nombre, apellido, carnet)

        if self.inicio is None:
            self.inicio = nuevo
            self.fin = nuevo
        else:
            nuevo.siguiente = self.inicio
            self.inicio.anterior = nuevo
            self.inicio = nuevo

    def insertar_al_final(self, nombre, apellido, carnet):
        nuevo = Nodo(nombre, apellido, carnet)

        if self.fin is None:
            self.inicio = nuevo
            self.fin = nuevo
        else:
            self.fin.siguiente = nuevo
            nuevo.anterior = self.fin
            self.fin = nuevo

    def eliminar_por_valor(self, carnet):
        if self.inicio is None:
            return False

        actual = self.inicio

        while actual is not None:
            if actual.carnet == carnet:

                # Caso 1: es el primero
                if actual.anterior is None:
                    self.inicio = actual.siguiente
                    if self.inicio is not None:
                        self.inicio.anterior = None
                    else:
                        self.fin = None

                # Caso 2: es el último
                elif actual.siguiente is None:
                    self.fin = actual.anterior
                    self.fin.siguiente = None

                # Caso 3: está en medio
                else:
                    actual.anterior.siguiente = actual.siguiente
                    actual.siguiente.anterior = actual.anterior

                return True

            actual = actual.siguiente

        return False

    def mostrar_lista(self):
        if self.inicio is None:
            print("La lista está vacía")
            return

        actual = self.inicio
        resultado = "None <- "

        while actual is not None:
            resultado += str(actual)
            if actual.siguiente is not None:
                resultado += " <-> "
            actual = actual.siguiente

        resultado += " -> None"
        print(resultado)

    def generar_png(self, nombre_archivo="lista_doble"):

        dot = Digraph("ListaDoble")
        dot.attr(rankdir="LR")

        # extremos
        dot.node("NoneL", "None", shape="plaintext")
        dot.node("NoneR", "None", shape="plaintext")

        if self.inicio is None:
            dot.edge("NoneL", "NoneR")
        else:
            actual = self.inicio
            i = 0
            ids = []

            # crear nodos
            while actual is not None:
                node_id = f"N{i}"
                label = f"{actual.nombre}\\n{actual.apellido}\\n{actual.carnet}"
                dot.node(node_id, label, shape="box")
                ids.append(node_id)

                actual = actual.siguiente
                i += 1

            # conectar extremos
            dot.edge("NoneL", ids[0])
            dot.edge(ids[-1], "NoneR")

            # conectar doble enlace
            for j in range(len(ids) - 1):
                dot.edge(ids[j], ids[j + 1])
                dot.edge(ids[j + 1], ids[j])

        dot.render(nombre_archivo, format="png", cleanup=True)


def menu():
    lista = ListaDoble()

    while True:
        print("\n****** MENU ******")
        print("1. Insertar al principio")
        print("2. Insertar al final")
        print("3. Eliminar por valor (carnet)")
        print("4. Mostrar lista")
        print("5. Salir")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            nombre = input("Nombre: ").strip()
            apellido = input("Apellido: ").strip()
            carnet = input("Carnet: ").strip()
            lista.insertar_al_principio(nombre, apellido, carnet)
            lista.generar_png()
            print("Insertado al principio.")

        elif opcion == "2":
            nombre = input("Nombre: ").strip()
            apellido = input("Apellido: ").strip()
            carnet = input("Carnet: ").strip()
            lista.insertar_al_final(nombre, apellido, carnet)
            lista.generar_png()
            print("Insertado al final.")

        elif opcion == "3":
            carnet = input("Ingrese número de carnet a eliminar: ").strip()
            eliminado = lista.eliminar_por_valor(carnet)
            lista.generar_png()
            if eliminado:
                print("Carnet eliminado correctamente.")
            else:
                print("No se encontró el carnet.")

        elif opcion == "4":
            lista.mostrar_lista()

        elif opcion == "5":
            print("Saliendo del programa...")
            break

        else:
            print("Opción inválida. Intente de nuevo.")


if __name__ == "__main__":
    menu()
