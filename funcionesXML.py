from lxml import etree

def nombre_consejerias():
	
	doc=etree.parse('consejerias_madrid.xml')

	consejerias=doc.findall("consejeria")
	lista=[]
	lista2=[]
	for i in consejerias:
		nombre=i.find("nombre")
		lista.append(nombre.text.replace("\n\t\t\t",""))
	for elem in lista:
		lista2.append(elem.replace("\n\t\t",""))
	return lista2


def contar_organismos():

	doc=etree.parse('consejerias_madrid.xml')

	consejerias=doc.findall("consejeria")
	lista=[]
	for i in consejerias:
		contador=0
		if i.find("organismo"):
			numorganismo=i.findall("organismo")
			for j in numorganismo:
				lista.append(i.find("organismo/nombre").text)
	return lista

for i in nombre_consejerias():
	print("-",i)

for i in contar_organismos():
	print(i,"->",j)
