import telebot
bot = telebot.TeleBot("***********************************")

# bot.send_message(351831201, "чем тебе помочь")
# upd = bot.get_updates()
# print(upd)


@bot.message_handler(content_types=['text'])
def handle_text(message): 
	if message.text == "сила тяжести" or message.text == "Сила тяжести":
		bot.send_message(message.chat.id, "F = mg\nВикипедия: https://ru.wikipedia.org/wiki/%D0%A1%D0%B8%D0%BB%D0%B0_%D1%82%D1%8F%D0%B6%D0%B5%D1%81%D1%82%D0%B8")
	elif message.text == "привет" or message.text == "Привет":
		bot.send_message(message.chat.id, "Салют. Как дела?")
	elif message.text == "нармально" or message.text == "отлично" or message.text == "Отлично" or message.text == "Нармально":
		bot.send_message(message.chat.id, "И у меня тоже всё хорошо! давай спраси меня о чем нибудь по физике")
	elif message.text == "сила упругости" or message.text == "Cила упругости" or message.text == "Закон Гука":
		bot.send_message(message.chat.id, "F = -kx\nВкикипедия: https://ru.wikipedia.org/wiki/%D0%A1%D0%B8%D0%BB%D0%B0_%D1%83%D0%BF%D1%80%D1%83%D0%B3%D0%BE%D1%81%D1%82%D0%B8")
	elif message.text == "закон архимеда" or message.text == "Закон архимеда" or message.text == "Архимедова сила":
		bot.send_message(message.chat.id, "F = pVg\nВикипедия https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%BA%D0%BE%D0%BD_%D0%90%D1%80%D1%85%D0%B8%D0%BC%D0%B5%D0%B4%D0%B0")
	elif message.text == "скорость" or message.text == "Скорость":
		bot.send_message(message.chat.id, "V = s/t\nВкикипедия: https://ru.wikipedia.org/wiki/%D0%A1%D0%BA%D0%BE%D1%80%D0%BE%D1%81%D1%82%D1%8C")
	elif message.text == "плотность" or message.text == "Плотность":
		bot.send_message(message.chat.id, "p = m/v\nВкикипедия: https://ru.wikipedia.org/wiki/%D0%9F%D0%BB%D0%BE%D1%82%D0%BD%D0%BE%D1%81%D1%82%D1%8C") 
	elif message.text == "вес тела" or message.text == "Вес тела" or message.text == "вес":
		bot.send_message(message.chat.id, "P = mg\nВкикипедия: https://ru.wikipedia.org/wiki/%D0%92%D0%B5%D1%81")
	elif message.text == "давление" or message.text == "Давление":
		bot.send_message(message.chat.id, "p = F/S\nВкикипедия: https://ru.wikipedia.org/wiki/%D0%94%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5")
	elif message.text == "давление в жидкости" or message.text == "Давление в жидкости":
		bot.send_message(message.chat.id, "P = pgh\nВкикипедия: Внутри жидкости в любой ее точке существует давление, обусловленное"\
		"весом верхних слоев жидкости на нижние. Если рассматривать жидкость в состоянии покоя, т.е. не двигающуюся, то это давление можно"\
		"назвать весовым  или гидростатическим давлением.")
	elif message.text == "площадь" or message.text == "Площадь":
		bot.send_message(message.chat.id, "S = ab\nВкикипедия: https://ru.wikipedia.org/wiki/%D0%9F%D0%BB%D0%BE%D1%89%D0%B0%D0%B4%D1%8C")
	elif message.text == "Объем" or message.text == "объем" or message.text == "объём" or message.text == "Объём":
		bot.send_message(message.chat.id, "V = Sh\nВкикипедия: https://ru.wikipedia.org/wiki/%D0%9E%D0%B1%D1%8A%D1%91%D0%BC")
	elif message.text == "сила трения" or message.text == "Сила трения" or message.text == "трение" or message.text == "Трение":
		bot.send_message(message.chat.id, "F = yP\nВкикипедия: https://ru.wikipedia.org/wiki/%D0%A2%D1%80%D0%B5%D0%BD%D0%B8%D0%B5")
	elif message.text == "работа" or message.text == "Работа":
		bot.send_message(message.chat.id, "A = Fs\nВкикипедия: Работа = сила × путь или A = Fs, где А - работа, F - сила и s - пройденный путь.")
	elif message.text == "мощность" or message.text == "Мощность":
		bot.send_message(message.chat.id, "N = A/t\nВкикипедия: https://ru.wikipedia.org/wiki/%D0%9C%D0%BE%D1%89%D0%BD%D0%BE%D1%81%D1%82%D1%8C")
	elif message.text == "момент силы" or message.text == "Момент силы":
		bot.send_message(message.chat.id, "M = Fl\nВкикипедия: https://ru.wikipedia.org/wiki/%D0%9C%D0%BE%D0%BC%D0%B5%D0%BD%D1%82_%D1%81%D0%B8%D0%BB%D1%8B")
	elif message.text == "Кинетическая энергия" or message.text == "кинетическая энергия":
		bot.send_message(message.chat.id, "E = mv**2 / 2\nВкикипедия: https://ru.wikipedia.org/wiki/%D0%9A%D0%B8%D0%BD%D0%B5%D1%82%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B0%D1%8F_%D1%8D%D0%BD%D0%B5%D1%80%D0%B3%D0%B8%D1%8F")
	elif message.text == "Потенциальная энергия" or message.text == "потенциальная энергия":
		bot.send_message(message.chat.id, "E = mgh\nВкикипедия: https://ru.wikipedia.org/wiki/%D0%9F%D0%BE%D1%82%D0%B5%D0%BD%D1%86%D0%B8%D0%B0%D0%BB%D1%8C%D0%BD%D0%B0%D1%8F_%D1%8D%D0%BD%D0%B5%D1%80%D0%B3%D0%B8%D1%8F")
	elif message.text == "сила" or message.text == "Сила":
		bot.send_message(message.chat.id, "Какая сила? Может вот эти:\nсила тяжести,\nсила упругости,\nсила трения")
	elif message.text == "Закон Паскаля" or message.text == "Закон паскаля" or message.text == "закон Паскаля" or message.text == "закон паскаля":
		bot.send_message(message.chat.id, "Какая сила? Может вот эти:\nсила тяжести")
	else:
		bot.send_message(message.chat.id, "Я не понимаю тебя, может где-то ошибка")




bot.polling(none_stop=True, interval=0)


