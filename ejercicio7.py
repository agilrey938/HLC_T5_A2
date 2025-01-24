fibonacci = [0, 1]

for i in range(2, 10):
    siguiente_numero = fibonacci[i-1] + fibonacci[i-2]
    fibonacci.append(siguiente_numero)

print(fibonacci)