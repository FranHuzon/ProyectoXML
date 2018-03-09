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








for i in nombre_consejerias():
	print("-",i)

print()
print("-"*50)
print()

conteo=zip(nombre_consejerias(),contar_organismos())

for i in conteo:
	print(i[0],"->",i[1])

print()
print("-"*50)
print()

subcad=input("Introduce una subcadena: ")
