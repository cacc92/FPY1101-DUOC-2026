# float() -> Me permite formatear un tipo de dato
# string a float(decimal)
# strip -> Me permite sacar los espacios vacios del
# inicio y fin de un texto
nota = float(input("Ingresa tu nota: ").strip())

if nota >= 4.0:
  print("El alumno se encuentra aprobado")
else:
  print("El alumno se encuentra reprobado")