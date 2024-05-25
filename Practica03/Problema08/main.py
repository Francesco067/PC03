import modulo_numeros

def main():
    lista_numeros = modulo_numeros.generar_numeros_aleatorios()
    print("Lista generada:")
    modulo_numeros.mostrar_lista(lista_numeros)
    lista_ordenada = modulo_numeros.ordenar_lista(lista_numeros)
    print("Lista ordenada:")
    modulo_numeros.mostrar_lista(lista_ordenada)

if __name__ == "__main__":
    main()