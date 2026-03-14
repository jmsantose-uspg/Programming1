def area_circulo(radio):
    """
    Calcula el área de un círculo usando la fórmula π * r².

    Args:
        radio (float): El radio del círculo.

    Returns:
        float: El área del círculo.
    """
    pi = 3.1416
    return pi * radio ** 2


def es_primo(n):
    """
    Determina si un número es primo.

    Args:
        n (int): Número entero a evaluar.

    Returns:
        bool: True si el número es primo, False en caso contrario.
    """
    if n <= 1:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True


def factorial(n):
    """
    Calcula el factorial de un número entero no negativo.

    Args:
        n (int): Número entero no negativo.

    Returns:
        int: El factorial de n.
    """
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i

    return resultado


def fibonacci(n):
    """
    Retorna los primeros n números de la sucesión de Fibonacci.

    Args:
        n (int): Cantidad de números de Fibonacci a generar.

    Returns:
        list: Lista con los primeros n números de Fibonacci.
    """
    secuencia = []
    a, b = 0, 1

    for i in range(n):
        secuencia.append(a)
        a, b = b, a + b

    return secuencia


def celsius_a_fahrenheit(c):
    """
    Convierte temperatura de Celsius a Fahrenheit.

    Args:
        c (float): Temperatura en Celsius.

    Returns:
        float: Temperatura en Fahrenheit.
    """
    return (c * 9 / 5) + 32


def maximo(lista):
    """
    Retorna el valor máximo de una lista sin usar max().

    Args:
        lista (list): Lista de números.

    Returns:
        int/float: Número mayor de la lista.
    """
    mayor = lista[0]

    for elemento in lista:
        if elemento > mayor:
            mayor = elemento

    return mayor


while True:

    print("\n--- Biblioteca Matemática ---")
    print("1. Área de un círculo")
    print("2. Verificar número primo")
    print("3. Calcular factorial")
    print("4. Serie de Fibonacci")
    print("5. Convertir Celsius a Fahrenheit")
    print("6. Encontrar máximo de una lista")
    print("7. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        radio = float(input("Ingrese el radio del círculo: "))
        resultado = area_circulo(radio)
        print("El área del círculo es:", resultado)

    elif opcion == "2":
        numero = int(input("Ingrese un número: "))
        if es_primo(numero):
            print("El número es primo")
        else:
            print("El número no es primo")

    elif opcion == "3":
        numero = int(input("Ingrese un número: "))
        print("El factorial es:", factorial(numero))

    elif opcion == "4":
        n = int(input("¿Cuántos números de Fibonacci desea?: "))
        print("Serie Fibonacci:", fibonacci(n))

    elif opcion == "5":
        c = float(input("Ingrese temperatura en Celsius: "))
        print("Temperatura en Fahrenheit:", celsius_a_fahrenheit(c))

    elif opcion == "6":
        datos = input("Ingrese números separados por coma: ")
        lista = [float(x) for x in datos.split(",")]
        print("El número máximo es:", maximo(lista))

    elif opcion == "7":
        print("Programa finalizado.")
        break

    else:
        print("Opción inválida.")

    
