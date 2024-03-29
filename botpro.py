from telegram.ext import Application, CommandHandler, CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from dotenv import load_dotenv
import os
import datetime
import asyncio

# возьмем переменные окружения из .env
load_dotenv()

# загружаем токен бота
TOKEN = os.environ.get("TOKEN")

# функция команды /start
async def start(update, context):

    # создаем список Inline кнопок
    keyboard = [[InlineKeyboardButton("Нажмите, чтобы получить информацию о себе", callback_data="1")]]
    
    # создаем Inline клавиатуру
    reply_markup = InlineKeyboardMarkup(keyboard)

    # прикрепляем клавиатуру к сообщению
    await update.message.reply_text('Получить информацию о себе', reply_markup=reply_markup)


# функция обработки нажатия на кнопки Inline клавиатуры
async def button(update, context):

    # параметры входящего запроса при нажатии на кнопку
    query = update.callback_query

    # отправка всплывающего уведомления
    await query.answer('Всплывающее уведомление!')
    
    user_id = query.from_user.id
    username = query.from_user.username
    first_name = query.from_user.first_name

    message = f'ID: {user_id}\nUsername: {username}\nFirst Name: {first_name}'
    await query.edit_message_text(text=message)

async def update_time(context, update):
    while True:
        now = datetime.datetime.now()
        time_str = now.strftime("Время %H:%M")
        
        # Используйте метод context.bot.edit_message_text для обновления текста в разделе "описание"
        await context.bot.edit_message_text(chat_id=update.effective_chat.id, message_id=update.message.message_id, text=time_str)
        
        # Приостанавливаем выполнение функции на 5 минут
        await asyncio.sleep(300)

def main():

    # точка входа в приложение
    application = Application.builder().token(TOKEN).build()
    print('Бот запущен...')

    # добавляем обработчик команды /start
    application.add_handler(CommandHandler("start", start))

    # добавляем обработчик нажатия на кнопку Inline клавиатуры
    application.add_handler(CallbackQueryHandler(button))


    # запуск приложения (для остановки нужно нажать Ctrl-C)
    application.run_polling()

if __name__ == "__main__":
    main()