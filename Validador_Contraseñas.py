# ========== VALIDADOR DE CONTRASEÑAS ==========
# Este programa valida contraseñas según criticidad de seguridad
# Requisitos:
#   1. Mínimo 8 caracteres
#   2. Al menos una letra mayúscula
#   3. Al menos un dígito (0-9)
#   4. Al menos un carácter especial: !@#$%


def tiene_mayuscula(texto):
    """
    Verifica si una cadena contiene al menos una letra mayúscula.
    Parámetro: texto - cadena de caracteres a verificar
    Retorna: True si contiene mayúscula, False si no
    """
    # iterar sobre cada carácter en el texto
    for c in texto:
        # verificar si el carácter es una letra mayúscula
        if c.isupper():  # isupper() retorna True si el carácter es mayúscula
            return True  # encontramos una mayúscula, retornar True
    
    # si no encontramos ninguna mayúscula en el bucle
    return False


def tiene_digito(texto):
    """
    Verifica si una cadena contiene al menos un dígito (número 0-9).
    Parámetro: texto - cadena de caracteres a verificar
    Retorna: True si contiene dígito, False si no
    """
    # iterar sobre cada carácter en el texto
    for c in texto:
        # verificar si el carácter es un número
        if c.isdigit():  # isdigit() retorna True si el carácter es un dígito
            return True  # encontramos un dígito, retornar True
    
    # si no encontramos ningún dígito en el bucle
    return False


def tiene_especial(texto):
    """
    Verifica si una cadena contiene al menos un carácter especial permitido.
    Parámetro: texto - cadena de caracteres a verificar
    Retorna: True si contiene carácter especial, False si no
    """
    # definir cuáles son los caracteres especiales permitidos
    especiales = "!@#$%"  # caracteres especiales válidos: ! @ # $ %
    
    # iterar sobre cada carácter en el texto
    for c in texto:
        # verificar si el carácter actual está en la lista de especiales
        if c in especiales:  # verifica si c es uno de estos: ! @ # $ %
            return True  # encontramos un carácter especial, retornar True
    
    # si no encontramos ningún especial en el bucle
    return False


def longitud_valida(texto):
    """
    Verifica si una cadena tiene la longitud mínima requerida (8 caracteres).
    Parámetro: texto - cadena de caracteres a verificar
    Retorna: True si la longitud es >= 8, False si es menor
    """
    # len() retorna la cantidad de caracteres en la cadena
    # verificar si la longitud es mayor o igual a 8
    return len(texto) >= 8  # retorna True si cumple, False si no


def validar_password(password):
    """
    Valida si una contraseña cumple TODOS los requisitos de seguridad.
    Retorna: True si es válida, False si algo falta
    """
    # verificar que TODOS los requisitos se cumplan usando 'and'
    # validar longitud AND mayúscula AND dígito AND especial
    if longitud_valida(password) and tiene_mayuscula(password) and tiene_digito(password) and tiene_especial(password):
        return True  # si cumple todo, retornar True
    
    # si no cumple alguno de los requisitos
    return False


def diagnosticar_password(password):
    """
    Analiza una contraseña y muestra un diagnóstico detallado.
    Muestra con ✔ los requisitos que cumple y con ✘ los que faltan.
    Parámetro: password - contraseña a analizar
    """
    print("\n" + "="*50)
    print("DIAGNÓSTICO DE CONTRASEÑA")
    print("="*50)
    
    # REQUISITO 1: Verificar longitud mínima de 8 caracteres
    if longitud_valida(password):
        print("✔ Tiene al menos 8 caracteres")  # ✔ indica que cumple
    else:
        # mostrar cuántos caracteres faltan
        caracteres_faltantes = 8 - len(password)
        print(f"✘ No tiene al menos 8 caracteres (Faltan {caracteres_faltantes})")  # ✘ indica que NO cumple

    # REQUISITO 2: Verificar que tenga al menos una mayúscula
    if tiene_mayuscula(password):
        print("✔ Tiene mayúscula")  # cumple este requisito
    else:
        print("✘ Le falta una mayúscula")  # NO cumple este requisito

    # REQUISITO 3: Verificar que tenga al menos un dígito (0-9)
    if tiene_digito(password):
        print("✔ Tiene dígito")  # cumple este requisito
    else:
        print("✘ Le falta un dígito")  # NO cumple este requisito

    # REQUISITO 4: Verificar que tenga al menos un carácter especial
    if tiene_especial(password):
        print("✔ Tiene carácter especial")  # cumple este requisito
    else:
        # listar los caracteres especiales permitidos
        print("✘ Le falta un carácter especial (!,@,#,$,%)")  # NO cumple este requisito
    
    print("="*50 + "\n")


# ========== PRUEBAS DEL PROGRAMA ==========

print("\n" + "="*50)
print("PRUEBAS DEL VALIDADOR DE CONTRASEÑAS")
print("="*50)

# Ejemplo 1: Contraseña válida
print("\n--- Ejemplo 1: Contraseña VÁLIDA ---")
clave1 = "Hola123!"
# mostrar el resultado de la validación (True = válida, False = inválida)
resultado1 = validar_password(clave1)
print(f"Contraseña: '{clave1}' -> Válida: {resultado1}")
# mostrar el diagnóstico detallado
diagnosticar_password(clave1)

# Ejemplo 2: Contraseña sin mayúscula
print("--- Ejemplo 2: Contraseña sin MAYÚSCULA ---")
clave2 = "hola123!"
resultado2 = validar_password(clave2)
print(f"Contraseña: '{clave2}' -> Válida: {resultado2}")
diagnosticar_password(clave2)

# Ejemplo 3: Contraseña sin dígito
print("--- Ejemplo 3: Contraseña sin DÍGITO ---")
clave3 = "Hola!"
resultado3 = validar_password(clave3)
print(f"Contraseña: '{clave3}' -> Válida: {resultado3}")
diagnosticar_password(clave3)

# Ejemplo 4: Contraseña muy corta
print("--- Ejemplo 4: Contraseña CORTA ---")
clave4 = "Ho1!"
resultado4 = validar_password(clave4)
print(f"Contraseña: '{clave4}' -> Válida: {resultado4}")
diagnosticar_password(clave4)

# Ejemplo 5: Contraseña sin caracteres especiales
print("--- Ejemplo 5: Contraseña sin ESPECIALES ---")
clave5 = "Hola1234"
resultado5 = validar_password(clave5)
print(f"Contraseña: '{clave5}' -> Válida: {resultado5}")
diagnosticar_password(clave5)