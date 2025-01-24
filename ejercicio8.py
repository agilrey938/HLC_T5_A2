n = int(input("¿Introduce un valor? "))

if n < 0:
    print("El número debe ser posivivo")
else:
    cuadrados = [x**2 for x in range(1, n+1)]
print(cuadrados)