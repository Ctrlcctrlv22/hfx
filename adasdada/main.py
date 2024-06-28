import telebot
import random
API_TOKEN = '7493949165:AAHTnAjvP11BXORZrMSwT8G5KKKbSlArNNU'

bot = telebot.TeleBot(API_TOKEN, parse_mode='HTML')

@bot.message_handler(commands= ["start"])
def send_welcome(message):
    bot.reply_to(message, "<b>Добро</b> пожаловать c🥵🥵🥵🥵!")

@bot.message_handler(commands= ["info"])
def send_welcome(message):
    bot.reply_to(message, "so eshh")

@bot.message_handler(commands= ["help"])
def send_welcome(message):
    help_text = (
        "<b>Доступные команды:</b>\n"
        "/start - запуск бота😈😈😈😈\n"
        "/info - список команд бота😈😈😈😈\n"
    )
    bot.reply_to(message, help_text)

#@bot.message_handler()
#def handle_unknown_command(message):
#    response = "<b> такой команды нет🥵🥵🥵🥵🥵🥵</b>"
#    bot.reply_to(message, response)
@bot.message_handler(commands=['rad'])
def send_hoip(message):
    try:
        random_index = random.randint(0,6)
        image_path = f"./img/image{random_index}.jpg"
        with open(image_path, 'rb') as image_file:
            bot.send_photo(message.chat.id, image_file)
    except Exception as e:
        bot.reply_to(message, f"Произошла ошибке: {e}")

@bot.message_handler()
def handle_unknown_command(message):
    response = "<b>o чём ты🥵🥵🥵🥵🥵🥵</b>"
    bot.reply_to(message, response)

bot.polling(none_stop=True)