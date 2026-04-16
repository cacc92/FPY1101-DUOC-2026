estudiante = input("Eres estudiante si/no: ").lower().strip() 
edad = int(input("Dame tu edad: ").strip())

if estudiante == "si" and edad < 18:
  print("Tienes descuento")
else:
  print("No tienes descuento")