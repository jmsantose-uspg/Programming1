def celsius_a_fahrenheit(c):
    """
    Convierte una temperatura de Celsius a Fahrenheit.
    Fórmula: F = (C × 9/5) + 32
    """
    return c * 9/5 + 32  # aplicar la fórmula de conversión


def fahrenheit_a_celsius(f):
    """
    Convierte una temperatura de Fahrenheit a Celsius.
    Fórmula: C = (F - 32) × 5/9
    """
    return (f - 32) * 5/9  # aplicar la fórmula de conversión


def celsius_a_kelvin(c):
    """
    Convierte una temperatura de Celsius a Kelvin.
    Fórmula: K = C + 273.15
    """
    return c + 273.15  # sumar 273.15 a los grados Celsius


def convertir(valor, origen, destino):
    """
    Función principal que convierte temperaturas entre tres escalas.
    Parámetros:
        - valor: número de temperatura a convertir
        - origen: escala de origen ('C', 'F' o 'K')
        - destino: escala destino ('C', 'F' o 'K')
    Retorna: valor convertido o None si la conversión no es válida
    """
    
    # Si el origen es Celsius, convertir hacia Fahrenheit o Kelvin
    if origen == 'C':
        if destino == 'F':  # Celsius → Fahrenheit
            return celsius_a_fahrenheit(valor)
        if destino == 'K':  # Celsius → Kelvin
            return celsius_a_kelvin(valor)
    
    # Si el origen es Fahrenheit, convertir hacia Celsius o Kelvin
    elif origen == 'F':
        if destino == 'C':  # Fahrenheit → Celsius
            return fahrenheit_a_celsius(valor)
        if destino == 'K':  # Fahrenheit → Kelvin
            # primero convertir F → C, luego C → K (conversión en dos pasos)
            return celsius_a_kelvin(fahrenheit_a_celsius(valor))
    
    # Si el origen es Kelvin, convertir hacia Celsius o Fahrenheit
    elif origen == 'K':
        if destino == 'C':  # Kelvin → Celsius
            return valor - 273.15  # restar 273.15 para pasar de Kelvin a Celsius
        if destino == 'F':  # Kelvin → Fahrenheit
            # primero K → C, luego C → F (conversión en dos pasos)
            return celsius_a_fahrenheit(valor - 273.15)
    
    # Si la conversión no es válida (escalas incorrectas)
    return None

