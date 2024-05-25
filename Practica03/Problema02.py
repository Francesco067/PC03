def obtener_calificaciones():
    while True:
        try:
            entrada = input("Ingrese una lista de calificaciones separadas por comas: ")
            calificaciones = entrada.split(',')
   
            calificaciones_int=[int(i) for i in calificaciones]
             
            return calificaciones_int
        
        except ValueError:
            print("Error: Asegúrese de ingresar solo números enteros separados por comas. Intente nuevamente.")

# Llamar a la función y mostrar las calificaciones
calificaciones = obtener_calificaciones()
print("Las calificaciones ingresadas son:", calificaciones)