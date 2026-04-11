def validar_password(password):
    especiales = "!@#$%"  # lista de caracteres especiales permitidos
    
    # Regla 1: mínimo 8 caracteres
    if len(password) < 8:
        return False
    
    # Regla 2: al menos una letra mayúscula
    if not any(c.isupper() for c in password):
        return False
    
    # Regla 3: al menos un dígito
    if not any(c.isdigit() for c in password):
        return False
    
    # Regla 4: al menos un carácter especial
    if not any(c in especiales for c in password):
        return False
# Si pasa todas las reglas
    return True
