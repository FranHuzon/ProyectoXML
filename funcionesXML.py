from lxml import etree

def nombre_consejerias():
	
	doc=etree.parse('consejerias_madrid.xml')

	consejerias=doc.findall("consejeria")
	lista=[]
	lista2=[]
	for i in consejerias:
		nombre=i.find("nombre")
		lista.append(nombre.text.replace("\n","").replace("\t",""))

	return lista


def contar_organismos():

	doc=etree.parse('consejerias_madrid.xml')

	consejerias=doc.findall("consejeria")
	lista=[]
	for i in consejerias:
		organismos=i.findall("organismo")
		lista.append(len(organismos))
	return lista

def filtra_organismos(subcad):

	doc=etree.parse('consejerias_madrid.xml')

	organismos=doc.findall("/consejeria/organismo")
	lista=[]
	for i in organismos:
		if subcad in i.find("nombre").text:
			lista.append(i.find("nombre").text.replace("\n","").replace("\t",""))
		
	return lista

def filtra_datos_consejeria(subcad):

	doc=etree.parse('consejerias_madrid.xml')

	consejerias=doc.findall("consejeria")
	lista=[]
	lista2=[]
	for i in consejerias:
		if subcad==i.find("nombre").text.replace("\n","").replace("\t",""):
			pedida=i.findall("organismo")
			for j in pedida:
				if j.find("responsable") is not None:
					lista.append(j.find("nombre").text.replace("\n","").replace("\t",""))
					lista2.append(j.find("responsable").text.replace("\n","").replace("\t",""))
				else:
					lista.append(j.find("nombre").text.replace("\n","").replace("\t",""))
					lista2.append("0")
	return zip(lista,lista2)

def 


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

