def determinar_mayor():
    a= int(input("Introduce el primer valor "))
    b= int(input("Introduce el segundo valor "))
    c= int(input("Introduce el tercer valor "))

    if a == b == c:
        print("Todos los números son iguales:", a)
    elif a == b and a > c:
        print("Hay un empate entre los mayores:", a, "y", b)
    elif a == c and a > b:
        print("Hay un empate entre los mayores:", a, "y", c)
    elif b == c and b > a:
        print("Hay un empate entre los mayores:", b, "y", c)
    else:
        mayor = max(a, b, c)
        print("El mayor número es:", mayor)
determinar_mayor()