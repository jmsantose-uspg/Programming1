def cifrar_mensaje(mensaje, desplazamiento):
    """Cifra un mensaje usando el cifrado César"""
    resultado = ""
    for carácter in mensaje:
        if carácter.isalpha():
            # Determinar si es mayúscula o minúscula
            es_mayuscula = carácter.isupper()
            # Convertir a minúscula para procesar
            carácter = carácter.lower()
            # Aplicar el desplazamiento
            código = ord(carácter) - ord('a')
            código = (código + desplazamiento) % 26
            carácter_cifrado = chr(código + ord('a'))
            # Restaurar mayúscula si es necesario
            if es_mayuscula:
                carácter_cifrado = carácter_cifrado.upper()
            resultado += carácter_cifrado
        else:
            # Mantener caracteres no alfabéticos
            resultado += carácter
    return resultado


def descifrar_mensaje(mensaje_cifrado, desplazamiento):
    """Descifra un mensaje usando el cifrado César"""
    # Para descifrar, usamos el desplazamiento negativo
    return cifrar_mensaje(mensaje_cifrado, -desplazamiento)


# BONUS: fuerza bruta (prueba todos los desplazamientos)
def fuerza_bruta(mensaje_cifrado):
    print("Probando todos los desplazamientos:\n")
    
    for i in range(26):
        intento = descifrar_mensaje(mensaje_cifrado, i)
        print("Desplazamiento", i, ":", intento)


# PRUEBAS
mensaje = "hola"
cifrado = cifrar_mensaje(mensaje, 3)

print("Mensaje original:", mensaje)
print("Mensaje cifrado:", cifrado)

descifrado = descifrar_mensaje(cifrado, 3)
print("Mensaje descifrado:", descifrado)

print("\n--- FUERZA BRUTA ---")
fuerza_bruta(cifrado)