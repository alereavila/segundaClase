dicGen={"nombre":"p53","taxomonia":9666,"union fuerte":True,"ubicacion":["citplasma","nucleo"]}
print(dicGen)
print(dicGen["taxomonia"])
print(dicGen["ubicacion"][0])
print(type(dicGen["taxomonia"]))
print("agegar nueva llave")
dicGen["id"]="x1278"
print(dicGen)
dicGen[(2,3)]="llave tipo dupla"
print(dicGen)
print("Prpblema con diccionario")
datos={}

