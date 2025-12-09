
import telebot
from telebot import apihelper

TOKEN = "8530548516:AAGolHePa16jWsDHxew4nibN9v0NW6YHFSs"
ADMINS = [1111111111, 8758469852]

# پراکسی SOCKS5
PROXY = "http://18.216.120.75:3000"
apihelper.proxy = {'https': PROXY}

bot = telebot.TeleBot(TOKEN)

print("Bot is running...")

bot.infinity_polling()
