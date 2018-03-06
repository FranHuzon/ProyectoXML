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


print(nombre_consejerias())








