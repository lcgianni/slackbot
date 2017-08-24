#coding: UTF-8
import re
import random

from slackbot.bot import respond_to
from slackbot.bot import listen_to

def choose_restaurant(meal='lunch'):
    address = {'dinner': {'4505 BBQ': '234 Divisadero St.',
                          'Signores Pizza': '234 Fulton St.'}}
    choice = random.choice(list(address[meal].keys()))
    return choice, address[meal][choice]

@respond_to('hello|hi|hey|olá|ola|oi', re.IGNORECASE)
def hello_reply(message):
    message.reply('Olá, como posso lhe ajudar?')

@respond_to('aeroporto.*casa', re.IGNORECASE)
def hello_reply(message):
    message.reply('A melhor forma de ir do aeroporto até a casa é pedindo um Uber. Qualquer dúvida, me pergunte qual o endereço da casa.')

@respond_to('endereço|endereco|endreco.*casa|house', re.IGNORECASE)
def hello_reply(message):
    message.reply('O endereço da casa é 1314 Fulton St.')

@respond_to('entrar.*casa', re.IGNORECASE)
def hello_reply(message):
    message.reply('Do lado esquerdo da porta, você vai encontrar um cofre. A senha é 143133. Dentro deste cofre, você encontrará a chave da casa.')

@respond_to('endereço|endereco|endreco.*galvanize|coworking', re.IGNORECASE)
def hello_reply(message):
    message.reply('O endereço da Galvanize é 543 Howard St.')

@respond_to('almoço|almoco|almocar', re.IGNORECASE)
def hello_reply(message):
    message.reply('Que tal comer neste lugar?')

@respond_to('janta|jantar', re.IGNORECASE)
def hello_reply(message):
    choice, address = choose_restaurant(meal='dinner')
    message.reply("Que tal jantar no %s? O endereço é %s", (choice, address))

@respond_to('evento', re.IGNORECASE)
def hello_reply(message):
    message.reply('Dê uma olhada no eventbrite.com ou meetup.com')

@respond_to('musica|música', re.IGNORECASE)
def hello_reply(message):
    message.reply('Miley Cyrus')

@respond_to('^reply_webapi$')
def hello_webapi(message):
    message.reply_webapi('hello there!', attachments=[{
        'fallback': 'test attachment',
        'fields': [
            {
                'title': 'test table field',
                'value': 'test table value',
                'short': True
            }
        ]
    }])


@respond_to('^reply_webapi_not_as_user$')
def hello_webapi_not_as_user(message):
    message.reply_webapi('hi!', as_user=False)


@respond_to('hello_formatting')
def hello_reply_formatting(message):
    # Format message with italic style
    message.reply('_hello_ sender!')
