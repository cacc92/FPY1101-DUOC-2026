saludo = "HOLA!"
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")

# CONCATENACION

print(saludo + " " + nombre + " " + apellido)
print(f"{saludo} {nombre} {apellido}")

# REPETICION 
print(saludo*3)
print(f"{saludo*3}")

# INDICES

palabra = "12345678-2 ANTONIA PUEBLA"
print(f"{palabra}")

print(f"{palabra[0]}")
print(f"{palabra[1]}")
print(f"{palabra[2]}")
print(f"{palabra[3]}")
print(f"{palabra[-2]}")

# print(f"{palabra[0:10]}")
# Substring
parte_entera = palabra[0:8]
digito_verificado = palabra[9:10]
print(f"La parte entera del rut es: {parte_entera}")
print(f"El digito verificador del rut es: {digito_verificado}")

texto = "              HOLA MUNDO! "
print(f"{texto}")

# De esta manera quito los espacios iniciales y finales
texto_modificado = texto.strip()
print(f"{texto_modificado}")

# Transformación a minúscula
print("="*10)
print(f"texto original: {texto_modificado}")
texto_modificado = texto_modificado.lower()
print(f"texto modificado en minúscula: {texto_modificado}")

# Transformación a mayúscula
print("="*10)
print(f"texto original: {texto_modificado}")
texto_modificado = texto_modificado.upper()
print(f"texto modificado en mayúscula: {texto_modificado}")


# Replace
print("="*10)
print(f"texto original: {texto_modificado}")
texto_modificado = texto_modificado.replace("HOLA","BIENVENIDO")
print(f"texto remplazado: {texto_modificado}")

# Find
print("="*10)
print(f"texto original: {texto_modificado}")
posicion_busqueda = texto_modificado.find("BIENVENIDO")
print(f"La posicion de bienvenido es: {posicion_busqueda}")

# Largo del string
print("="*10)
print(f"texto original: {texto_modificado}")
largo = len(texto_modificado)
print(f"El largo del string es : {largo}")

# Split
print("="*10)
print(f"texto original: {texto_modificado}")
palabras = texto_modificado.split()
print(f"{palabras}")

"""
  12345678-2 ANTONIA PUEBLA
  1234567-2 ANTONIA PUEBLA
  12345-2 ANTONIA PUEBLA
  1234-2 ANTONIA PUEBLA
  123-2 ANTONIA PUEBLA
  12-2 ANTONIA PUEBLA
  1-2 ANTONIA PUEBLA

"""