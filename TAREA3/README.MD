Árbol Binario de Búsqueda en Python

## Integrantes
Marvin Eleazar Vásquez Gómez – 9490-18-8656 – 100% Participación

Alfredo Bryan Hernandez Galindo – 9490-20-16716 – 100% Participación

## Descripción

Este proyecto implementa un **Árbol Binario de Búsqueda (ABB)** en Python, permitiendo realizar operaciones básicas como inserción, búsqueda, eliminación de nodos, carga de datos desde archivo y visualización gráfica mediante Graphviz.

El programa funciona mediante un menú interactivo en consola.



## Funcionalidades

* Insertar nodos en el árbol
* Buscar un valor dentro del árbol
* Eliminar nodos
* Cargar datos desde un archivo `.txt`
* Visualizar el árbol gráficamente con Graphviz


## Estructura del Proyecto


TAREA3/
│── TAREA3.PY          # Programa principal
│── datos.txt          # Archivo de entrada (opcional)
│── arbol_binario.png  # Imagen generada del árbol
│── README.md          # Documentación del proyecto



## Requisitos

Antes de ejecutar el programa, revisar de tener instalado:

### 1. Python

* Versión recomendada: 3.x

### 2. Librería Graphviz (Python)

pip install graphviz

### 3. Graphviz (Software)

Descargar e instalar desde:
https://graphviz.org/download/

Luego agregar la ruta al PATH, por ejemplo:

C:\Program Files\Graphviz\bin



## Ejecución

1. Ubicarse en la carpeta del proyecto
2. Ejecutar el programa:


python TAREA3.py


3. Seleccionar una opción del menú:


1. INSERTAR NODO
2. BUSCAR NODO
3. ELIMINAR NODO
4. CARGAR ARCHIVO
5. MOSTRAR ARBOL
6. SALIR



## Uso de archivo de entrada

El archivo debe contener números separados por comas o espacios.

### Ejemplo (`datos.txt`):


50,30,70,20,40,60,80


O también:


50 30 70 20 40 60 80


Para cargarlo:


Ingrese el nombre del archivo: datos.txt


---

## Visualización del árbol

Al seleccionar la opción **"MOSTRAR ARBOL"**, el programa:

* Genera un archivo gráfico (`.png`)
* Muestra la estructura del árbol binario

---


## Consideraciones

* Es importante que el archivo esté en la misma carpeta o indicar la ruta completa
* Graphviz debe estar correctamente instalado para visualizar el árbol

---


