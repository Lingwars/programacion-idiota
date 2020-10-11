import requests
from lxml import html

def download_html(url):
	'''
	Descarga el contenido de una página a partir de una url y lo devuelve
	'''
	response = requests.get(url)
	if response.status_code != 200:
		message = "Error {} retrieving url {}".format(response.status_code, url)
		raise Exception(message)
	return response.content

def download_artists_page(index):
	'''
	Descarga el contenido de la página de artistas españoles a partir de
	un número y lo devuelve
	'''
	url_prefix = "https://www.last.fm/es/tag/spanish/artists?page="
	return download_html(url_prefix + str(index))

def build_xpath(index):
	'''
	Busca en la página de artistas el nombre del correspondiente a partir de
	un número
	'''
	xpath_prefix = "/html/body/div[4]/div[2]/div[3]/div[3]/div/div[1]/section/ol/li["
	xpath_suffix = "]/div/h3/a"
	return xpath_prefix + str(index) + xpath_suffix

def get_data(index):
	'''
	Lee una página a partir de un número, busca los nombres de los artistas y
	los devuelve en una lista
	'''
	page = download_artists_page(index)
	tree = html.fromstring(page)
	names = []
	for i in range(1, 24): # Hay 24 artistas por página
		results = tree.xpath(build_xpath(i))
		for r in results:
			names.append(r.text)
	return names

def fetch_all_names():
	'''
	Busca en todas las páginas de artistas y devuelve todos los nombres de los
	artistas en una lista
	'''
	list = []
	for index in range(1, 48): # Hay 48 páginas de artistas con el tag Spanish
		for name in get_data(index):
			list.append(name)
	return list


def write_names_to_file(names, file):
	'''
	Escribe la lista de nombres en el archivo que quieras
	'''
	with open(file, "w", encoding="UTF-8") as file:
		for name in names:
			file.write(name + "\n")


write_names_to_file(fetch_all_names(), "artistas_españoles.txt")
