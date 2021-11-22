#WORKING

import requests
from bs4 import BeautifulSoup
from datetime import datetime

url = "https://www.sunat.gob.pe/"
response = requests.get(url)
html = BeautifulSoup(response.text, 'html.parser')

#day = html.find_all('date', {'id':"date"})
compra_sunat = html.find('strong', {'id': "buy-rate"})
venta_sunat = html.find('strong', {'id': "sell-rate"})

today = datetime.today().strftime("%d-%m-%y")

print(f"Tipo de Cambio {today}\nCompra: {compra_sunat.text}\nVenta: {venta_sunat.text}")