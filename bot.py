import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

# Вставьте сюда ваш токен, полученный от @BotFather
BOT_TOKEN = "8998825871:AAEY2If1o7RoMx7YYiCntUJ_nYai_1qTR10"
# Адрес сайта, который откроется по кнопке
SITE_URL = "https://athur.pythonanywhere.com/"

# Включаем логирование (полезно для отладки)
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Команда /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Создаём кнопку с URL
    keyboard = [
        [InlineKeyboardButton("🛒 Магазин", url=SITE_URL)]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # Отправляем сообщение с кнопкой
    await update.message.reply_text(
        "Добро пожаловать! Нажмите кнопку ниже, чтобы перейти в магазин:",
        reply_markup=reply_markup
    )

# Обработчик нажатий на inline-кнопки (если понадобится)
async def button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()  # Обязательно отвечаем на колбэк, чтобы убрать "часики"
    # Здесь можно добавить логику, если нужно что-то сделать при нажатии
    await query.edit_message_text("Спасибо за нажатие! Ссылка уже открыта.")

def main():
    # Создаём приложение
    application = Application.builder().token(BOT_TOKEN).build()

    # Регистрируем обработчики
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button_callback))

    # Запускаем бота
    print("Бот запущен...")
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main()