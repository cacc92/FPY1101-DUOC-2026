valor_propiedad = int(input("Ingrese en UF cuanto vale su propiedad: "))
valor_vehiculo = int(input("Ingrese su valor de su vehiculo: "))

if valor_propiedad >= 10000 or valor_vehiculo >= 45000000:
  print("Eres una persona de altos ingresos")
else:
  print("Eres una persona de ingresos medios")