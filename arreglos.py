"""""
Problema : Objetivo: Area que calcula el area de un triangulo
Usuario: General
SO: Windows, Linux, MAC
Interface: Cline
Autor: alereavila (alereavila8@gmail.com)
Programa que muestra un Hola Mundo
"""
print("Conjunto")
conjunto1={"a","b","c","d"}

lista1=[1,2,3,4,5,6,7]
conjunto2=set(lista1)
print(conjunto2)
minimo= min(conjunto1)
print(minimo)
conjunto3=conjunto1
conjunto3.add("x")
print(conjunto3 is conjunto1)
print("Si quiero tener dos conjuntos")
conjunto4=conjunto3.copy()

conjunto4.discard(1)
print(conjunto4)
conjunto4.discard("x")
print(conjunto4)
print("se puede agregar conjunto a otro conjunto")
conjunto4.update(conjunto2)
print(conjunto4)
print("funciones de conjuntos")
print(conjunto1.union(conjunto2))
print(conjunto1.intersection(conjunto2))
print(conjunto4.difference(conjunto2))
print(conjunto4.symmetric_difference(conjunto2))
print("tambien se puede hacer con operadores")
print(conjunto1 | conjunto2)
print(conjunto1 & conjunto2)
print(conjunto4 - conjunto2)
print(conjunto4 ^ conjunto2)