# Función para calcular el promedio
def promedio(notas):
    suma = 0
    # recorremos cada nota y la sumamos
    for nota in notas:
        suma = suma + nota
    
    # dividimos entre la cantidad de notas
    return suma / len(notas)


# Función para encontrar la nota mayor (sin usar max)
def mayor(notas):
    # asumimos que la primera es la mayor
    mayor = notas[0]
    
    for nota in notas:
        if nota > mayor:
            mayor = nota
    
    return mayor


# Función para encontrar la nota menor (sin usar min)
def menor(notas):
    # asumimos que la primera es la menor
    menor = notas[0]
    
    for nota in notas:
        if nota < menor:
            menor = nota
    
    return menor


# Función para contar aprobados (mínimo 61 por defecto)
def contar_aprobados(notas, minimo=61):
    contador = 0
    
    for nota in notas:
        if nota >= minimo:
            contador += 1
    
    return contador


# Función para hacer un histograma con asteriscos
def histograma(notas):
    print("\nHistograma:")
    
    for nota in notas:
        # dividimos entre 20 para no hacer demasiados asteriscos
        estrellas = "*" * (nota // 20)
        print(str(nota) + ": " + estrellas)


# Función principal que muestra todo el reporte
def reporte(notas):
    print("===== REPORTE DE NOTAS =====")
    
    print("Lista de notas:", notas)
    print("Promedio:", promedio(notas))
    print("Nota más alta:", mayor(notas))
    print("Nota más baja:", menor(notas))
    print("Cantidad de aprobados:", contar_aprobados(notas))
    
    # llamamos al histograma
    histograma(notas)


# Lista de prueba
notas = [85, 42, 73, 61, 55, 90, 38, 77, 95, 60]

# Ejecutamos el reporte
reporte(notas)  

