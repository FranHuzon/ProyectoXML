from lxml import etree

def nombre_consejerias():
	
	doc=etree.parse('consejerias_madrid.xml')

	consejerias=doc.findall("consejeria")
	lista=[]
	for i in consejerias:
		nombre=i.find("nombre")
		lista.append(nombre.text)
	for elem in lista:
		elem.replace("\n\t\t\t","")
	
	return lista


print(nombre_consejerias())








