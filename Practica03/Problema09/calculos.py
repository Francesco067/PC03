import operaciones

def main():
    # Pruebas de las funciones del módulo operaciones
    print("Suma de 5 + 3:", operaciones.suma(5, 3))
    print("Resta de 5 - 3:", operaciones.resta(5, 3))
    print("Producto de 5 * 3:", operaciones.producto(5, 3))
    print("División de 5 / 3:", operaciones.division(5, 3))

    # Pruebas con errores
    print("Suma de '5' + 3:", operaciones.suma('5', 3))
    print("División de 5 / 0:", operaciones.division(5, 0))
    print("Producto de 'cinco' * 3:", operaciones.producto('cinco', 3))

if __name__ == "__main__":
    main()