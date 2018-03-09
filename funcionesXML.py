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

def datos_centro(consejeria,centro):

	doc=etree.parse('consejerias_madrid.xml')

	consejerias=doc.findall("consejeria")
	listanombre=[]
	listadireccion=[]
	listapostal=[]
	listaresponsable=[]
	for i in consejerias:
		if consejeria==i.find("nombre").text.replace("\n","").replace("\t",""):
			pedida=i.findall("organismo/centro")
			for j in pedida:
				if centro==j.find("nombre").text.replace("\n","").replace("\t","") and j.find("responsable") is not None:
					listanombre.append(j.find("nombre").text.replace("\n","").replace("\t",""))
					listadireccion.append(j.find("direccion").text.replace("\n","").replace("\t",""))
					listapostal.append(j.find("codigopostal").text.replace("\n","").replace("\t",""))
					listaresponsable.append(j.find("responsable").text.replace("\n","").replace("\t",""))
				elif centro==j.find("nombre").text.replace("\n","").replace("\t","") and j.find("responsable") is None:
					listanombre.append(j.find("nombre").text.replace("\n","").replace("\t",""))
					listadireccion.append(j.find("direccion").text.replace("\n","").replace("\t",""))
					listapostal.append(j.find("codigopostal").text.replace("\n","").replace("\t",""))
					listaresponsable.append("0")
	return zip(listanombre,listadireccion,listapostal,listaresponsable)



