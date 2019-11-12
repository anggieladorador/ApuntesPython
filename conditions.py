#!/usr/bin/env python
# CONDICIONES (if, elif, else)

a = 8
b = 4

if(a > b):
    print("a es mayor que b")

c = 2
d = 6

################################################

if(a > c) and (b > d):
    print("la expresion es verdadera")  # 8>2 y 4>6?
else:
    print("la expresion es falsa!")

##############################################

if(a < b):
    print("a es menor que b")
elif (a == b):
    print("a es igual a b")
else:
    print("a es mayor a b")
