import telebot
from config import TOKEN, keys
from extensions import error, CruptoConverter


bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, f"Приветствую, {message.chat.username}, \n узнать как пользоваться функцией бота: /help"
                                      f"\n узнать список доступных валют: /values")


@bot.message_handler(commands=['help'])
def help(message: telebot.types.Message):
    text= ('Чтобы воспользоваться функцией бота и превести валюту,нужно вводить команду в таком формате: \n<имя волюты>\
<в какую волюту переводить>\
<колл-во переводимой волюты>')
    bot.reply_to(message, text)

@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Все доступные валюты:'
    for key in keys.keys():
        text = "\n".join((text, key, ))
    bot.reply_to(message, text)



@bot.message_handler(content_types=['text', ])
def convert(message: telebot.types.Message):
    try:
        Errorhunt = message.text.split(' ')

        if len(Errorhunt) != 3:
            raise error('Слишком много символов.')

        quote, base, amount = Errorhunt
        total_base = CruptoConverter.convert(quote, base, amount)
    except error as e:
        bot.reply_to(message,f'Ошибка пользователя.\n{e}')



    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать команду\n{e}')
    else:
        text = f'Цена {amount} {quote} в {base} - {total_base}'
        bot.send_message(message.chat.id, text)


bot.polling()

