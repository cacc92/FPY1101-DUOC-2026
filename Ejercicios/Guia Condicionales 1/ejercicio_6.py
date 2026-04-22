# Variables
promedio = float(input("Ingrese su promedio: ").strip())
asistencia = float(input("Ingrese porcetaje de asistencia: ").strip())

# Condicionales
if promedio >= 5.5 and asistencia >= 85.0:
    print("El alumno queda eximido del examen final.")
else:
    print("El alumno no queda eximido del examen final.")