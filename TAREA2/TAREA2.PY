# definicion de la funcion
def convetir_a_binario(numero):
    if numero < 0:
        return "-" + convetir_a_binario(-numero)

    if numero < 2:
        return str(numero)

    return convetir_a_binario(numero // 2) + str(numero % 2)


# contar digitos
def contar_digitos(numero):
    numero = abs(numero)

    if numero < 10:
        return 1

    return 1 + contar_digitos(numero // 10)


# raiz cuadrada
def calcular_raiz_cuadrada(numero, raiz=0):
    if raiz * raiz > numero:
        return raiz - 1

    return calcular_raiz_cuadrada(numero, raiz + 1)


def raiz_cuadrada_entera(numero):
    if numero < 0:
        return "No tiene raiz cuadrada real"

    return calcular_raiz_cuadrada(numero)


# convertir numero romano a decimal
def convertir_a_decimal(romano):
    valores = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
               'C': 100, 'D': 500, 'M': 1000}

    if len(romano) == 0:
        return 0

    if len(romano) == 1:
        return valores[romano]

    if valores[romano[0]] < valores[romano[1]]:
        return valores[romano[1]] - valores[romano[0]] + convertir_a_decimal(romano[2:])
    else:
        return valores[romano[0]] + convertir_a_decimal(romano[1:])


# suma de numeros enteros
def Suma_numeros_enteros(numero):
    if numero <= 0:
        return 0

    return numero + Suma_numeros_enteros(numero - 1)


# Menu
def Menu():
    while True:
        print("\n****** MENU *******")
        print("1. Convertidor a Binario")
        print("2. Contador de Digitos")
        print("3. Raiz Cuadrada Entera")
        print("4. Convertidor Romanos a Decimal")
        print("5. Suma de Numeros Enteros")
        print("6. SALIR")

        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            numero = int(input("Ingrese un numero entero: "))
            print("Binario:", convetir_a_binario(numero))

        elif opcion == "2":
            numero = int(input("Ingrese Numero: "))
            print("Cantidad de Digitos:", contar_digitos(numero))

        elif opcion == "3":
            numero = int(input("Ingrese un numero entero: "))
            print("Raiz cuadrada:", raiz_cuadrada_entera(numero))

        elif opcion == "4":
            romano = input("Ingrese Numero Romano en Mayuscula: ").upper()
            print("Numero decimal:", convertir_a_decimal(romano))

        elif opcion == "5":
            numero = int(input("Ingrese Numero Entero: "))
            print("Suma:", Suma_numeros_enteros(numero))

        elif opcion == "6":
            print("Saliendo del programa...")
            break

        else:
            print("Opcion Invalida")


# ejecutar programa
if __name__ == "__main__":
    Menu()