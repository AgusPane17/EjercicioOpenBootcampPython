class Vehiculo:

    color = None
    ruedas = None
    puertas = None
    
    def __init__(self,color, ruedas, puertas):
        self.color = color
        self.puertas = puertas
        self.ruedas = ruedas

class auto(Vehiculo):

    Velocidad = None
    Cilindrada = None

    def __init__(self, color, ruedas, puertas, Velocidad, Cilindrada):
        super().__init__(color, ruedas, puertas)
        self.Velocidad = Velocidad
        self.Cilindrada = Cilindrada

miAuto = auto("Verde","4","4","160","1596cc")
print("La velocidad: ", miAuto.Velocidad)
print("La cilindrada: ", miAuto.Cilindrada)
print("El color: ", miAuto.color)
print("La cantidad de puertas es: ", miAuto.puertas)
print("La cantidad de ruedas es: ", miAuto.ruedas)
