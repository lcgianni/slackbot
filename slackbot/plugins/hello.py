#coding: UTF-8
import re
import random
import datetime as dt

from slackbot.bot import respond_to
from slackbot.bot import listen_to

def choose_restaurant(meal='lunch'):
    address = {'lunch': {'4505 BBQ': '234 Divisadero St.',
                         "Signore's Pizza": '234 Fulton St.'},
               'dinner': {'4505 BBQ': '234 Divisadero St.',
                          "Signore's Pizza": '234 Fulton St.'}}
    choice = random.choice(list(address[meal].keys()))
    return choice, address[meal][choice]

@respond_to('hello|hi|hey|olá|ola|oi', re.IGNORECASE)
def hello_reply(message):
    message.reply('Olá, como posso lhe ajudar?')

@respond_to('aeroporto.*casa', re.IGNORECASE)
def arrive_at_house_reply(message):
    message.reply('A melhor forma de ir do aeroporto até a casa é pedindo um Uber. Qualquer dúvida, me pergunte qual o endereço da casa.')

@respond_to('endereço|endereco|endreco.*casa|house', re.IGNORECASE)
def house_address_reply(message):
    message.reply('O endereço da casa é 1314 Fulton St.')

@respond_to('entrar.*casa', re.IGNORECASE)
def enter_house_reply(message):
    message.reply('Do lado esquerdo da porta, você vai encontrar um cofre. A senha é 143133. Dentro deste cofre, você encontrará a chave da casa.')

@respond_to('endereço|endereco|endreco.*galvanize|coworking', re.IGNORECASE)
def galvanize_address_reply(message):
    message.reply('O endereço da Galvanize é 543 Howard St.')

@respond_to('comer|fome', re.IGNORECASE)
def eat_reply(message):
    current_time = dt.datetime.now().hour
    weekday = dt.datetime.today().weekday()
    if current_time < 15 and weekday >= 5:
        lunch_reply(message)
    dinner_reply(message)

@respond_to('almoço|almoco|almocar', re.IGNORECASE)
def lunch_reply(message):
    choice, address = choose_restaurant(meal='lunch')
    message.reply("Que tal almoçar no %s? O endereço é %s" % (choice, address))

@respond_to('janta|jantar', re.IGNORECASE)
def dinner_reply(message):
    choice, address = choose_restaurant(meal='dinner')
    message.reply("Que tal jantar no %s? O endereço é %s" % (choice, address))

@respond_to('evento', re.IGNORECASE)
def event_reply(message):
    message.reply('Dê uma olhada no eventbrite.com ou meetup.com')

@respond_to('entediado|bored', re.IGNORECASE)
def bored_reply(message):
    message.reply('Caminhe até a Golden Gate Bridge')

@respond_to('musica|música', re.IGNORECASE)
def song_reply(message):
    message.reply('Miley Cyrus')
