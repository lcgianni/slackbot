#coding: UTF-8
import re
from slackbot.bot import respond_to
from slackbot.bot import listen_to


@respond_to('hello|hi|hey|olá|ola|oi', re.IGNORECASE)
def hello_reply(message):
    message.reply('Olá, como posso lhe ajudar?')

@respond_to('entrar.*casa', re.IGNORECASE)
def hello_reply(message):
    message.reply('Do lado esquerdo da porta, você vai encontrar um cofre.')

@respond_to('endereço|endereco|endreco.*casa|house', re.IGNORECASE)
def hello_reply(message):
    message.reply('Esse é o endereço da casa.')

@respond_to('endereço|endereco|endreco.*galvanize|coworking', re.IGNORECASE)
def hello_reply(message):
    message.reply('Esse é o endereço da Galvanize.')

@respond_to('almoço|almoco|almocar', re.IGNORECASE)
def hello_reply(message):
    message.reply('Que tal comer neste lugar?')

@respond_to('janta|jantar', re.IGNORECASE)
def hello_reply(message):
    message.reply('Que tal jantar neste lugar?')

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
