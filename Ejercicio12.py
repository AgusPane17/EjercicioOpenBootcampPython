paises = input("Ingrese nombre de paises separandolos por comas: ")
listaPaises = sorted(set(paises.split(",")))
print(f"su lista es :{listaPaises}")