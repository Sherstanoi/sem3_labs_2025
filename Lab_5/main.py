# import os
from telegram import Update, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes, CallbackQueryHandler

BOT_TOKEN = ('8243471811:AAFSPtx06Rpi-8VOaDLlYMKyY-RWrB_ku7o')

keyboard0 = [
    ["/start"]
]

keyboard1 = [
        ["любимый тип игр", "как жизнь?"],
        ["Закончить"]
    ]
keyboard2 = [
    ["хоррор", "шутер", "другое"]
]
keyboard3 = [
        ["квест", "РПГ", "другое2"],
    ]
keyboard4 = [
    ["новелла", "инди"]
]

inline_keyboard = [
    [InlineKeyboardButton("Хорошо", callback_data="хорошо")],
    [InlineKeyboardButton("Средне", callback_data="средне")],
    [InlineKeyboardButton("Плохо", callback_data="плохо")]
]

# global counter

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Простая клавиатура
    reply_markup = ReplyKeyboardMarkup(keyboard1, resize_keyboard=True)
    await update.message.reply_text(
        "Нажмите кнопку:",
        reply_markup=reply_markup
    )

async def handle_buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    if text == "любимый тип игр":
        await update.message.reply_text(
            "Ого-го! и какой же он?",
            reply_markup=ReplyKeyboardMarkup(keyboard2, resize_keyboard=True)
        )

    elif text == "хоррор":
        await update.message.reply_text("О! мне они тоже нравятся")
        await update.message.reply_text(
            "А так понял! давайте начнём заново",
            reply_markup=ReplyKeyboardMarkup(keyboard1, resize_keyboard=True)
        )

    if text == "шутер":
        await update.message.reply_text("Понимаю! Это популярный жанр")
        await update.message.reply_text(
            "А так понял! давайте начнём заново",
            reply_markup=ReplyKeyboardMarkup(keyboard1, resize_keyboard=True)
        )

    elif text == "другое":
        await update.message.reply_text(
            "окак",
            reply_markup=ReplyKeyboardMarkup(keyboard3, resize_keyboard=True)
        )

    elif text == "квест":
        await update.message.reply_text("Жесть! Далеко не всем такое нравится, клёво")
        await update.message.reply_text(
            "А так понял! давайте начнём заново",
            reply_markup=ReplyKeyboardMarkup(keyboard1, resize_keyboard=True)
        )

    if text == "РПГ":
        await update.message.reply_text("О-о, неизменная классика!")
        await update.message.reply_text(
            "А так понял! давайте начнём заново",
            reply_markup=ReplyKeyboardMarkup(keyboard1, resize_keyboard=True)
        )

    elif text == "другое2":
        await update.message.reply_text(
            "окак2",
            reply_markup=ReplyKeyboardMarkup(keyboard4, resize_keyboard=True)
        )

    elif text == "новелла":
        await update.message.reply_text("Понимаю1 Вове вот они тоже нравятся! Или вы и есть Вова?")
        await update.message.reply_text(
            "А так понял! давайте начнём заново",
            reply_markup=ReplyKeyboardMarkup(keyboard1, resize_keyboard=True)
        )

    if text == "инди":
        await update.message.reply_text("Жееесть, это очень разнообразный жанр!")
        await update.message.reply_text(
            "А так понял! давайте начнём заново",
            reply_markup=ReplyKeyboardMarkup(keyboard1, resize_keyboard=True)
        )

    elif text == "как жизнь?":
        await update.message.reply_text(
            "Как ваши дела?",
            reply_markup= InlineKeyboardMarkup(inline_keyboard)
        )

    elif text == "Закончить":
        await update.message.reply_text(
            "До свидания",
            reply_markup= ReplyKeyboardMarkup(keyboard0, resize_keyboard=True)
        )

    else:
        await update.message.reply_text("Используйте кнопки для навигации!")


async def inline_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    if query.data == "средне":
        await query.edit_message_text("Ой! воьмите яблоко")
    elif query.data == "хорошо":
        await query.edit_message_text("Это замечательно!! Надеюсь, ваше настроение сохранится и дальше")
    elif query.data == "плохо":
        await query.edit_message_text("Сочувствую, послушайте тогда анекдот: в семье пулемётчиков умер отец, для них это была большая утрататататата")


def main():
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT, handle_buttons))
    app.add_handler(CallbackQueryHandler(inline_handler))

    print("Бот запущен!")
    app.run_polling()


if __name__ == "__main__":
    main()