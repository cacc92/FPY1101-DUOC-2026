"""
  Este es el desarrollo de la guia 1.3.2 destinada pseudo codigo,
  sin embargo sera desarrollada para python
"""
# Paso 1
print("¡Comienza la carrera!")

# Paso 2
# lower() -> traspasamos todo el texto a minúscila
# strip() -> sacamos todos los espacios vacios al inicio y al final del texto
respuesta = input("¿Encuentras una valla? Responde con si/no: ").lower().strip()

if respuesta == "si":
  print("Salta la valla")
  # IF ANIDADO
  # Cambio el valor de respuesta por la nueva entrada por teclado
  respuesta = input("¿Encuentras el tunel? Responde con si/no: ").lower().strip()
  if respuesta == "si":
    print("Atraviesa el tunel")

    respuesta = input("Encuentras la laguna si/no: ").lower().strip()
    if respuesta == "si":
      print("Perdiste la carrera porque te fuiste por el camino equivocado")
    elif respuesta == "no":
      print("Ganaste la carrera porque llegaste a la meta")
    else:
      print("La opción ingresada no es válida")

  elif respuesta == "no":
    print("Continua corriendo")
  else:
    print("La opción ingresada no es válida")
elif respuesta == "no":
  print("Continua corriendo")
else:
  print("La opción ingresada no es válida")

