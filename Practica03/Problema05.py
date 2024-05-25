class Alumno:
    def __init__(self, nombre, num_registro):
        self.nombre = nombre
        self.num_registro = num_registro
        self.edad = None
        self.notas = []

    def display(self):
        print("Nombre del estudiante:", self.nombre)
        print("Número de registro:", self.num_registro)
        if self.edad is not None:
            print("Edad:", self.edad)
        if self.notas:
            print("Notas:", self.notas)
        print()

    def setAge(self, edad):
        self.edad = edad

    def setNota(self, nota):
        self.notas.append(nota)


if __name__ == "__main__":
    alumno1 = Alumno("Juan Pérez", 123456)
    alumno1.setAge(25)
    alumno1.setNota(8)
    alumno1.setNota(9)
    
alumno1.display()