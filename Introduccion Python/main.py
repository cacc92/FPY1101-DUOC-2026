# Entrada de texto, por teclado
# nombre = input("Hola, ¿Cúal es tu nombre? ")
# apellido = input("¿Cúal es tu apellido? ")

# Salida de texto por pantalla
# print(f"Hola {nombre} {apellido}")

"""
  ----------------------Tipos de Datos ---------------
  ----- Pseudo Código ------  = ------- Python -------
  Cadena ("HOLA MUNDO")      -> str ("HOLA MUNDO")
  Entero (1)                 -> int (1)
  Logico (Verdadero o Falso) -> boolean (True o False)
  Real (1.0)                 -> float (1.0)
"""

edad : int = 20 # Var se tipo entero o int

# Definir porcentaje_descuento como Real
porcentaje_descuento : float = 0.20 # La variable es un real o float en python

texto : str = 'Esto es un texto'

bandera : bool = True


nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = int(input("Ingrese su edad: "))

edad = edad + 1
nombre_completo = nombre + " " +  apellido
print(f"La edad de {nombre_completo} es : {edad}")