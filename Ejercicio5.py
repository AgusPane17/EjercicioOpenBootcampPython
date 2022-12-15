

def funcionAñoBisiesto(año):
    añoBisiesto = 2020
    if (añoBisiesto > año):
        dif = (añoBisiesto - año )% 4
        if(dif == 0):
            print("Es un año Bisiesto")
        else:
            print("No es año bisiesto")
    elif (año > añoBisiesto ):
        dif = (año - añoBisiesto )% 4
        if(dif == 0):
            print("Es un año Bisiesto")
        else:
            print("No es año bisiesto")  
    elif (año == añoBisiesto):
        print("Es un año Bisiesto")
    else:
        print("No es año bisiesto")
        
funcionAñoBisiesto(2580)