def calcular_billetes(monto):
    if monto % 5 != 0:  # ahora validamos múltiplos de 5
        print("El monto debe ser múltiplo de 5.")
        return None
    
    billetes = {}
    for valor in [200, 100, 50, 20, 10, 5]:  # agregamos Q10 y Q5
        billetes[valor] = monto // valor
        monto %= valor
    
    return billetes


    