# Variables
numero_1 = int(input("Ingrese el primer número: ").strip())
numero_2 = int(input("Ingrese el segundo número: ").strip())

# Condicional
if numero_1 > numero_2:
    print(f"El número 1 es mayor que el número 2.")
    print(f"El número 1 es: {numero_1}")
elif numero_2 > numero_1:
    print(f"El número 2 es mayor que el número 1.")
    print(f"El número 2 es: {numero_2}")
else:
    print("Ambos números son iguales.")