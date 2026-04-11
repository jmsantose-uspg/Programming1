def validar_password(password):
    """
    Valida si una contraseña cumple con los requisitos de seguridad.
    Retorna True si es válida, False si no cumple algún requisito.
    """
    
    # Definir la lista de caracteres especiales permitidos para la validación
    especiales = "!@#$%"  # caracteres especiales que se aceptan: ! @ # $ %
    
    # ========== VALIDACIONES OBLIGATORIAS ==========
    
    # Regla 1: verificar que la contraseña tenga mínimo 8 caracteres
    if len(password) < 8:
        print("Error: La contraseña debe tener al menos 8 caracteres.")
        return False  # retorna False si no cumple esta regla
    
    # Regla 2: verificar que contenga al menos una letra mayúscula
    # isupper() verifica si el carácter es mayúscula, any() verifica si existe al menos uno
    if not any(c.isupper() for c in password):
        print("Error: La contraseña debe contener al menos una letra mayúscula.")
        return False  # retorna False si no hay mayúsculas
    
    # Regla 3: verificar que contenga al menos un dígito (número del 0 al 9)
    # isdigit() verifica si el carácter es un dígito, any() verifica si existe al menos uno
    if not any(c.isdigit() for c in password):
        print("Error: La contraseña debe contener al menos un dígito (0-9).")
        return False  # retorna False si no hay dígitos
    
    # Regla 4: verificar que contenga al menos un carácter especial de los permitidos
    # verifica si algún carácter está en la lista de especiales
    if not any(c in especiales for c in password):
        print(f"Error: La contraseña debe contener al menos un carácter especial: {especiales}")
        return False  # retorna False si no hay caracteres especiales
    
    # Si pasa todas las validaciones anteriores, la contraseña es válida
    print("✓ Contraseña válida. Cumple todos los requisitos de seguridad.")
    return True  # retorna True si cumple todos los requisitos
