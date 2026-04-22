# Variables
entrada = input("¿Usted posee entrada? (si/no): ").strip()
edad = int(input("Ingrese su edad: ").strip())

# Trasnformacion
entrada = entrada.lower()

# Condiciones
if entrada == "si" and edad >= 18:
    print("Puedes entrar al concierto.")
else:
    print("No puedes entrar al concierto.")
