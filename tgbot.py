# telegram bot
import pyowm
import telebot
#from telebot import apihelper
import logging
logging.basicConfig(level=logging.DEBUG,format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

bot = telebot.TeleBot("877194843:AAGChcYUQ7Ol945JAHxSczaeuZfha0BbfRs", threaded=False)
#apihelper.proxy = {'https': 'socks5h://167.86.121.208:40077'}
owm = pyowm.OWM('8b79b20a5b368c91c5e9898490dc0a8a', language = 'ru')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Пожалуйста, напишите название города, для которого хотите узнать погоду.')

@bot.message_handler(content_types=['text'])
def send_echo(message):
	observation = owm.weather_at_place(message.text)
	w = observation.get_weather()
	temp = w.get_temperature('celsius')['temp']
	answer = 'В городе ' + message.text + ' сейчас ' + w.get_detailed_status() + '.\n'
	answer += 'Температура приблизительно ' + str(temp) + '°C' + '\n'

	bot.send_message(message.chat.id, answer)

while True:
	try:
	bot.polling(none_stop=True, timeout = 100)

	except Exception as e:
        print(e)  # или logger.error(e) если есть логгер,
        # или import traceback; traceback.print_exc() для печати полной инфы
        time.sleep(15)
