"""
  12345678-2 ANTONIA PUEBLA
  1234567-2 ANTONIA PUEBLA
  12345-2 ANTONIA PUEBLA
  1234-2 ANTONIA PUEBLA
  123-2 ANTONIA PUEBLA
  12-2 ANTONIA PUEBLA
  1-2 ANTONIA PUEBLA
"""

texto = "1-1 ANTONIA PUEBLA"
posicion = texto.find("-")
print(f"La posicion de la raya del rut es: {posicion}")

# Substring
parte_entera = texto[0:posicion]
digito_verificador = texto[posicion+1:posicion+2]
print(f"La parte entera del rut es: {parte_entera}")
print(f"El digito verificador es: {digito_verificador}")

largo = len(texto)
nombre = texto[posicion+2:largo].strip()
print(f"El nombre de la persona es: {nombre}")
