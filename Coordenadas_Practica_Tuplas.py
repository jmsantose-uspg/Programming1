# 1. Crear una tupla con coordenadas de tu casa
coordenadas = (14.6349, -90.5069)

# 2. Desempaquetar en variables lat, lon
lat, lon = coordenadas
print("Latitud:", lat)
print("Longitud:", lon)


# 3. Función que retorna (min, max, promedio)
def estadisticas(lista):
    minimo = min(lista)
    maximo = max(lista)
    promedio = sum(lista) / len(lista)
    return (minimo, maximo, promedio)

# Probar función
numeros = [10, 20, 30, 40, 50]
resultado = estadisticas(numeros)
print("\nEstadísticas:", resultado)


# 4. Usar tuplas como claves de un diccionario
distancias = {
    ("Guate", "Escuintla"): 58,
    ("Guate", "Antigua"): 45
}

print("\nDistancias:")
for ruta, km in distancias.items():
    print(ruta, ":", km)


# 5. Intentar modificar una tupla (esto dará error)
# coordenadas[0] = 15.0000

# Explicación:
# Las tuplas son inmutables, no se pueden modificar después de crearse.