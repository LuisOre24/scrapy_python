#NO OK
import requests
from bs4 import BeautifulSoup

url = "https://cuantoestaeldolar.pe/"
response = requests.get(url)
html = BeautifulSoup(response.text, 'html.parser')

p_compra = html.find_all('div', class_="tb_dollar_compra")
p_venta = html.find_all('div', class_="tb_dollar_venta")
entidad_html = html.find_all('h3')

entidades = list()
for entidad in entidad_html:
    entidades.append(entidad)

compras = list()
for compra in p_compra:
    compras.append(compra.text)

ventas = list()
for venta in p_venta:
    ventas.append(venta.text)

for p in zip(entidades, compras, ventas):
    print(p)