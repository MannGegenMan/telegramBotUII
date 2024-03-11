import os
import asyncio
from dotenv import load_dotenv
from telegram.ext import Application, CommandHandler


# возьмем переменные окружения из .env
load_dotenv()

# загружаем токен бота
TOKEN = os.environ.get("TOKEN")


# функция команды /start
async def start(update, context):
    await asyncio.sleep(5)
    await update.message.reply_text('Первая проверка')

# функция команды /help
async def help(update, context):
    # await asyncio.sleep(5)
    await update.message.reply_text('Вторая проверка')


def main():

    # точка входа в приложение
    application = Application.builder().token(TOKEN).build()
    print('Бот запущен...')

    # добавляем обработчик команды /start
    application.add_handler(CommandHandler("start", start, block=False))

    # добавляем обработчик команды /help
    application.add_handler(CommandHandler("help", help, block=False))

    # запуск приложения (для остановки нужно нажать Ctrl-C)
    application.run_polling()


if __name__ == "__main__":
    main()