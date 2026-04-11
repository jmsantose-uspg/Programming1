def tiene_mayuscula(texto):
    for c in texto:
        if c.isupper():
            return True
    return False


def tiene_digito(texto):
    for c in texto:
        if c.isdigit():
            return True
    return False


def tiene_especial(texto):
    especiales = "!@#$%"
    for c in texto:
        if c in especiales:
            return True
    return False


def longitud_valida(texto):
    return len(texto) >= 8


def validar_password(password):
    if longitud_valida(password) and tiene_mayuscula(password) and tiene_digito(password) and tiene_especial(password):
        return True
    return False


def diagnosticar_password(password):
    if longitud_valida(password):
        print("✔ Tiene al menos 8 caracteres")
    else:
        print("✘ No tiene al menos 8 caracteres")

    if tiene_mayuscula(password):
        print("✔ Tiene mayúscula")
    else:
        print("✘ Le falta una mayúscula")

    if tiene_digito(password):
        print("✔ Tiene dígito")
    else:
        print("✘ Le falta un dígito")

    if tiene_especial(password):
        print("✔ Tiene carácter especial")
    else:
        print("✘ Le falta un carácter especial (!,@,#,$,%)")

# Pruebas
clave = "Hola123!"
print(validar_password(clave))
diagnosticar_password(clave)