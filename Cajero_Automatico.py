def calcular_billetes(monto):
    # Validar que el monto sea múltiplo de 5 (requerimiento del cajero)
    if monto % 5 != 0:  # si el monto no es divisible entre 5
        print("El monto debe ser múltiplo de 5.")  # mostrar mensaje de error
        return None  # retornar None si la validación falla
    
    # Crear un diccionario vacío para almacenar la cantidad de cada billete
    billetes = {}
    
    # Iterar sobre cada denominación de billete disponible (de mayor a menor)
    for valor in [200, 100, 50, 20, 10, 5]:  # denominaciones en quetzales (Q200, Q100, Q50, Q20, Q10, Q5)
        # Calcular cuántos billetes de este valor se pueden usar
        billetes[valor] = monto // valor  # división entera para obtener la cantidad de billetes
        # Actualizar el monto restante después de usar billetes de esta denominación
        monto %= valor  # operación módulo para obtener el residuo
    
    # Retornar el diccionario con la cantidad de billetes de cada denominación
    return billetes


    