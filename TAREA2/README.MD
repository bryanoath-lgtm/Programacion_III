# Tarea 2 - Métodos Recursivos en Python

Marvin Eleazar Vásquez Gómez – 9490-18-8656 – 100% Participación
Alfredo Bryan Hernandez Galindo – 9490-20-16716 – 100% Participación


Este proyecto contiene la implementación de diferentes métodos recursivos en Python:

- Conversión de número entero a binario
- Conteo de dígitos de un número
- Cálculo de raíz cuadrada entera
- Conversión de número romano a decimal
- Suma de números enteros
- Menú interactivo en consola

Tecnologías utilizadas
- Python 3

Requisitos
- Tener instalado Python 3 en el sistema.
- Contar con una terminal (CMD, PowerShell o terminal integrada de Visual Studio Code).

Cómo ejecutar el programa

1. Descargar o clonar el repositorio.
2. Ubicarse en la carpeta del proyecto desde la terminal.
3. Ejecutar el archivo principal con el siguiente comando:
    - python TAREA2.py

Al ejecutarlo, aparecerá un menú en consola con las diferentes opciones disponibles.

Cómo probar cada funcionalidad

Una vez que el programa esté en ejecución, se mostrará el siguiente menú:

1. Convertidor a Binario
2. Contador de Dígitos
3. Raíz Cuadrada Entera
4. Convertidor Romanos a Decimal
5. Suma de Números Enteros
6. Salir

Para probar cada opción:

1. Convertidor a Binario

Ingresar un número entero positivo o negativo.
El programa mostrará su representación en sistema binario.

Ejemplo:
Entrada: 6
Salida esperada: 110

2. Contador de Dígitos

Ingresar un número entero.
El programa mostrará la cantidad de dígitos que contiene.

Ejemplo:
Entrada: 1234
Salida esperada: 4

3. Raíz Cuadrada Entera

Ingresar un número entero positivo.
El programa calculará la raíz cuadrada entera (la parte entera de la raíz).

Ejemplo:
Entrada: 17
Salida esperada: 4

Si el número es negativo, el programa indicará que no tiene raíz cuadrada real.

4. Convertidor Romanos a Decimal

Ingresar un número romano en mayúsculas.
El programa convertirá el valor romano a su equivalente en número decimal.

Ejemplo:
Entrada: IX
Salida esperada: 9

5. Suma de Números Enteros

Ingresar un número entero positivo.
El programa calculará la suma desde 1 hasta el número ingresado.

Ejemplo:
Entrada: 4
Salida esperada: 10

Estructura del programa

El programa está compuesto por funciones recursivas independientes para cada operación, además de una función Menu() que permite interactuar con el usuario mediante un ciclo repetitivo hasta que se seleccione la opción de salida.

Cada método implementa:
- Un caso base que detiene la recursión.
- Un caso recursivo que reduce el problema hasta llegar al caso base.

Conceptos aplicados
- Recursividad.
- Casos base y casos recursivos.
- Operadores matemáticos (//, %, multiplicación).
- Manipulación de cadenas.
- Control de flujo con condicionales y ciclos.