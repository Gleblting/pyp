import telebot
import socket
import ssl

hostname = 'www.telegram.org'
context = ssl.create_default_context()

with socket.create_connection((hostname, 443)) as sock:
    with context.wrap_socket(sock, server_hostname=hostname) as ssock:
        print(ssock.version())

bot = telebot.TeleBot('8011958480:AAFBfypy0tLaCjImAzrOuv3siwczZn06ufI')


@bot.message_handler(commands=['start'])
def start(message):
	bot.send_message(message.chat.id, '<b>Катка Связь!</b>', parse_mode='html')
	mess = f'Ваше ФИО: <b><u>{message.from_user.first_name} {message.from_user.last_name}</u></b>'
	bot.send_message(message.chat.id, mess, parse_mode='html' )


# @bot.message_handler()
# def get_user_text(message):
# 	bot.send_message(message.chat.id, message, parse_mode='html')


@bot.message_handler()
def get_user_text(message):#content_types=['text']
	if message.text == 'как дела у Глебки':
		bot.send_message(message.chat.id, "Глебка вкусно кушает и стал заниматься спортом" , parse_mode='html')
	elif message.text == 'что приготовил сегодня Глебка':
		bot.send_message(message.chat.id, "<b>Глебка потушил куррицу в сливках</b>", parse_mode='html')
	elif message.text == 'скинь фото':
		photo = open('dir/cartoony-bird-nest_23-2151002306.jpg', 'rb')
		bot.send_photo(message.chat.id, photo )
	else:
		bot.send_message(message.chat.id, "<b>Задай другой вопрос,я тебя не понимаю</b>", parse_mode='html')

@bot.message_handler(content_types=['photo'])
def content(message):
	bot.send_message(message.chat.id, '<b>Красивая фотография</b>', parse_mode='html')

bot.polling(none_stop=True)
