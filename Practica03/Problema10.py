import Problema04
import Problema03

def mostrar_menu():
    print("\nMenú de opciones:")
    print("1. Calcular el área de un círculo")
    print("2. Calcular el área de un rectángulo")
    print("3. Calcular el área de un cuadrado")
    print("4. Salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            radio = float(input("Ingrese el radio del círculo: "))
            area_circulo=(Problema03.CIRCULO(radio)).calcular_area()
          
            print(f"El área del circulo es: {area_circulo}")
        
        elif opcion == "2":
            largo = float(input("Ingrese el largo del rectángulo: "))
            ancho = float(input("Ingrese el ancho del rectángulo: "))
            rectangulo01=Problema04.Rectangulo(largo,ancho)
            area_rectangulo01 = rectangulo01.calcular_area()
            print(f"El área del rectángulo es: {area_rectangulo01}")
        
        elif opcion == "3":
            lado = float(input("Ingrese el lado del cuadrado: "))
            areadelcuadrado=lado**2
            print(f"El área del cuadrado es: {areadelcuadrado}")
        
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        
        else:
            print("Opción no válida. Por favor, intente nuevamente.")

if __name__ == "__main__":
    main()