# ========== GENERADOR DE TABLAS DE MULTIPLICAR ==========

def tabla(n, hasta=10):
    """
    Imprime la tabla de multiplicar de un número específico.
    Parámetros:
        - n: número del cual queremos la tabla de multiplicar
        - hasta: límite superior para el multiplicador (por defecto 10)
    """
    # mostrar el encabezado indicando de qué número es la tabla
    print("Tabla del", n)
    
    # bucle desde 1 hasta 'hasta' (inclusive, por eso hasta + 1)
    for i in range(1, hasta + 1):
        # calcular la multiplicación y mostrar el resultado
        # ejemplo: si n=5 e i=3, imprime "5 x 3 = 15"
        print(n, "x", i, "=", n * i)
    
    # imprimir una línea en blanco para separar las tablas
    print()


def es_primo(n):
    """
    Verifica si un número es primo (solo divisible entre 1 y sí mismo).
    Parámetro: n - número a verificar
    Retorna: True si es primo, False si no lo es
    """
    # los números menores a 2 no son primos por definición
    if n < 2:
        return False
    
    # necesitamos verificar divisores desde 2 hasta la raíz cuadrada de n
    # int(n ** 0.5) calcula la raíz cuadrada de n (n ** 0.5 es lo mismo que √n)
    # rango va desde 2 hasta la raíz cuadrada (sin incluir la raíz + 1)
    for i in range(2, int(n ** 0.5) + 1):
        # si encontramos un número que divide a n exactamente
        if n % i == 0:  # % es módulo, retorna el residuo de n/i
            return False  # entonces no es primo
    
    # si pasamos el bucle sin encontrar divisores, es primo
    return True


def tablas_primos(limite):
    """
    Genera y muestra las tablas de multiplicar solo de números primos.
    Parámetro: limite - número máximo hasta donde buscar primos
    """
    # iteramos desde 2 hasta el límite (inclusive)
    for num in range(2, limite + 1):
        # verificamos si el número actual es primo
        if es_primo(num):
            # si es primo, imprimimos su tabla de multiplicar
            tabla(num)


# ========== EJECUTAR EL PROGRAMA ==========

# mostrar las tablas de multiplicar de los números primos del 2 al 10
# números primos del 2 al 10: 2, 3, 5, 7
tablas_primos(10)