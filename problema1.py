"""""
Problema : Objetivo: Programa solicita al usuario algunos datos
Usuario: General
SO: Windows, Linux, MAC
Interface: Cline
Autor: alereavila (alereavila8@gmail.com)
Programa que muestra un Hola Mundo
"""
persona={}
nombre= input("Introduce tu nombre   :")
persona["nombre"]=nombre
edad=input("Proporciona tu edad")
persona["edad"]=edad
direccion=input("Ingresa tu direccion")
persona["direccion"]=direccion
telefono=input("Ingresa tu telefono ")
persona["telefono"]=telefono
print(persona)
print(f"{persona['nombre']}  tiene {persona['edad']}")
print(persona.items())
print(persona.keys())
print("formas de devolver")
print(persona.get("nombre"))
print(persona.get("apellido","No existe esta llave"))
print("se puede borrar con pop")