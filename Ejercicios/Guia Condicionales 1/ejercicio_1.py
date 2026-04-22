# Declaracion de variables
nombre = input("Ingresa el nombre de la persona: ")
edad = int(input("Ingresa la edad de la persona: ").strip())

# Condicionales
if edad >= 18:
  print(f"{nombre} es mayor de edad.")
else:
  print(f"{nombre} es menor de edad.")