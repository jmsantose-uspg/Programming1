# Función para calcular la propina
def calcular_propina(subtotal, porcentaje):
    return subtotal * (porcentaje / 100)


# Función para calcular el total
def calcular_total(subtotal, propina):
    return subtotal + propina


# Función para dividir la cuenta
def dividir_cuenta(total, personas):
    if personas <= 0:
        return "Error: la cantidad de personas debe ser mayor que 0."
    return total / personas


# Función para aplicar descuento
def aplicar_descuento(subtotal, descuento_pct):
    descuento = subtotal * (descuento_pct / 100)
    nuevo_subtotal = subtotal - descuento
    return nuevo_subtotal


# Función para mostrar el menú
def mostrar_menu():
    print("\n===== MENÚ DEL RESTAURANTE =====")
    print("1. Calcular propina")
    print("2. Dividir la cuenta entre personas")
    print("3. Aplicar descuento + propina")
    print("4. Salir")
    print("5. Resumen de operaciones")


# Función principal
def main():
    historial = []

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            try:
                subtotal = float(input("Ingrese el subtotal: Q"))
                print("Porcentajes sugeridos: 10%, 15%, 20%")
                porcentaje = float(input("Ingrese el porcentaje de propina: "))

                propina = calcular_propina(subtotal, porcentaje)
                total = calcular_total(subtotal, propina)

                print("Propina: Q", round(propina, 2))
                print("Total a pagar: Q", round(total, 2))

                historial.append(
                    f"Opción 1 -> Subtotal: Q{subtotal}, Propina: {porcentaje}%, "
                    f"Monto propina: Q{round(propina, 2)}, Total: Q{round(total, 2)}"
                )

            except ValueError:
                print("Error: debe ingresar un número válido.")

        elif opcion == "2":
            try:
                total = float(input("Ingrese el total de la cuenta: Q"))
                personas = int(input("¿Entre cuántas personas se divide?: "))

                resultado = dividir_cuenta(total, personas)

                if type(resultado) == str:
                    print(resultado)
                else:
                    print("Cada persona debe pagar: Q", round(resultado, 2))
                    historial.append(
                        f"Opción 2 -> Total: Q{total}, Personas: {personas}, "
                        f"Pago por persona: Q{round(resultado, 2)}"
                    )

            except ValueError:
                print("Error: debe ingresar valores numéricos válidos.")

        elif opcion == "3":
            try:
                subtotal = float(input("Ingrese el subtotal: Q"))
                descuento_pct = float(input("Ingrese el porcentaje de descuento: "))
                porcentaje_propina = float(input("Ingrese el porcentaje de propina: "))

                nuevo_subtotal = aplicar_descuento(subtotal, descuento_pct)
                propina = calcular_propina(nuevo_subtotal, porcentaje_propina)
                total = calcular_total(nuevo_subtotal, propina)

                print("Subtotal con descuento: Q", round(nuevo_subtotal, 2))
                print("Propina: Q", round(propina, 2))
                print("Total final a pagar: Q", round(total, 2))

                historial.append(
                    f"Opción 3 -> Subtotal: Q{subtotal}, Descuento: {descuento_pct}%, "
                    f"Nuevo subtotal: Q{round(nuevo_subtotal, 2)}, Propina: {porcentaje_propina}%, "
                    f"Total final: Q{round(total, 2)}"
                )

            except ValueError:
                print("Error: debe ingresar un número válido.")

        elif opcion == "4":
            print("Gracias por usar el sistema del restaurante. ¡Hasta luego!")
            break

        elif opcion == "5":
            print("\n===== RESUMEN DE OPERACIONES =====")
            if len(historial) == 0:
                print("No se han realizado operaciones todavía.")
            else:
                for operacion in historial:
                    print("-", operacion)

        else:
            print("Opción no válida. Intente de nuevo.")


# Ejecutar el programa
main()