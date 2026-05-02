class Estudiante:
    def __init__(self, nombre, carnet, carrera):
        self.nombre = nombre
        self.carnet = carnet
        self.carrera = carrera
        self.notas = []

    def agregar_nota(self, nota):
        self.notas.append(nota)

    def promedio(self):
        if self.notas == []:
            return 0
        else:
            return sum(self.notas) / len(self.notas)

    def aprobado(self):
        if self.promedio() >= 61:
            return True
        else:
            return False


estudiante1 = Estudiante("José", "2025001", "Sistemas")

estudiante1.agregar_nota(70)
estudiante1.agregar_nota(80)
estudiante1.agregar_nota(50)

print("Nombre:", estudiante1.nombre)
print("Carnet:", estudiante1.carnet)
print("Carrera:", estudiante1.carrera)
print("Notas:", estudiante1.notas)
print("Promedio:", round(estudiante1.promedio(), 2))
print("Aprobado:", estudiante1.aprobado())
