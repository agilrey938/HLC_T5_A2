import random
numero= random.randint(1, 50)

while True:
    n = int(input("Adivina el número "))
    if n == numero:
        print("¡Correcto!")
        break
    if n > numero:
        print("Es menor")
    elif n < numero:
        print("Es mayor")