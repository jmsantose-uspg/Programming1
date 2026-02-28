import random
numero_secreto = random.randint(1, 100)  # corregido nombre variable
intentos = 0
max_intentos = 7
while intentos < max_intentos:
    intento = int(input("Adivina el número entre 1 y 100: "))
    intentos += 1
    if intento < numero_secreto:
        print("Demasiado bajo. Intenta de nuevo.")
    elif intento > numero_secreto:
        print("Demasiado alto. Intenta de nuevo.")
    else:
        print(f"¡Felicidades! Has adivinado el número en {intentos} intentos.")
        break
else:
    # Este bloque se ejecuta si el while termina sin break
    print(f"Lo siento, agotaste tus {max_intentos} intentos. El número era {numero_secreto}.")