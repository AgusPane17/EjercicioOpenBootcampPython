class alumno:
    nombre = None
    nota = None

    def __init__(self, nombre: str, nota: int):
        self.nombre = nombre
        self.nota = nota
    
    def mostrarNombre(self):
        print("El nombre es:", self.nombre)

    def mostrarNota(self):
        if (self.nota >= 6):
            print("La nota es", self.nota ," esta aprobado")
        else:
            print("La nota es", self.nota,"estas desaprobado")

alumno1 = alumno("Manuel Martines", 5)
alumno1.mostrarNombre()
alumno1.mostrarNota()