# !/usr/bin/env python

# clase => constructor de objetos


class Persona:
    def __init__(self, nombre, edad):  # constructor, self referencia a los atributos de la clase
        self.nombre = nombre
        self.edad = edad

    def saludar():
        print("hola soy ")


Persona1 = Persona("anggie", 26)
