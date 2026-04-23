# Definición de variables

# Toda variable que sea un monto de dinero debe estar como float
ingresos = float(input("Ingrese sus ingresos mensuales: ").strip())
cuota = float(input("Ingrese el monto de la cuota mensual: ").strip())
deudas = float(input("Ingrese el monto mensual pagado por deudas: ").strip())
tipo_contrato = int(input("Ingrese el tipo de contrato\n1)-Dependiente\n2)-Independiente\n"))
historial = int(input("Ingrese el historial crediticio\n1)-Excelente\n2)-Bueno\n3)-Malo\n"))

# Acumulador donde voy a ir sumando cada uno de los puntajes.
score = 0

# Ingresos vs Cuota
if ingresos >= cuota*3:
    print("Los ingresos son superiores a 3 veces la cuota")
    score = score + 30
elif ingresos >= cuota*2 and ingresos < cuota*3:
    print("Los ingresos estan entre 2 y 3 veces la cuota")
    score = score + 15
else:
    print("No se asigna puntaje por concepto cuota vs ingreso")
    
# Concepto Historial Crediticio
if historial == 1:
    print("El historial crediticio es excelente")
    score = score + 25
elif historial == 2:
    print("El historial crediticio es bueno")
    score = score + 10
elif historial == 3:
    print("El historial crediticio es malo")
    score = score - 20
else:
    print("No se ha ingresado la opción correcta, no se sumará puntaje por concepto historial crediticio")

# Concepto Tipo de Contrato
if tipo_contrato == 1:
    print("El tipo de contrato es dependiente")
    score = score + 20
elif tipo_contrato == 2:
    print("El tipo de contrato es independiente")
    score = score + 5
else:
    print("No se ha ingresado la opción correcta, no se sumará puntaje por concepto tipo de contrato")

# Concepto Deudas
if deudas == 0:
    print("No tiene deudas")
    score = score + 10
elif deudas > ingresos * 0.5:
    print("El monto de las deudas es superior al 50% de los ingresos")
    score = score - 15
else:
    print("El monto de las deudas es inferior al 50% de los ingresos")
    
    
# Resultado final
print("El puntaje total es: ", score)
if score >= 60:
    print("El cliente es aprobado para el crédito")
elif score >= 40 and score < 60:
    print("El cliente se encuentra en revisión")
else:
    print("El cliente se encuentra rechazado para el crédito")