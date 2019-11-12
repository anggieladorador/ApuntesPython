#!/usr/bin/env python


cadena = "supercalifragilistico"
# elige el caracter en la posicion indicada
print(cadena[2])
# imprime el ultimo indice del array
print(cadena[-1])
# seleccion entre indices, toma el primero indicado y el anterior al ultimo indicado
print(cadena[2:5])

# largo de cadena
largo = len(cadena)
print("largo cadena: "+str(largo))

# upperCase & lowerCase
print(cadena.upper())
print(cadena.lower())

# split
saludo = "hello world"
print(saludo.split())

fruitList = "manzana, naranja, avellana"
print(fruitList.split(","))

# concatenacion
animal = "jirafas"
peso = 700
print("las " + animal + " pueden alcanzar 5,8 metros de altura")
# format
print("y pueden tener un peso  que varia entre  {} y 1600 kg".format(peso))

nombre = "anggie"
edad = 26
print("mi nombre es {name} y tengo {age} ".format(name=nombre, age=edad))

pizza = "pizza"
bgg = "juegos de mesa"
print("me gusta la {p} y los {b}".format(p=pizza, b=bgg))

# f-string nota: no funciona aqui no sé por qué. en consola funciona. Averiguar*
comida = "hamburguesa"
juego = "catan"
print(f"hoy con nuestros amigos jugaremos {juego}, mientras comemos {comida}")
