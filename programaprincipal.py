
from funcionesXML import nombre_consejerias,contar_organismos,filtra_organismos,filtra_datos_consejeria,datos_centro


opcion=input('''	
	1.Nombre de las consejerías de Madrid.
	2.Número de organismos que tiene cada consejería.
	3.Búsqueda de organismos por caracteres introducidos.
	4.Búsqueda de organismos y responsables por consejería.
	5.Información concreta de un centro específico de una consejería.
	0.SALIR.
	Escoge una opción del menú: ''')

while not opcion==0:
	if opcion==1:
		for i in nombre_consejerias():
			print("-",i)

	elif opcion==2:
		conteo=zip(nombre_consejerias(),contar_organismos())
		for i in conteo:
			print("-",i[0],"->",i[1])

	elif opcion==3:
		subcad=input("Introduce una subcadena: ")
		print("Estos son los organismos que contienen la subcadena introducidad:")
		for i in filtra_organismos(subcad):
			print("-",i)

	elif opcion==4:
		subcad=input("Introduce una consejería: ")

		for i in filtra_datos_consejeria(subcad):
			if i[1]=="0":
				print("-",i[0],"->","Este organismo no tiene una persona como responsable")
			else:
				print("-",i[0],"->",i[1])

	elif opcion==5:
		consejeria=input("Introduce una consejería: ")
		centro=input("Introduce un centro: ")

		for i in datos_centro(consejeria,centro):
			if i[3]=="0":
				print("Los datos del centro",i[0],"son :", i[1],";",i[2],";","Este organismo no tiene una persona como responsable")
			else:
				print("Los datos del centro",i[0],"son :", i[1],";",i[2],";",i[3])


