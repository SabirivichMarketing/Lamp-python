import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import mysql.connector
from config import TELEGRAM_TOKEN, DB_CONFIG

# Настройка логирования
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Привет! Я Telegram бот в Docker контейнере!')

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    
    # Сохранение сообщения в базу данных
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO messages (user_id, message) VALUES (%s, %s)",
            (update.effective_user.id, user_message)
        )
        conn.commit()
        cursor.close()
        conn.close()
    except Exception as e:
        logging.error(f"Database error: {e}")
    
    await update.message.reply_text(f'Вы сказали: {user_message}')

def main():
    # Создание приложения
    application = Application.builder().token(TELEGRAM_TOKEN).build()

    # Добавление обработчиков
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # Запуск бота
    application.run_polling()

if __name__ == '__main__':
    main()