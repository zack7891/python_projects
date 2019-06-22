import requests
from bs4 import BeautifulSoup

page = requests.get('https://www.evomotorsusa.com/buy-cars-in-seffner-fl')

soup = BeautifulSoup(page.text, 'html.parser')

car_inventory = soup.find(class_='inventory-item_description_inner js-description-inner')

car_inventory_list = car_inventory.find_all("Clean Carfax")


for cars in car_inventory_list:
    names = cars.contents[0]
    links = 'https://www.evomotorsusa.com/buy-cars-in-seffner-fl' + cars.get('href')
    print(names)
    print(links)
