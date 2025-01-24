palabra = input("Introduce una palabra: ")

simbolos_especiales = ['@', '#', '$', '%']

for simbolo in simbolos_especiales:
    if simbolo in palabra:
        print(f"La palabra contiene el símbolo {simbolo}.")
        break
else:
    print("La palabra no contiene ningún símbolo especial.")