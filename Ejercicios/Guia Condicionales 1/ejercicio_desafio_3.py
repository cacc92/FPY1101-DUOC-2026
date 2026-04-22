# Variables
temperatura = float(input("Ingrese la temperatura en grados Celsius: ").strip())
lacteo = input("¿El producto es lácteo? (si/no): ").strip()

# Transformación
lacteo = lacteo.lower()

if temperatura >= 8.0 or lacteo == "si":
    print("El producto debe ser refrigerado.")
else:
    print("El producto no necesita refrigeración.")