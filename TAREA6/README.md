# Tarea 6 - Árbol B en Python

## Integrantes

| Nombre | Carnet | Porcentaje de participación |
|---|---|---|
| Marvin Eleazar Vásquez Gómez  | 9490-18-8656 | 100% |
| Alfredo Bryan Hernandez Galindo | 9490-20-16716 | 100% |


## Descripción

Este proyecto implementa un Árbol B configurable por el grado del nodo.  
El programa permite insertar, buscar, eliminar claves, cargar datos desde archivos CSV y generar una representación gráfica del árbol usando Graphviz.

En este proyecto se utiliza la siguiente definición:

- Grado del Árbol B = cantidad máxima de hijos por nodo.
- Máximo de claves por nodo = grado - 1.

Por ejemplo:

- Grado 3: máximo 3 hijos y máximo 2 claves por nodo.
- Grado 4: máximo 4 hijos y máximo 3 claves por nodo.

## Funcionalidades

El programa incluye las siguientes opciones:

1. Insertar claves.
2. Buscar claves.
3. Eliminar claves.
4. Mostrar recorrido del árbol.
5. Cargar archivo CSV.
6. Graficar árbol con Graphviz.
7. Salir del programa.

## Requisitos

Para ejecutar el programa se necesita:

- Python 3.
- Librería `graphviz` de Python.
- Graphviz instalado en el sistema operativo.

## Instalación de dependencias

Instalar la librería de Python:

```bash
pip install graphviz
```

Además, debe instalarse Graphviz en el sistema operativo.

En Windows, se puede descargar desde el sitio oficial de Graphviz.  
Después de instalarlo, verificar que la carpeta `bin` de Graphviz esté agregada al PATH del sistema.

Ejemplo de ruta en Windows:

```text
C:\Program Files\Graphviz\bin
```

## Ejecución del programa

Desde la terminal, ubicarse en la carpeta del proyecto y ejecutar:

```bash
python Tarea6.py
```

## Uso del programa

Al iniciar el programa, se solicita ingresar el grado del Árbol B.

Ejemplo:

```text
Ingrese el grado del Árbol B: 3
```

Luego se muestra el menú principal:

```text
========= MENÚ =========
1. Insertar clave
2. Buscar clave
3. Eliminar clave
4. Mostrar recorrido
5. Cargar archivo CSV
6. Graficar árbol
7. Salir
```

## Insertar claves manualmente

Seleccionar la opción `1` e ingresar las claves separadas por coma.

Ejemplo:

```text
31,11,56,5,7,21,36,69,98,1,6,10,13,22,33,35,54,65,87,100
```

El programa ignora claves duplicadas y valores inválidos.

## Buscar claves

Seleccionar la opción `2` e ingresar la clave a buscar.

Ejemplo:

```text
Ingrese clave a buscar: 31
```

El programa indicará si la clave fue encontrada o no.

## Eliminar claves

Seleccionar la opción `3` e ingresar la clave a eliminar.

Ejemplo:

```text
Ingrese clave a eliminar: 11
```

El programa elimina la clave si existe y mantiene el árbol válido.

## Mostrar recorrido

Seleccionar la opción `4`.

El programa muestra el recorrido ordenado del Árbol B.  
Este recorrido sirve para validar que las claves se mantienen correctamente ordenadas.

## Cargar archivos CSV

Seleccionar la opción `5` e ingresar el nombre del archivo CSV.

Ejemplo:

```text
datos1.csv
```

Los archivos CSV deben estar en la misma carpeta del programa.  
También se puede ingresar la ruta completa del archivo.

Ejemplo en Windows:

```text
D:/Documents/PROGRAMACION_III/datos1.csv
```

## Archivos CSV incluidos

El proyecto incluye tres archivos CSV de prueba:

- `datos1.csv`: contiene 100 claves del 1 al 100.
- `datos2.csv`: contiene 100 claves en orden variado del 1 al 100.
- `datos3.csv`: contiene 100 claves en orden variado del 101 al 200.

Estos archivos permiten probar la carga masiva de datos y la estabilidad del Árbol B.

## Generar gráfico del árbol

Seleccionar la opción `6`.

El programa generará un archivo de imagen llamado:

```text
arbolB.png
```

Este archivo muestra la representación gráfica del Árbol B generado con Graphviz.

## Estructura del proyecto

```text
Tarea6.py
README.md
datos1.csv
datos2.csv
datos3.csv
```


## Notas importantes

- Verificar que Graphviz esté instalado correctamente antes de generar el gráfico.
- Los archivos CSV deben contener claves numéricas enteras.
- El programa ignora valores vacíos, duplicados o no numéricos.
- Para validar el árbol, se recomienda usar la opción `4. Mostrar recorrido` después de insertar o eliminar claves.
