from functools import reduce

def suma(a, b):
    return a+b
def sacarPares(num):
    return num % 2 == 1
def sumaImpares(lista):
    listaClasificada = filter(sacarPares, lista)
    valoResultante = reduce(suma, listaClasificada)
    print(f"El valor resultante es: {valoResultante}") 

listita =[1,2,3,4,5]
sumaImpares(listita)