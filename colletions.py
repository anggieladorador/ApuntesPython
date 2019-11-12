#!/usr/bin/env python
# LISTA -> coleccion de elementos modificables
colores = ["rojo", "amarillo", "verde"]
print(colores[0])
print(len(colores))  # len = largo
colores.append("turquesa")
print(colores)
colores.remove("rojo")
print(colores)

for color in colores:
    print(color)

# colores.clear()   limpia la lista (probar en consola)

# TUPLA --> coleccion de elementos ORDENADA y NO modificable
tupla_colores = ("cyan", "magenta", "amarillo")
print(tupla_colores)
print(len(tupla_colores))

# CONJUNTOs  --> colleccion de elementos NO ordenada, no se puede acceder por indeces

conjunto_colores = {"beige", "rosa", "vermellon"}
print(conjunto_colores)
for color in conjunto_colores:
    print(color)

# print(conjunto_colores[0])  error: set no soporta indexacion
print(len(conjunto_colores))

conjunto_colores.add("negro")  # lo coloca en cualquier lugar de la lista
print(conjunto_colores)

conjunto_colores.remove("rosa")
print(conjunto_colores)

# DICCIONARIO {"clave":"valor"}

diccionario_colores = {"red": "rojo", "blue": "azul", "green": "verde"}
print(diccionario_colores)

print(diccionario_colores["red"])

# agregar datos al diccionario
diccionario_colores["pink"] = "rosa"

print(diccionario_colores)

# eliminacion de elementos en el diccionario
diccionario_colores.pop("red")
print(diccionario_colores)

del(diccionario_colores["blue"])
print(diccionario_colores)

for color in diccionario_colores:
    print(color)

for key, value in diccionario_colores.items():
    print(key + ":"+value)
