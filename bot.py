import telebot
from bot_logic import plastic_craft

bot = telebot.TeleBot("TOKEN")

# Команда /start
@bot.message_handler(commands=["start"])
def send_start(message):
    bot.reply_to(message, f'Привет, я {bot.get_me().first_name}. Список команд: /start')

@bot.message_handler(commands=['plastic_crafts'])
def send_plastic_crafts(message):
    bot.reply_to(message, '')


bot.polling()