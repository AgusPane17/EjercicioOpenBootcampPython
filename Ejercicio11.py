class Vehiculo:
    marca = ""
    modelo =""
    año = None
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año

# Creamos un objeto de la clase Vehículo
mi_vehiculo = Vehiculo("Ford", "Mustang", 1969)

# Importamos la librería pickle para poder serializar el objeto
import pickle

# Abrimos el archivo en modo escritura binaria
with open("vehiculo.pickle", "wb") as archivo:
    # Serializamos el objeto y lo escribimos en el archivo
    pickle.dump(mi_vehiculo, archivo)