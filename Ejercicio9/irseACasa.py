import time 

horaActual = time.strftime("%H:%M:%S")

horaActualInt = int(horaActual.split(":")[0]) #esta line conviete la horas a enteros

if horaActualInt >= 19:
    print("Es la hora de irse")

else:
    horaRestante = 19 - horaActualInt
    minRestantes = (60- int(horaActual.split(":")[1])) % 60

    print(f"Quedan {horaRestante} horas y {minRestantes} para poder salir del trabajo")