
from funcionesXML import nombre_consejerias,contar_organismos,filtra_organismos,filtra_datos_consejeria,datos_centro


print('''
	1.Nombre de las consejerías de Madrid.
	2.Número de organismos que tiene cada consejería.
	3.Búsqueda de organismos por caracteres introducidos.
	4.Búsqueda de organismos y responsables por consejería.
	5.Información concreta de un centro específico de una consejería.
	0.SALIR.
	''')
opcion=input("Escoge una opción del menú: ")

while opcion!="0":
	if opcion=="1":
		for i in nombre_consejerias():
			print("-",i)


	if opcion=="2":
		conteo=zip(nombre_consejerias(),contar_organismos())
		for i in conteo:
			print("-",i[0],"->",i[1])


	if opcion=="3":
		subcad=input("Introduce una subcadena: ")
		print("Estos son los organismos que contienen la subcadena introducidad:")
		for i in filtra_organismos(subcad):
			print("-",i)


	if opcion=="4":
		subcad=input("Introduce una consejería: ")

		for i in filtra_datos_consejeria(subcad):
			if i[1]=="0":
				print("-",i[0],"->","Este organismo no tiene una persona como responsable")
			else:
				print("-",i[0],"->",i[1])


	if opcion=="5":
		consejeria=input("Introduce una consejería: ")
		centro=input("Introduce un centro: ")

		for i in datos_centro(consejeria,centro):
			if i[3]=="0":
				print("Los datos del centro",i[0],"son :", i[1],";",i[2],";","Este organismo no tiene una persona como responsable.")
			else:
				print("Los datos del centro",i[0],"son :", i[1],";",i[2],";",i[3])
		break

	else:
		print('''
	1.Nombre de las consejerías de Madrid.
	2.Número de organismos que tiene cada consejería.
	3.Búsqueda de organismos por caracteres introducidos.
	4.Búsqueda de organismos y responsables por consejería.
	5.Información concreta de un centro específico de una consejería.
	0.SALIR.
	''')
		opcion=input("Escoge otra opción del menú: ")



#Consejería de Presidencia, Justicia y Portavocía del Gobierno
#Subdirección General de lo Consultivo y Asuntos Constitucionales