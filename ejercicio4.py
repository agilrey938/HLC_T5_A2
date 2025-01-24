intentos = 0
while intentos < 3:
    contraseña = input("Introduce tu contraseña: ")
    if contraseña == "secreta123":
        print("Contraseña correcta. ¡Bienvenido!")
        break
    else:
        intentos += 1
        print(f"Intento {intentos}: Contraseña incorrecta.")
else:
    print("¡Has agotado tus intentos!")