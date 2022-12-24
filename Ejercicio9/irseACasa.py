import time 

horaActual = time.strftime("%H:%M:%S")

horaActualInt = int(horaActual.split(":")[0]) #esta line conviete la horas a enteros
horaActualInt = 5
if horaActualInt == 19:
    print("Es la hora de irse")

elif ((horaActualInt> 8) & (horaActualInt < 19)):
        horaRestante = 19 - horaActualInt
        print("xd")
        minRestantes = (60- int(horaActual.split(":")[1])) % 60

        print(f"Quedan {horaRestante} horas y {minRestantes} para poder salir del trabajo")
elif (horaActualInt>19):
        print(f"Faltan {(24-horaActualInt)+8} hs para tu siguiente jornada laborar a las 8")

else:
    print(f"Te quedan {8-horaActualInt} horas para tu proxima jornada")
