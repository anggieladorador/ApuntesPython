#!/usr/bin/env python
numeros = [1, 3, 5, 7, 9]
for num in numeros:
    print(num)

cadena = "hello world"
for caracter in cadena:
    print(caracter)

range(8)
for numero in range(8):
    print(numero)

for numero in range(3, 8):
    print(numero)

for numero in range(3, 8, 2):  # del 3 al 8, 2 = saltos
    print(numero)

print("*************")
for numero in range(10):
    if(numero == 5):
        break
    print(numero)

# continue : para saltar la iteracion actual
print("********************")
for numero in range(10):
    if(numero == 3):
        continue
    print(numero)

print("******************")
for numero1 in range(4):
    for numero2 in range(3):
        print(numero1, numero2)
