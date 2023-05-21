import telebot
import requests
import json
from time import sleep

CHAVE_API = ''
bot = telebot.TeleBot(CHAVE_API)
id_grupo = ''


@bot.message_handler(commands=['start'])
def enviar_msg_grupo(mensagem):
    if mensagem:
        while True:
            request_api = requests.get('https://blaze.com/api/roulette_games/recent')
            response = request_api.json()
            ultimos_resultados = []
            for item in response:
                if item['color'] == 0:
                    item['color'] = 'Branco'
                elif item['color'] == 1:
                    item['color'] = 'Vermelha'
                else:
                    item['color'] = 'Preta'
                ultimos_resultados.append(f'{item["roll"]}  {item["color"]}')
            sleep(15)    
            bot.send_message(id_grupo, f"Quatro ultimos resultados{ultimos_resultados[:4]}")


def verificar(mensagem):
    return True

@bot.message_handler(func=verificar)
def responder(mensagem):
    texto = '/start'
    bot.reply_to(mensagem, texto)

bot.polling()