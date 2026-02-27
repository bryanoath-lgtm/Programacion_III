Lista Doblemente Enlazada en Python
------ Integrantes: ------

Marvin Eleazar Vásquez Gómez – 9490-18-8656 – 100% Participación

Alfredo Bryan Hernandez Galindo – 9490-20-16716 – 100% Participación

------ Descripción ------

Este proyecto implementa una Lista Doblemente Enlazada en Python con una interfaz de línea de comandos (CLI).
Cada nodo contiene:

    -Nombre
    -Apellido
    -Carnet
    -Referencia al nodo siguiente
    -Referencia al nodo anterio

El programa permite insertar nodos al principio, insertar al final, eliminar por carnet y mostrar la lista.
Utiliza Graphviz para generar una representación visual de la lista después de cada inserción o eliminación en el formato:
________________________________________________________
    None <- Nodo1 <-> Nodo2 <-> ... <-> NodoN -> None
________________________________________________________

El programa utiliza Graphviz para generar automáticamente una imagen en formato PNG que representa visualmente la estructura de la lista después de cada operación de inserción o eliminación.


------ REQUISITOS ------

    -Python 3.x
    -Graphviz instalado en el sistema
    -Librería graphviz para Python

------ INSTALACIÓN ------

1. Instalar Graphviz en Windows desde su página oficial.
2. Verificar instalación ejecutando en terminal:

    -dot -V

3. Instalar la librería de Python ejecutando:
    -python -m pip install graphviz

------ EJECUCIÓN ------

Ubicarse en la carpeta del proyecto y ejecutar:

    -python TAREA1.py

------ FUNCIONALIDADES ------

1. Insertar al principio
2. Insertar al final
3. Eliminar por carnet
4. Mostrar lista
5. Generación automática de imagen PNG con Graphviz
