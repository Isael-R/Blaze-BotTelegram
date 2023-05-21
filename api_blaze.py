import requests
import json
import telebot
from time import sleep


cont = 0
while cont < 5:
    request_api = requests.get('https://blaze.com/api/roulette_games/recent')
    response = request_api.json()

    giros = []
    for item in response:
        if item['color'] == 0:
            item['color'] = 'Branco'
        elif item['color'] == 1:
            item['color'] = 'Vermelha'
        else:
            item['color'] = 'Preta'
        giros.append(f'{item["roll"]}  {item["color"]}')

    for giro in giros[:4]:
        print(giro)
    cont += 1
    sleep(15)
    print('-'*20)
