import random

def generar_numeros_aleatorios():

    numeros = [random.randint(0, 100) for _ in range(20)]
    return numeros

def mostrar_lista(lista):
    print("Lista:", lista)

def ordenar_lista(lista):
    lista_ordenada = sorted(lista)
    return lista_ordenada