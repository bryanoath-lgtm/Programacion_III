# TAREA 4 - Árbol AVL en Python
------ Integrantes: ------

Marvin Eleazar Vásquez Gómez – 9490-18-8656 – 100% Participación

Alfredo Bryan Hernandez Galindo – 9490-20-16716 – 100% Participación

# TAREA 4 - Árbol AVL en Python

## Descripción
Este proyecto implementa un **Árbol AVL** en Python, es decir, un árbol binario de búsqueda auto-balanceado.

El programa permite al usuario trabajar con el árbol mediante un menú en consola, con las siguientes opciones:

- Cargar datos desde un archivo CSV
- Insertar un valor manualmente
- Buscar un valor dentro del árbol
- Eliminar un valor
- Graficar el árbol en formato PNG
- Salir del programa

Además, el árbol se balancea automáticamente después de cada inserción o eliminación por medio de rotaciones, manteniendo una estructura eficiente para las operaciones.

## Objetivo del programa
Simular el funcionamiento de un árbol AVL, aplicando los conceptos de:

- Árbol binario de búsqueda
- Altura de nodos
- Factor de balance
- Rotaciones simples
- Rotaciones dobles
- Recorridos recursivos
- Carga de datos desde archivos
- Generación gráfica de estructuras de datos

## Estructura del programa

### Clase `Nodo`
Representa cada nodo del árbol.

Atributos:
- `valor`: dato almacenado en el nodo
- `izquierda`: referencia al hijo izquierdo
- `derecha`: referencia al hijo derecho
- `altura`: altura del nodo dentro del árbol

### Clase `ArbolABB`
Clase base que contiene la operación de búsqueda dentro del árbol.

Método principal:
- `buscar(raiz, valor)`: localiza un valor dentro del árbol

### Clase `ArbolAVL`
Hereda de `ArbolABB` e implementa toda la lógica del árbol AVL.

Métodos principales:
- `altura(nodo)`: devuelve la altura del nodo
- `obtener_balance(nodo)`: calcula el factor de balance
- `rotacion_derecha(y)`: realiza una rotación simple a la derecha
- `rotacion_izquierda(x)`: realiza una rotación simple a la izquierda
- `insertar(raiz, valor)`: inserta un valor y rebalancea el árbol
- `minimo(nodo)`: obtiene el nodo con menor valor en un subárbol
- `eliminar(raiz, valor)`: elimina un valor y rebalancea el árbol
- `graficar(raiz)`: genera una imagen del árbol
- `cargar_csv(ruta)`: carga datos numéricos desde un archivo CSV

### Función `menu()`
Controla la interacción con el usuario por medio de un menú en consola.

## Funcionalidades del sistema

### 1. Cargar datos desde CSV
Permite cargar múltiples valores numéricos desde un archivo CSV.

Ejemplo de contenido de archivo:
csv
10,20,30
5,15,25
40,50

### 2. Insertar un valor

Permite ingresar manualmente un número entero para insertarlo en el árbol.

### 3. Buscar un valor

Permite verificar si un valor existe dentro del árbol.

### 4. Eliminar un valor

Permite eliminar un valor existente del árbol, aplicando rebalanceo automático si es necesario.

### 5. Graficar el árbol

Genera una imagen del árbol AVL en formato PNG usando Graphviz.

### 6. Salir

Finaliza la ejecución del programa.

## Requisitos

Para ejecutar correctamente el programa se necesita:

Python 3
Librería graphviz de Python
Graphviz instalado en el sistema operativo
Instalación de dependencias

## Uso del programa
Al ejecutar el archivo, aparecerá un menú como este:
1. Cargar datos desde CSV
2. Insertar un valor
3. Buscar un valor
4. Eliminar un valor
5. Graficar el árbol
6. Salir

## Lógica del árbol AVL

El árbol AVL mantiene el equilibrio calculando el factor de balance de cada nodo:
 - balance = altura(izquierda) - altura(derecha)

Según el resultado, puede aplicar una de las siguientes rotaciones:

- Rotación simple a la derecha
- Rotación simple a la izquierda
- Rotación doble izquierda-derecha
- Rotación doble derecha-izquierda

Esto evita que el árbol se desbalancee y mejora el rendimiento de búsqueda, inserción y eliminación.


## Consideraciones importantes

- El archivo CSV debe contener únicamente valores enteros.
- Si la ruta del archivo es incorrecta, el programa generará error.
- Si se ingresan datos no numéricos, el programa también puede generar error.
- La imagen del árbol se genera al seleccionar la opción de graficar.
- El programa trabaja mediante consola.

## Archivos esperados en el proyecto
- TAREA4.PY
- README.md

