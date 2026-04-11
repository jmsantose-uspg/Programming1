def celsius_a_fahrenheit(c):
    return c * 9/5 + 32

def fahrenheit_a_celsius(f):
    return (f - 32) * 5/9

def celsius_a_kelvin(c):
    return c + 273.15

def convertir(valor, origen, destino):
    if origen == 'C':
        if destino == 'F': return celsius_a_fahrenheit(valor)
        if destino == 'K': return celsius_a_kelvin(valor)
    elif origen == 'F':
        if destino == 'C': return fahrenheit_a_celsius(valor)
        if destino == 'K': 
            # primero F → C, luego C → K
            return celsius_a_kelvin(fahrenheit_a_celsius(valor))
    elif origen == 'K':
        if destino == 'C': return valor - 273.15
        if destino == 'F': return celsius_a_fahrenheit(valor - 273.15)
    return None

