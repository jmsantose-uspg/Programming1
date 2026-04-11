# Función para imprimir la tabla de multiplicar
def tabla(n, hasta=10):
    print("Tabla del", n)
    for i in range(1, hasta + 1):
        print(n, "x", i, "=", n * i)
    print()


# Función para saber si un número es primo
def es_primo(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True


# Función para imprimir solo tablas de números primos
def tablas_primos(limite):
    for num in range(2, limite + 1):
        if es_primo(num):
            tabla(num)


# Prueba
tablas_primos(10)