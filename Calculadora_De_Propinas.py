# ========== CALCULADORA DE PROPINAS PARA RESTAURANTE ==========

def calcular_propina(subtotal, porcentaje):
    """
    Calcula el monto de propina basado en el subtotal y el porcentaje.
    Parámetros:
        - subtotal: monto base (sin propina ni impuestos)
        - porcentaje: porcentaje a aplicar (ej: 15 para 15%)
    Retorna: el monto de propina calculado
    """
    return subtotal * (porcentaje / 100)  # fórmula: subtotal × (porcentaje / 100)


def calcular_total(subtotal, propina):
    """
    Calcula el total final sumando el subtotal y la propina.
    Parámetros:
        - subtotal: monto base
        - propina: monto de propina a agregar
    Retorna: el total (subtotal + propina)
    """
    return subtotal + propina  # suma simple del subtotal y propina


def dividir_cuenta(total, personas):
    """
    Divide el total de la cuenta entre varias personas.
    Parámetros:
        - total: monto total a dividir
        - personas: cantidad de personas
    Retorna: el monto por persona o un mensaje de error
    """
    # validar que el número de personas sea válido
    if personas <= 0:
        return "Error: la cantidad de personas debe ser mayor que 0."
    
    # dividir el total entre el número de personas
    return total / personas


def aplicar_descuento(subtotal, descuento_pct):
    """
    Aplica un descuento porcentual al subtotal.
    Parámetros:
        - subtotal: monto original
        - descuento_pct: porcentaje de descuento (ej: 10 para 10%)
    Retorna: el nuevo subtotal después de aplicar el descuento
    """
    # calcular el monto del descuento
    descuento = subtotal * (descuento_pct / 100)  # descuento = subtotal × (porcentaje / 100)
    # restar el descuento del subtotal original
    nuevo_subtotal = subtotal - descuento  # nuevo subtotal = subtotal - descuento
    return nuevo_subtotal


def mostrar_menu():
    """
    Muestra el menú principal con las opciones disponibles.
    """
    print("\n===== MENÚ DEL RESTAURANTE =====")
    print("1. Calcular propina")
    print("2. Dividir la cuenta entre personas")
    print("3. Aplicar descuento + propina")
    print("4. Salir")
    print("5. Resumen de operaciones")


def main():
    """
    Función principal que ejecuta el programa en un bucle interactivo.
    Maneja el menú, recibe opciones del usuario y realiza cálculos.
    """
    # crear una lista para guardar el historial de operaciones
    historial = []

    # bucle infinito hasta que el usuario seleccione salir
    while True:
        # mostrar el menú de opciones
        mostrar_menu()
        # recibir la opción del usuario
        opcion = input("Seleccione una opción: ")

        # ========== OPCIÓN 1: Calcular propina ==========
        if opcion == "1":
            try:  # intentar ejecutar el código (capturar posibles errores)
                # solicitar el subtotal al usuario
                subtotal = float(input("Ingrese el subtotal: Q"))
                # mostrar porcentajes sugeridos
                print("Porcentajes sugeridos: 10%, 15%, 20%")
                # solicitar el porcentaje de propina
                porcentaje = float(input("Ingrese el porcentaje de propina: "))

                # calcular la propina usando la función
                propina = calcular_propina(subtotal, porcentaje)
                # calcular el total (subtotal + propina)
                total = calcular_total(subtotal, propina)

                # mostrar los resultados redondeados a 2 decimales
                print("Propina: Q", round(propina, 2))
                print("Total a pagar: Q", round(total, 2))

                # agregar esta operación al historial
                historial.append(
                    f"Opción 1 -> Subtotal: Q{subtotal}, Propina: {porcentaje}%, "
                    f"Monto propina: Q{round(propina, 2)}, Total: Q{round(total, 2)}"
                )

            except ValueError:  # si el usuario ingresa algo que no es un número
                print("Error: debe ingresar un número válido.")

        # ========== OPCIÓN 2: Dividir la cuenta ==========
        elif opcion == "2":
            try:  # intentar ejecutar el código (capturar posibles errores)
                # solicitar el total de la cuenta
                total = float(input("Ingrese el total de la cuenta: Q"))
                # solicitar el número de personas
                personas = int(input("¿Entre cuántas personas se divide?: "))

                # calcular cuánto debe pagar cada persona
                resultado = dividir_cuenta(total, personas)

                # verificar si el resultado es un error (es una cadena de texto)
                if type(resultado) == str:
                    # mostrar el mensaje de error
                    print(resultado)
                else:
                    # mostrar el monto por persona redondeado a 2 decimales
                    print("Cada persona debe pagar: Q", round(resultado, 2))
                    # agregar esta operación al historial
                    historial.append(
                        f"Opción 2 -> Total: Q{total}, Personas: {personas}, "
                        f"Pago por persona: Q{round(resultado, 2)}"
                    )

            except ValueError:  # si el usuario ingresa valores no numéricos
                print("Error: debe ingresar valores numéricos válidos.")

        # ========== OPCIÓN 3: Aplicar descuento y propina ==========
        elif opcion == "3":
            try:  # intentar ejecutar el código (capturar posibles errores)
                # solicitar el subtotal original
                subtotal = float(input("Ingrese el subtotal: Q"))
                # solicitar el porcentaje de descuento
                descuento_pct = float(input("Ingrese el porcentaje de descuento: "))
                # solicitar el porcentaje de propina
                porcentaje_propina = float(input("Ingrese el porcentaje de propina: "))

                # aplicar el descuento al subtotal
                nuevo_subtotal = aplicar_descuento(subtotal, descuento_pct)
                # calcular la propina sobre el nuevo subtotal (con descuento)
                propina = calcular_propina(nuevo_subtotal, porcentaje_propina)
                # calcular el total final (nuevo subtotal + propina)
                total = calcular_total(nuevo_subtotal, propina)

                # mostrar los resultados del proceso
                print("Subtotal con descuento: Q", round(nuevo_subtotal, 2))
                print("Propina: Q", round(propina, 2))
                print("Total final a pagar: Q", round(total, 2))

                # agregar esta operación al historial
                historial.append(
                    f"Opción 3 -> Subtotal: Q{subtotal}, Descuento: {descuento_pct}%, "
                    f"Nuevo subtotal: Q{round(nuevo_subtotal, 2)}, Propina: {porcentaje_propina}%, "
                    f"Total final: Q{round(total, 2)}"
                )

            except ValueError:  # si el usuario ingresa algo que no es un número
                print("Error: debe ingresar un número válido.")

        # ========== OPCIÓN 4: Salir del programa ==========
        elif opcion == "4":
            print("Gracias por usar el sistema del restaurante. ¡Hasta luego!")
            break  # salir del bucle while y terminar el programa

        # ========== OPCIÓN 5: Ver historial de operaciones ==========
        elif opcion == "5":
            print("\n===== RESUMEN DE OPERACIONES =====")
            # verificar si hay operaciones en el historial
            if len(historial) == 0:
                # si no hay operaciones, mostrar mensaje
                print("No se han realizado operaciones todavía.")
            else:
                # si hay operaciones, mostrar cada una
                for operacion in historial:
                    print("-", operacion)

        # ========== OPCIÓN NO VÁLIDA ==========
        else:
            print("Opción no válida. Intente de nuevo.")


# ========== EJECUTAR EL PROGRAMA ==========

# llamar a la función main para iniciar el programa
main()