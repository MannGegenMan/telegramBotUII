from telegram.ext import Application, CommandHandler, MessageHandler, filters, Updater
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Message, ReplyKeyboardMarkup, ReplyKeyboardRemove
from dotenv import load_dotenv
import os
import asyncio


# возьмем переменные окружения из .env
load_dotenv()

# загружаем токен бота
TOKEN = os.environ.get("TOKEN")


# функция команды /start
async def start(update, context):
    await update.message.reply_text('Первая задача выполнена')

# функция команды /warcraft
async def warcraft(update, context):
    keyboard = [[InlineKeyboardButton('Альянс', callback_data='1'),
                 InlineKeyboardButton('Орда', callback_data='2')]]
    
    reply_markup = InlineKeyboardMarkup(keyboard)

    message = await update.message.reply_text('Выберите сторону', reply_markup=reply_markup)

    # Удаление сообщения с кнопками после их нажатия
    await asyncio.sleep(5)  # Ждем 5 секунд (можно изменить время)
    await context.bot.delete_message(chat_id=update.effective_chat.id, message_id=message.message_id)



# функция обработки команд
async def command_handler(update, context):
    command = context.args[0] # получаем переданный параметр команды

    if command == 'start':
        await start(update, context)
    elif command == 'warcraft':
        await warcraft(update, context)
    else:
        await update.message.reply_text('Неизвестная команда')

# функция для текстовых сообщений
async def text(update, context):
    message = update.message.text
    char_count = len(message)
    await update.message.reply_text(f"Количество символов: {char_count}")

# функция для изображений
async def image(update, context):
    await update.message.reply_text('Эй! Мы получили от тебя фотографию!')

# Получение id голосового сообщения
async def voice(update, context):
    voice_id = update.message.voice.file_id
    await update.message.reply_text(f'ID вашего голосового сообщения: {voice_id}')


def main():

    # точка входа в приложение
    application = Application.builder().token(TOKEN).build()
    print('Бот запущен...')

    # добавляем обработчик команды /start
    application.add_handler(CommandHandler("start", start))

    # добавлем обработчик команды /warcraft
    application.add_handler(CommandHandler('warcraft', warcraft))

    # добавляем обработчик текстовых сообщений
    application.add_handler(MessageHandler(filters.TEXT, text))

    # добавляем обработчик сообщений с изображениями
    application.add_handler(MessageHandler(filters.PHOTO, image))

    # добавляем обработчик голосовых сообщений
    application.add_handler(MessageHandler(filters.VOICE, voice))

    # запуск приложения (для остановки нужно нажать Ctrl-C)
    application.run_polling()


if __name__ == "__main__":
    main()