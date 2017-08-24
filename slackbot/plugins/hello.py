#coding: UTF-8
import re
import random
import time
import datetime as dt

from slackbot.bot import respond_to
from slackbot.bot import listen_to
from slackbot.bot import default_reply


def choose_restaurant(meal):
    address = {'lunch': {'Uno Dos Tacos': '595 Market St.',
                         'Lemonade': '781 Market St.'},
               'dinner': {'4505 Burgers & BBQ': '705 Divisadero St.',
                          'Kung Food': '1615 McAllister St.',
                          'Saffron Grill': '1279 Fulton St.',
                          'El Rancho Grande': '855 Divisadero St.'}}
    choice = random.choice(list(address[meal].keys()))
    return choice, address[meal][choice]

def choose_experience():
    options = ['Já caminhou até a Golden Gate Bridge? Peça dicas ao @lcgianni',
               'Conheça o Golden Gate Park',
               'Visite a Prisão de Alcatraz',
               'Vá de carro até Napa Valley',
               'Vá de carro até o Yosemite',
               'Ouça Friends do Justin Bieber',
               'Pergunte para a @agueda sobre cachorro-quente']
    choice = random.choice(options)
    return choice

@respond_to('hello|hi|hey|olá|ola|oi', re.IGNORECASE)
def hello_reply(message):
    message.reply('Olá! Como posso lhe ajudar?')
    wait_before_answering(2)
    message.reply('Me pergunte sobre onde comer, como chegar na casa e na Galvanize, e passeios para fazer em São Francisco.')

@respond_to('aeroporto.*casa', re.IGNORECASE)
def arrive_at_house_reply(message):
    message.reply('A melhor forma de ir do aeroporto até a casa é pedindo um Uber. Qualquer dúvida, me pergunte qual o endereço da casa.')

@respond_to('endereço|endereco|endreco.*casa|house|casa', re.IGNORECASE)
def house_address_reply(message):
    message.reply('O endereço da casa é 1314 Fulton St.')

@respond_to('entrar.*casa', re.IGNORECASE)
def enter_house_reply(message):
    message.reply('Do lado esquerdo da porta, você vai encontrar um cofre. A senha é 143133. Dentro deste cofre, você encontrará a chave da casa.')

@respond_to('endereço|endereco|endreco.*galvanize|coworking|galvanize', re.IGNORECASE)
def galvanize_address_reply(message):
    message.reply('O endereço da Galvanize é 543 Howard St.')

def wait_before_answering(seconds):
    time.sleep(seconds)

def reply_with_meal(message, meal):
    message.reply('Hmmmm... Deixa eu pensar em um lugar legal para %s.' %(meal))
    wait_before_answering(3)

def is_early():
    if dt.datetime.now().hour < 15: return True; return False

def is_weekday():
    if dt.datetime.today().weekday() <= 5: return True; return False

@respond_to('comer|fome|comida', re.IGNORECASE)
def eat_reply(message):
    if is_early() and is_weekday():
        reply_with_meal(message, 'almoçar')
        lunch_reply(message)
    else:
        reply_with_meal(message, 'jantar')
        dinner_reply(message)

def reply_with_address(message, choice, address):
    message.reply("Que tal comer no %s? O endereço é %s" % (choice, address))

@respond_to('almoço|almoco|almocar', re.IGNORECASE)
def lunch_reply(message):
    choice, address = choose_restaurant(meal='lunch')
    reply_with_address(message, choice, address)

@respond_to('janta|jantar', re.IGNORECASE)
def dinner_reply(message):
    choice, address = choose_restaurant(meal='dinner')
    reply_with_address(message, choice, address)

@respond_to('evento', re.IGNORECASE)
def event_reply(message):
    message.reply('Dê uma olhada no eventbrite.com ou meetup.com')

@respond_to('entediado|bored|passeio|visita|conhecer|passear|visitar', re.IGNORECASE)
def bored_reply(message):
    message.reply(choose_experience())

@respond_to('musica|música', re.IGNORECASE)
def song_reply(message):
    message.reply('Miley Cyrus')

@respond_to('idade', re.IGNORECASE)
def age_reply(message):
    message.reply('Tenho 42 anos')

@respond_to('seu|teu.*nome', re.IGNORECASE)
def name_reply(message):
    message.reply('Meu nome é Henrique Herculano Tormena')

@respond_to('thanks|thank|thanx|obrigado|orbgiado|obg|valeu', re.IGNORECASE)
def thankyou_reply(message):
    message.react('+1')

@respond_to('tchau|valeu|flw|vlw', re.IGNORECASE)
def bye_reply(message):
    message.reply('Até mais!')

@respond_to('.*', re.IGNORECASE)
def save(message):
    print('Saving message...')

@default_reply
def my_default_hanlder(message):
    message.reply('Falou a pessoa que assiste filme de salsicha.')

#senha da casa
#senha do wifi
#pessoas de cada batch darem sugestoes para melhorar
#dicas de empresas (offices legais, boas praticas de RH, CRM do Tormena)
