from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

from config import TOKEN, ADMINS
from data import courses
from utils import get_categories, get_courses_by_category, get_course_by_id


# /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton(cat, callback_data=f"category_{cat}")]
        for cat in get_categories()
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    if update.message:
        await update.message.reply_text(
            "سلام! دسته‌بندی حوزه‌های برنامه‌نویسی:",
            reply_markup=reply_markup
        )


# Callback buttons
async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    data = query.data

    if data.startswith("category_"):
        category = data.replace("category_", "")

        keyboard = [
            [InlineKeyboardButton(course["name"],
             callback_data=f"course_{category}_{course['id']}")]
            for course in get_courses_by_category(category)
        ]

        await query.edit_message_text(
            f"دوره‌های {category}:",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

    elif data.startswith("course_"):
        _, category, course_id = data.split("_")
        course_id = int(course_id)

        course = get_course_by_id(category, course_id)
        if not course:
            await query.edit_message_text("دوره پیدا نشد.")
            return

        keyboard = [[
            InlineKeyboardButton("درخواست خرید",
            callback_data=f"buy_{category}_{course_id}")
        ]]

        await query.edit_message_text(
            f"دوره: {course['name']}\n"
            f"قیمت: {course['price']}$\n"
            f"توضیحات: {course['description']}",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

    elif data.startswith("buy_"):
        _, category, course_id = data.split("_")
        course_id = int(course_id)

        course = get_course_by_id(category, course_id)
        user = query.from_user

        for admin_id in ADMINS:
            await context.bot.send_message(
                chat_id=admin_id,
                text=(
                    f"درخواست خرید جدید:\n"
                    f"کاربر: {user.first_name}\n"
                    f"ID: {user.id}\n"
                    f"دوره: {course['name']}"
                )
            )

        await query.edit_message_text(
            "درخواست شما ثبت شد. ادمین‌ها به‌زودی با شما تماس می‌گیرند."
        )


def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button))

    print("Bot is running...")
    app.run_polling()


if __name__ == "__main__":
    main()
