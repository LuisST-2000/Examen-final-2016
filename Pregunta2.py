import random

n = int(input("Ingrese cuantos numeros aleatorios desea obtener: "))

def listaAleatorios(n):
    lista = []
    for i in range(n):
        lista.insert(i, random.randrange(0, 1000))
    return lista
aleatorios = listaAleatorios(n)
print(aleatorios)


