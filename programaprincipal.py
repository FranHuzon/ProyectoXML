from lxml import tree
from funcionesXML import nombre_consejerias,contar_organismos,filtra_datos_consejeria,datos_centro

for i in nombre_consejerias():
	print("-",i)

print()
print("-"*50)
print()

conteo=zip(nombre_consejerias(),contar_organismos())

for i in conteo:
	print("-",i[0],"->",i[1])

print()
print("-"*50)
print()

subcad=input("Introduce una subcadena: ")
print("Estos son los organismos que contienen la subcadena introducidad:")
for i in filtra_organismos(subcad):
	print("-",i)

print()
print("-"*50)
print()

subcad=input("Introduce una consejería: ")

for i in filtra_datos_consejeria(subcad):
	if i[1]=="0":
		print("-",i[0],"->","Este organismo no tiene una persona como responsable")
	else:
		print("-",i[0],"->",i[1])

print()
print("-"*50)
print()

consejeria=input("Introduce una consejería: ")
centro=input("Introduce un centro: ")

for i in datos_centro(consejeria,centro):
	if i[3]=="0":
		print("Los datos del centro",i[0],"son :", i[1],";",i[2],";","Este organismo no tiene una persona como responsable")
	else:
		print("Los datos del centro",i[0],"son :", i[1],";",i[2],";",i[3])