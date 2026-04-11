# ========== FUNCIONES DE ANÁLISIS DE CALIFICACIONES ==========

def promedio(notas):
    """
    Calcula el promedio (media aritmética) de las notas.
    Parámetro: notas - lista de números que representan calificaciones
    Retorna: el promedio de todas las notas
    """
    suma = 0  # variable para acumular la suma de todas las notas
    
    # recorremos cada nota en la lista y la sumamos
    for nota in notas:
        suma = suma + nota  # suma = suma + nota equivalente a suma += nota
    
    # calculamos el promedio dividiendo la suma entre la cantidad de notas
    return suma / len(notas)  # len(notas) retorna la cantidad de elementos


def mayor(notas):
    """
    Encuentra la nota más alta sin usar la función max().
    Parámetro: notas - lista de números
    Retorna: el valor más grande de la lista
    """
    # asumimos que la primera nota es la mayor
    mayor = notas[0]  # variable que guardará el valor más grande encontrado
    
    # comparamos cada nota con el valor máximo actual
    for nota in notas:
        if nota > mayor:  # si encontramos una nota más grande
            mayor = nota  # actualizamos el máximo
    
    return mayor  # retornamos la nota más alta


def menor(notas):
    """
    Encuentra la nota más baja sin usar la función min().
    Parámetro: notas - lista de números
    Retorna: el valor más pequeño de la lista
    """
    # asumimos que la primera nota es la menor
    menor = notas[0]  # variable que guardará el valor más pequeño encontrado
    
    # comparamos cada nota con el valor mínimo actual
    for nota in notas:
        if nota < menor:  # si encontramos una nota más pequeña
            menor = nota  # actualizamos el mínimo
    
    return menor  # retornamos la nota más baja


def contar_aprobados(notas, minimo=61):
    """
    Cuenta cuántas calificaciones están por encima del mínimo requerido.
    Parámetros:
        - notas: lista de números
        - minimo: umbral para considerar aprobado (por defecto 61)
    Retorna: cantidad de notas que cumplen con el mínimo
    """
    contador = 0  # inicializamos el contador de aprobados en 0
    
    # iteramos sobre cada nota
    for nota in notas:
        if nota >= minimo:  # si la nota es mayor o igual al mínimo requerido
            contador += 1  # incrementamos el contador (contador = contador + 1)
    
    return contador  # retornamos el total de aprobados


def histograma(notas):
    """
    Crea una representación visual de las notas usando asteriscos.
    Parámetro: notas - lista de números a visualizar
    """
    print("\nHistograma:")  # encabezado del histograma
    
    # para cada nota, creamos una fila con asteriscos proporcionales
    for nota in notas:
        # dividimos la nota entre 20 para no hacer demasiados asteriscos
        # ejemplo: nota 80 → 80 // 20 = 4 asteriscos
        estrellas = "*" * (nota // 20)  # creamos una cadena de asteriscos
        # mostramos la nota y su representación gráfica
        print(str(nota) + ": " + estrellas)


def reporte(notas):
    """
    Función principal que genera un reporte completo de análisis de calificaciones.
    Parámetro: notas - lista de calificaciones a analizar
    Muestra: promedio, nota máxima, nota mínima, aprobados e histograma
    """
    print("===== REPORTE DE NOTAS =====")  # título del reporte
    
    # mostramos la lista completa de notas
    print("Lista de notas:", notas)
    # calculamos y mostramos el promedio
    print("Promedio:", promedio(notas))
    # encontramos y mostramos la calificación más alta
    print("Nota más alta:", mayor(notas))
    # encontramos y mostramos la calificación más baja
    print("Nota más baja:", menor(notas))
    # contamos y mostramos cuántos estudiantes aprobaron
    print("Cantidad de aprobados:", contar_aprobados(notas))
    
    # llamamos a la función que genera el histograma visual
    histograma(notas)


# ========== EJECUCIÓN DEL PROGRAMA ==========

# creamos una lista de prueba con 10 calificaciones diferentes
notas = [85, 42, 73, 61, 55, 90, 38, 77, 95, 60]

# ejecutamos la función reporte para mostrar todo el análisis
reporte(notas)  

