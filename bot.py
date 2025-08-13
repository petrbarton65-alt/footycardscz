import telebot
import os

TOKEN = os.getenv("TELEGRAM_TOKEN", "VLOZ_SVUJ_TOKEN_SEM")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Ahoj! Já jsem FootyCardscz bot. Pošli mi zprávu a odpovím.")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, f"Psal jsi: {message.text}")

if __name__ == "__main__":
    print("Bot běží...")
    bot.infinity_polling()
