from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps
from pyowm.utils.config import get_default_config
import telebot

config_dict = get_default_config()
config_dict['language'] = 'en'

owm = OWM('f97fc709f4ef9864dea38cb41e81edca', config_dict)
mgr = owm.weather_manager()

bot = telebot.TeleBot("5031029858:AAEiPPEVMQuYJxC5iJAfRLBhlNzur5HQOLU")

@bot.message_handler(content_types=['text'])
def send_echo(message):
    observation = mgr.weather_at_place( message.text )
    w = observation.weather
    temp = w.temperature('celsius')['temp']

    answer = " It's " + w.detailed_status + " in " + message.text + " right now." + "\n"
    answer += "It's [" + str(temp) + "] celsius degrees" + "\n\n"

    if temp < 1:
        answer += " Winter is came "
    elif temp < 11:
        answer += " Warm up, it's pretty chilly there "
    elif temp < 21:
        answer += " Not that cold "
    elif temp < 31:
        answer += " It's wonderful temperature "
    elif temp > 30:
        answer += " It's bloody hell outside, drink more liquid "

    bot.send_message(message.chat.id, answer)
bot.infinity_polling()