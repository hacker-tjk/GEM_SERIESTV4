# main.py
import telebot
from config import TOKEN
from handlers import setup_handlers

def main():
    bot = telebot.TeleBot(TOKEN)

    user_messages = {}
    user_message_ids = {}

    setup_handlers(bot, user_messages, user_message_ids)

    # Добавьте эту строку, чтобы сбросить конфликт с вебхуком
    bot.remove_webhook()

    # Запуск бота
    print("Бот запущен...")
    bot.polling(none_stop=True)

if __name__ == "__main__":
    main()
