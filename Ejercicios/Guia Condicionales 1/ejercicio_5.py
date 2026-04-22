# Variables
cupon = input("¿Usted posee un. cupón de descuento? (si/no): ").strip()
monto_compra = int(input("Ingrese el monto total de su compra: ").strip())

# Trasnformación
cupon = cupon.lower()

# Condicionales
if cupon == "si" or monto_compra >= 20000:
    print("Su despacho será gratuito.")
else:
    print("Debera cancelar el costo de despacho. ")