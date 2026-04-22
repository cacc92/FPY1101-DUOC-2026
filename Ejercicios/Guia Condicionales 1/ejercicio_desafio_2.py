# Variables
usuario = input("Ingrese su nombre de usuario: ").strip()
contrasena = input("Ingrese su contraseña: ").strip()

if usuario == "admin" and contrasena == "1234":
    print("¡Bienvenido, admin!")
else:
    print("Usuario o contraseña incorrectos.")