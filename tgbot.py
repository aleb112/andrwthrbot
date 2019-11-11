# telegram bot
import pyowm
import telebot
owm = pyowm.OWM('8b79b20a5b368c91c5e9898490dc0a8a', language = 'ru')
bot = telebot.TeleBot("877194843:AAGChcYUQ7Ol945JAHxSczaeuZfha0BbfRs")
from telebot import apihelper
apihelper.proxy = {
    'https': 'socks5h://207.154.231.216:1080'
}

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Пожалуйста, напишите название города, для которого хотите узнать погоду.')

@bot.message_handler(content_types=['text'])
def send_echo(message):
	observation = owm.weather_at_place(message.text)
	w = observation.get_weather()
	temp = w.get_temperature('celsius')['temp']
	answer = 'В городе ' + message.text + ' сейчас ' + w.get_detailed_status() + '\n'
	answer += 'Температура приблизительно ' + str(temp) + '\n\n'

	bot.send_message(message.chat.id, answer)

while True:
    try:
        bot.polling(none_stop=True)

    except Exception as e:
        print(e)  # или logger.error(e) если есть логгер,
        # или import traceback; traceback.print_exc() для печати полной инфы
        time.sleep(15)
