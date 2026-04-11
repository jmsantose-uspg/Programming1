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


def validar_y_diagnosticar(password):
    """
    Valida una contraseña y proporciona un diagnóstico detallado de los requisitos.
    Muestra qué requisitos CUMPLE y cuáles NO CUMPLE.
    Retorna: True si es válida, False si no lo es
    """
    
    # Definir caracteres especiales permitidos
    especiales = "!@#$%"  # caracteres especiales permitidos
    
    # Crear un diccionario para almacenar el resultado de cada validación
    diagnostico = {
        "longitud_minima": len(password) >= 8,  # mínimo 8 caracteres
        "tiene_mayuscula": any(c.isupper() for c in password),  # al menos una mayúscula
        "tiene_digito": any(c.isdigit() for c in password),  # al menos un dígito (0-9)
        "tiene_especial": any(c in especiales for c in password)  # al menos un carácter especial
    }
    
    # Mostrar encabezado del diagnóstico
    print("\n" + "="*50)
    print("DIAGNÓSTICO DE CONTRASEÑA")
    print("="*50)
    print(f"Contraseña: {len(password)} caracteres")
    print("-"*50)
    
    # Verificar requisito 1: Longitud mínima
    print(f"\n✓ LONGITUD MÍNIMA (8 caracteres):" if diagnostico["longitud_minima"] else f"\n✗ LONGITUD MÍNIMA (8 caracteres):")
    print(f"  La contraseña tiene {len(password)} caracteres.")
    if not diagnostico["longitud_minima"]:
        print(f"  Falta: {8 - len(password)} caracteres más.")
    
    # Verificar requisito 2: Mayúscula
    print(f"\n✓ LETRA MAYÚSCULA:" if diagnostico["tiene_mayuscula"] else f"\n✗ LETRA MAYÚSCULA:")
    if diagnostico["tiene_mayuscula"]:
        mayusculas = [c for c in password if c.isupper()]
        print(f"  ✓ Contiene: {mayusculas}")
    else:
        print(f"  ✗ No contiene ninguna letra mayúscula.")
    
    # Verificar requisito 3: Dígito
    print(f"\n✓ DÍGITO (0-9):" if diagnostico["tiene_digito"] else f"\n✗ DÍGITO (0-9):")
    if diagnostico["tiene_digito"]:
        digitos = [c for c in password if c.isdigit()]
        print(f"  ✓ Contiene: {digitos}")
    else:
        print(f"  ✗ No contiene ningún dígito.")
    
    # Verificar requisito 4: Carácter especial
    print(f"\n✓ CARÁCTER ESPECIAL ({especiales}):" if diagnostico["tiene_especial"] else f"\n✗ CARÁCTER ESPECIAL ({especiales}):")
    if diagnostico["tiene_especial"]:
        especiales_encontrados = [c for c in password if c in especiales]
        print(f"  ✓ Contiene: {especiales_encontrados}")
    else:
        print(f"  ✗ No contiene caracteres especiales.")
        print(f"  Caracteres permitidos: {especiales}")
    
    # Mostrar resultado final
    print("\n" + "="*50)
    todos_validos = all(diagnostico.values())  # verificar si todos los requisitos se cumplen
    
    if todos_validos:
        print("✓ CONTRASEÑA VÁLIDA - CUMPLE TODOS LOS REQUISITOS")
    else:
        requisitos_cumplidos = sum(diagnostico.values())  # contar cuántos se cumplen
        requisitos_totales = len(diagnostico)
        print(f"✗ CONTRASEÑA INVÁLIDA - {requisitos_cumplidos}/{requisitos_totales} requisitos cumplidos")
    
    print("="*50 + "\n")
    
    # Retornar True si es válida, False si no
    return todos_validos


# ========== EJEMPLOS DE USO ==========

print("\n" + "="*50)
print("PRUEBAS DEL VALIDADOR DE CONTRASEÑAS")
print("="*50 + "\n")

# Ejemplo 1: Contraseña válida
print("--- Ejemplo 1: Contraseña VÁLIDA ---")
validar_y_diagnosticar("Segura123!")

# Ejemplo 2: Contraseña sin mayúscula
print("--- Ejemplo 2: Contraseña sin MAYÚSCULA ---")
validar_y_diagnosticar("segura123!")

# Ejemplo 3: Contraseña sin dígito
print("--- Ejemplo 3: Contraseña sin DÍGITO ---")
validar_y_diagnosticar("SeguraContra!")

# Ejemplo 4: Contraseña muy corta
print("--- Ejemplo 4: Contraseña CORTA ---")
validar_y_diagnosticar("Seg1!")

# Ejemplo 5: Contraseña sin caracteres especiales
print("--- Ejemplo 5: Contraseña sin ESPECIALES ---")
validar_y_diagnosticar("Segura123abc")
