def obtener_fraccion():
    while True:
        try:
            fraccion = input("Ingrese una fracción en el formato X/Y: ")
            x, y = fraccion.split('/')
            x = int(x)
            y = int(y)
            if y == 0:
                raise ZeroDivisionError
            if x > y:
                raise ValueError("El numerador no puede ser mayor que el denominador.")
            return x, y
        except ValueError:
            print("Error: asegúrese de ingresar numeros enteros y separados por / .")
        except ZeroDivisionError:
            print("Error: el denominador no puede ser cero.")

def calcular_porcentaje(x, y):
    porcentaje = (x / y) * 100  
    if porcentaje < 1:
        return "E"
    elif porcentaje > 99:
        return "F"
    else:
        return f"{round(porcentaje)}%"

def main():
    while True:
        x, y = obtener_fraccion()
        resultado = calcular_porcentaje(x, y)
        print(f"El nivel de combustible es: {resultado}")
        break


if __name__ == "__main__":
    main()