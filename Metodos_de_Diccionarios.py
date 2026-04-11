# Crear diccionario
alumno = {
    "nombre": "Jose Maria Santos",
    "edad": 33,
    "ciudad": "Guatemala",
    "lenguaje_favorito": "Español"
}

# update() → agregar varios datos
alumno.update({
    "universidad": "Universidad de San Pablo de Guatemala",
    "carrera": "Ingenieria en Tecnologia Industrial"
})

# Modificar edad
alumno["edad"] = 34

# Mostrar claves (.keys)
print("\nClaves:")
for k in alumno.keys():
    print(k)

# Mostrar valores (.values)
print("\nValores:")
for v in alumno.values():
    print(v)

# Mostrar pares (.items)
print("\nDatos del alumno:")
for k, v in alumno.items():
    print(k, ":", v)

# Verificar existencia
print("\n¿Existe email?", "email" in alumno)

# Obtener dato seguro (.get)
print("Teléfono:", alumno.get("telefono", "No disponible"))

# Eliminar dato (.pop)
eliminado = alumno.pop("ciudad")
print("\nSe eliminó:", eliminado)
