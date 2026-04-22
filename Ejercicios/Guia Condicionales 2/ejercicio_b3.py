# Variables
nota = float(input("Ingrese la nota del estudiante: ").strip())

# Validacion del rango de la nota
if nota >= 1.0 and nota <= 7.0:
    if nota < 4.0:
        print("Categoria: Insuficiente")
        print("El alumno ha reprobado.")
    elif nota >= 4.0 and nota < 5.0:
        print("Categoria: Suficiente")
        print("El alumno ha aprobado.")
    elif nota >= 5.0 and nota < 6.0:
        print("Categoria: Bueno")
        print("El alumno ha realizado un buen trabajo.")
    else:
        print("Categoria: Excelente")
        print("El alumno ha realizado un excelente trabajo.")
else:
    print("La nota ingresada no es válida. Debe estar entre 1.0 y 7.0.")