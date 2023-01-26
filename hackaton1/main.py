import csv
import requests
from bs4 import BeautifulSoup
from bs4.element import ResultSet,Tag

URL = 'https://www.kivano.kg/mobilnye-telefony'

response = requests.get(URL)
html = response.text

total = []
soup = BeautifulSoup(html, 'html.parser')
card = soup.find_all('div', class_='item')

for i in card:
    name = i.find('div', class_='listbox_title oh').text
    cena = i.find('div', class_='listbox_price text-center').text
    kartina = i.find('div', class_='listbox_img pull-left').find('img').get('src')

    
    obj = {
    'name': name,
    'cena': cena,
    'kartina': kartina,
    }    
    total.append(obj)


with open('hackaton.csv', 'w') as file:
    zagolovki = ['name', 'cena', 'kartina']
    writer = csv.DictWriter(file, fieldnames=zagolovki)
    writer.writeheader()
    for info in total:
        writer.writerow(info)