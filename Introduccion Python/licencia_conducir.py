edad = int(input("Ingrese su edad: "))
respuesta_licencia = input("Usted tiene licencia \n1)- SI \n2)- NO")
tiene_licencia = False

if respuesta_licencia.lower() == "si":
  tiene_licencia = True
elif respuesta_licencia.lower() == "no":
  tiene_licencia = False
else:
  print("La opcion ingresada no es válida")

if edad >= 18 and edad<= 65 and tiene_licencia:
  print("Usted puede manejar.")
else:
  print("No puede manejar")
