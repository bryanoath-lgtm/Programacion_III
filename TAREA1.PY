def generar_png(self, nombre_archivo="lista_doble"):

    ruta_actual = os.path.dirname(os.path.abspath(__file__))
    ruta_completa = os.path.join(ruta_actual, nombre_archivo)

    dot = Digraph("ListaDoble")
    dot.attr(rankdir="LR")

    dot.node("NoneL", "None", shape="plaintext")
    dot.node("NoneR", "None", shape="plaintext")

    if self.inicio is None:
        dot.edge("NoneL", "NoneR")
    else:
        actual = self.inicio
        i = 0
        ids = []

        while actual is not None:
            node_id = f"N{i}"
            label = f"{actual.nombre}\\n{actual.apellido}\\n{actual.carnet}"
            dot.node(node_id, label, shape="box")
            ids.append(node_id)

            actual = actual.siguiente
            i += 1

        dot.edge("NoneL", ids[0])
        dot.edge(ids[-1], "NoneR")

        for j in range(len(ids) - 1):
            dot.edge(ids[j], ids[j + 1])
            dot.edge(ids[j + 1], ids[j])

    dot.render(ruta_completa, format="png", cleanup=True)
