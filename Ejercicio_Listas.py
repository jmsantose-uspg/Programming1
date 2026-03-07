tareas = []

while True:
    print("\n1. Agregar tarea")
    print("2. Ver tareas")
    print("3. Marcar tarea como completada")
    print("4. Eliminar tarea")
    print("5. Salir")

    opcion = input("Opción: ")

    if opcion == "1":
        tarea = input("Nueva tarea: ")
        tareas.append(["[ ]", tarea])
        print("✅ Agregada.")

    elif opcion == "2":
        print("\nTareas:")
        for i, t in enumerate(tareas, 1):
            print(i, t[0], t[1])

    elif opcion == "3":
        num = int(input("Número de tarea completada: "))
        tareas[num-1][0] = "[✔]"

    elif opcion == "4":
        num = int(input("Número de tarea a eliminar: "))
        tareas.pop(num-1)

    elif opcion == "5":
        print("Saliendo...")
        break

    else:
        print("Opción no válida")
