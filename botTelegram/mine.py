import telebot
import random
bot = telebot.TeleBot("449027989:AAHC8m5yUMBmx0Z0Alq6fN0ooMr4QDZvDS0")

# bot.send_message(351831201, "чем тебе помочь")
# upd = bot.get_updates()
# print(upd)

@bot.message_handler(commands=['start'])
def handle_start(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
    user_markup.row('/start', '/stop')
    user_markup.row('/умения', '/создатели', '/информация')
    bot.send_message(message.from_user.id, 'Добро пожаловать..', reply_markup=user_markup)

@bot.message_handler(commands=['stop'])
def handle_start(message):
    user_markup = telebot.types.ReplyKeyboardMarkup()
    bot.send_message(message.from_user.id, 'Goodbye', reply_markup=user_markup)

@bot.message_handler(commands=['умения'])
def handle_start(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True)
    bot.send_message(message.from_user.id, 'Этот бот знает формулы по физике из программы 7-го класса и ученныx физиков.Например напиши "Кинетическая энергия"', reply_markup=user_markup)

@bot.message_handler(commands=['создатели'])
def handle_start(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True)
    bot.send_message(message.from_user.id, 'Гусейнов Альберт - 13лет\nФаталиев Джавид - 13лет', reply_markup=user_markup)

@bot.message_handler(commands=['информация'])
def handle_start(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True)
    bot.send_message(message.from_user.id, 'Бот создан 18.08.2017г\nАвторы: Гусейнов Альберт, Фаталиев Джавид\nСделан для добрых целей', reply_markup=user_markup)


@bot.message_handler(content_types=['text'])
def handle_text(message): 
    if message.text == "сила тяжести" or message.text == "Сила тяжести":
        bot.send_message(message.chat.id, "F = mg\nВикипедия: https://ru.wikipedia.org/wiki/Сила_тяжести")
    elif message.text == "привет" or message.text == "Привет":
        bot.send_message(message.chat.id, "Салют. Спроси у меня про ученого или про закон?")
    elif message.text == "Закон сохранения энергии" or message.text == "закон сохранения энергии":
        bot.send_message(message.chat.id, "Зако́н сохране́ния эне́ргии — фундаментальный закон природы, установленный эмпирически и"\
            "заключающийся в том, что для изолированной физической системы может быть введена скалярная физическая величина, являющаяся"\
            " функцией параметров системы и называемая энергией, которая сохраняется с течением времени. Поскольку закон сохранения"\
            " энергии относится не к конкретным величинам и явлениям, а отражает общую, применимую везде и всегда, закономерность, то"\
            " его можно именовать не законом, а принципом сохранения энергии.\nВикипедия: https://ru.wikipedia.org/wiki/Закон_сохранения_энергии")
    elif message.text == "нармально" or message.text == "отлично" or message.text == "Отлично" or message.text == "Нармально":
        bot.send_message(message.chat.id, "И у меня тоже всё хорошо! давай спраси меня о чем нибудь по физике")
    elif message.text == "Закон Паскаля" or message.text == "Закон паскаля" or message.text == "закон Паскаля" or message.text == "закон паскаля":
        bot.send_message(message.chat.id, "Давление, производимое на жидкость или газ, передается в любую точку без изменений во всех направлениях.\nВикипедия: https://ru.wikipedia.org/wiki/Закон_Паскаля")
    elif message.text == "сила упругости" or message.text == "Cила упругости" or message.text == "Закон Гука" or message.text == "закон Гука" or message.text == "закон гука":
        bot.send_message(message.chat.id, "F = -kx\nВкикипедия: https://ru.wikipedia.org/wiki/Cила_упругости")
    elif message.text == "закон архимеда" or message.text == "Закон архимеда" or message.text == "Архимедова сила" or message.text == "Закон Архимеда":
        bot.send_message(message.chat.id, "F = pVg\nВикипедия https://ru.wikipedia.org/wiki/Закон_Архимеда")
    elif message.text == "скорость" or message.text == "Скорость":
        bot.send_message(message.chat.id, "V = s/t\nВкикипедия: https://ru.wikipedia.org/wiki/Скорость")
    elif message.text == "Материя" or message.text == "материя":
        bot.send_message(message.chat.id, "Мате́рия (от лат. māteria «вещество») — основное понятие физики, общий термин, определяющийся множеством всего содержимого пространства-времени и влияющее на его свойства.\nВикипедия: https://ru.wikipedia.org/wiki/Материя")
    elif message.text == "плотность" or message.text == "Плотность":
        bot.send_message(message.chat.id, "p = m/v\nВкикипедия: https://ru.wikipedia.org/wiki/Плотность") 
    elif message.text == "вес тела" or message.text == "Вес тела" or message.text == "вес" or message.text == "Вес":
        bot.send_message(message.chat.id, "P = mg\nВкикипедия: https://ru.wikipedia.org/wiki/Вес_тела")
    elif message.text == "давление" or message.text == "Давление":
        bot.send_message(message.chat.id, "p = F/S\nВкикипедия: https://ru.wikipedia.org/wiki/Давление")
    elif message.text == "давление в жидкости" or message.text == "Давление в жидкости":
        bot.send_message(message.chat.id, "P = pgh\nВкикипедия: Внутри жидкости в любой ее точке существует давление, обусловленное"\
        "весом верхних слоев жидкости на нижние. Если рассматривать жидкость в состоянии покоя, т.е. не двигающуюся, то это давление можно"\
        "назвать весовым  или гидростатическим давлением.")
    elif message.text == "площадь" or message.text == "Площадь":
        bot.send_message(message.chat.id, "S = ab\nВкикипедия: https://ru.wikipedia.org/wiki/Площадь")
    elif message.text == "Объем" or message.text == "объем" or message.text == "объём" or message.text == "Объём":
        bot.send_message(message.chat.id, "V = Sh\nВкикипедия: https://ru.wikipedia.org/wiki/Объем")
    elif message.text == "сила трения" or message.text == "Сила трения" or message.text == "трение" or message.text == "Трение":
        bot.send_message(message.chat.id, "F = yP\nВкикипедия: https://ru.wikipedia.org/wiki/Сила_трения")
    elif message.text == "работа" or message.text == "Работа":
        bot.send_message(message.chat.id, "A = Fs\nВкикипедия: Работа = сила × путь или A = Fs, где А - работа, F - сила и s - пройденный путь.")
    elif message.text == "мощность" or message.text == "Мощность":
        bot.send_message(message.chat.id, "N = A/t\nВкикипедия: https://ru.wikipedia.org/wiki/Мощность")
    elif message.text == "момент силы" or message.text == "Момент силы":
        bot.send_message(message.chat.id, "M = Fl\nВкикипедия: https://ru.wikipedia.org/wiki/Момент_силы")
    elif message.text == "Кинетическая энергия" or message.text == "кинетическая энергия":
        bot.send_message(message.chat.id, "E = mv**2 / 2\nВкикипедия: https://ru.wikipedia.org/wiki/Кинетическая_энергия")
    elif message.text == "Потенциальная энергия" or message.text == "потенциальная энергия":
        bot.send_message(message.chat.id, "E = mgh\nВкикипедия: https://ru.wikipedia.org/wiki/Потенциальная_энергия")
    elif message.text == "сила" or message.text == "Сила":
        bot.send_message(message.chat.id, "Какая сила? Может вот эти:\nсила тяжести,\nсила упругости,\nсила трения")
    elif message.text == "Архимед" or message.text == "архимед":
        bot.send_message(message.chat.id, "Архиме́д (Ἀρχιμήδης; 287 до н. э. — 212 до н. э.) — древнегреческий математик,\n физик и инженер из Сиракуз. Сделал множество открытий в геометрии.\n Заложил основы механики, гидростатики, был автором ряда важных изобретений.\nВикипедия: https://ru.wikipedia.org/wiki/Архимед")
    elif message.text == "Альберт" or message.text == "альберт" or message.text == "Эйнштейн, Альберт" or message.text == "Альберт Эйнштейн" or message.text == "альберт эйнштейн" or message.text == "эйнштейн, альберт":
        bot.send_message(message.chat.id, "Альбе́рт Эйнште́йн (нем. Albert Einstein, МФА [ˈalbɐt ˈaɪ̯nʃtaɪ̯n] (инф.)[C 1]; 14 марта 1879, Ульм, Вюртемберг,"\
            " Германия — 18 апреля 1955, Принстон, Нью-Джерси, США) — физик-теоретик, один из основателей современной"\
            " теоретической физики, лауреат Нобелевской премии по физике 1921 года, общественный деятель-гуманист. Жил в Германии (1879—1893, 1914—1933), Швейцарии (1893—1914) и США (1933—1955). Почётный доктор около 20 ведущих университетов мира, член многих Академий наук, в том числе иностранный почётный член АН СССР (1926).\nВикипедия: https://ru.wikipedia.org/wiki/Альберт_Эйнштейн")
    elif message.text == "Роберт Гук" or message.text == "роберт гук" or message.text == "Роберт гук" or message.text == "роберт Гук" or message.text == "Гук" or message.text == "гук":
        bot.send_message(message.chat.id, "Ро́берт Гук (англ. Robert Hooke; Роберт Хук, 18 (28) июля 1635, остров Уайт, Англия — 3 марта 1703, в Лондоне) — английский естествоиспытатель, учёный-энциклопедист. Гука смело можно назвать одним из отцов физики, в особенности экспериментальной, но и во многих других науках ему принадлежат зачастую одни из первых основополагающих работ и множество открытий.\nВикипедия: https://ru.wikipedia.org/wiki/Роберт_Гук")
    elif message.text == "Галилео Галилей" or message.text == "галилео галилей" or message.text == "Галилео галилей" or message.text == "галилео" or message.text == "Галилео" or message.text == "Галилей" or message.text == "галилей":
        bot.send_message(message.chat.id, "Галиле́о Галиле́й (итал. Galileo Galilei; 15 февраля 1564, Пиза — 8 января 1642, Арчетри) — итальянский физик, механик, астроном, философ, математик, оказавший значительное влияние на науку своего времени. Он первым использовал телескоп для наблюдения небесных тел[3] и сделал ряд выдающихся астрономических открытий.\nВикипедия: https://ru.wikipedia.org/wiki/Галилео_Галилей")
    elif message.text == "Блез Паскаль" or message.text == "блез паскаль" or message.text == "паскаль" or message.text == "Паскаль" or message.text == "Блез" or message.text == "блез":
        bot.send_message(message.chat.id, "Блез Паска́ль (фр. Blaise Pascal [blɛz pasˈkal]; 19 июня 1623, Клермон-Ферран, Франция — 19 августа 1662, Париж, Франция) — французский математик, механик, физик, литератор и философ. Классик французской литературы, один из основателей математического анализа, теории вероятностей и проективной геометрии, создатель первых образцов счётной техники, автор основного закона гидростатики.\nВикипедия: https://ru.wikipedia.org/wiki/Блез_Паскаль")
    elif message.text == "Масса" or message.text == "масса":
        bot.send_message(message.chat.id, "Ма́сса — физическая величина, определяющая инерционные и гравитационные свойства тела в ситуациях, когда его скорость много меньше скорости света[1].\nВикипедия: https://ru.wikipedia.org/wiki/Масса")
    elif message.text == "Никола Тесла" or message.text == "никола тесла" or message.text == "Никола тесла" or message.text == "никола Тесла" or message.text == "никола" or message.text == "Никола" or message.text == "тесла" or message.text == "Тесла":
        bot.send_message(message.chat.id, "Нико́ла Те́сла (серб. Ни́кола Те́сла, англ. Nikola Tesla; 10 июля 1856, Смилян, Австрийская империя, ныне в Хорватии — 7 января 1943, Нью-Йорк, США) — изобретатель в области электротехники и радиотехники сербского происхождения, инженер, физик. Родился и вырос в Австро-Венгрии, в последующие годы в основном работал во Франции и США. В 1891 году получил гражданство США[4].\nВикипедия: https://ru.wikipedia.org/wiki/Никола_Тесла")
    elif message.text == "Равномерное движение" or message.text == "равномерное движение":
        bot.send_message(message.chat.id, "l = vt\nВикипедия: https://ru.wikipedia.org/wiki/Равномерное_движение")
    else:
        bot.send_message(message.chat.id, "Я не понимаю тебя, может где-то ошибка")

@bot.message_handler(content_types=['sticker'])
def handle_text(message):
      text = ["не отправляй мне стикеры", "у тебя глупые стикеры", "я не сделан чтобы ты отправлял стикеры", "тебе очень повезло что стикеры в телеграмме бесплатные"]
      text2 = random.choice(text)

      bot.send_message(message.chat.id, text2)

@bot.message_handler(content_types=['emoji'])
def handle_text(message):
    emoji = [":)", ":(", "<3", ":o", ":|", ";)", "$)"]
    emoji2 = random.choice(text)
    bot.send_message(message.chat.id, emoji2)
    





bot.polling(none_stop=True, interval=0)


