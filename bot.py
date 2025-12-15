from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    ReplyKeyboardMarkup,
    KeyboardButton
)
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    CallbackQueryHandler,
    MessageHandler,
    ContextTypes,
    filters
)

from config import TOKEN, ADMINS, CREATOR_NAME
from utils import (
    get_categories,
    get_courses_by_category,
    get_course_by_id,
    get_free_courses
)

# =========================
# منوی پایین چت (ثابت)
# =========================
MAIN_MENU = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton("📚 دسته‌بندی دوره‌ها")],
        [KeyboardButton("🎁 دوره‌های رایگان"), KeyboardButton("📞 تماس با ادمین")]
    ],
    resize_keyboard=True
)

# =========================
# START
# =========================
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        f"👋 خوش آمدی!\n\n"
        f"🎓 فروشگاه دوره‌های آموزشی\n"
        f"🛠 سازنده: {CREATOR_NAME}\n\n"
        f"از منوی پایین استفاده کن 👇",
        reply_markup=MAIN_MENU
    )

# =========================
# پیام‌های منوی پایین
# =========================
async def on_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "📚 دسته‌بندی دوره‌ها":
        keyboard = [
            [InlineKeyboardButton(cat, callback_data=f"category_{cat}")]
            for cat in get_categories()
        ]
        await update.message.reply_text(
            "📂 یک دسته‌بندی انتخاب کن:",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

    elif text == "🎁 دوره‌های رایگان":
        free_courses = get_free_courses()
        if not free_courses:
            await update.message.reply_text("❌ دوره رایگان موجود نیست.")
            return

        keyboard = [
            [InlineKeyboardButton(course["name"], callback_data=f"course_{cat}_{course['id']}")]
            for cat, course in free_courses
        ]

        await update.message.reply_text(
            "🎁 دوره‌های رایگان:",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

    elif text == "📞 تماس با ادمین":
        await update.message.reply_text(
            f"📞 برای خرید یا پشتیبانی با ادمین تماس بگیرید\n\n"
            f"🛠 سازنده بات: {CREATOR_NAME}"
        )

# =========================
# Inline buttons
# =========================
async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    data = query.data

    if data.startswith("category_"):
        category = data.replace("category_", "")
        keyboard = [
            [InlineKeyboardButton(c["name"], callback_data=f"course_{category}_{c['id']}")]
            for c in get_courses_by_category(category)
        ]
        keyboard.append([InlineKeyboardButton("🏠 منوی اصلی", callback_data="home")])

        await query.edit_message_text(
            f"📚 دوره‌های {category}:",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

    elif data.startswith("course_"):
        _, category, course_id = data.split("_")
        course_id = int(course_id)
        course = get_course_by_id(category, course_id)

        if not course:
            await query.edit_message_text("❌ دوره پیدا نشد")
            return

        keyboard = [
            [InlineKeyboardButton("💬 درخواست خرید", callback_data=f"buy_{category}_{course_id}")],
            [InlineKeyboardButton("⬅️ بازگشت", callback_data=f"category_{category}")]
        ]

        await query.edit_message_text(
            f"📘 {course['name']}\n\n"
            f"💰 قیمت: {course['price']}$\n"
            f"📝 توضیحات:\n{course['description']}\n\n"
            f"🛠 سازنده: {CREATOR_NAME}",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

    elif data.startswith("buy_"):
        _, category, course_id = data.split("_")
        course_id = int(course_id)
        course = get_course_by_id(category, course_id)
        user = query.from_user

        for admin in ADMINS:
            await context.bot.send_message(
                admin,
                f"📥 درخواست خرید جدید\n\n"
                f"👤 کاربر: {user.first_name}\n"
                f"🆔 {user.id}\n"
                f"📘 دوره: {course['name']}"
            )

        await query.edit_message_text(
            "✅ درخواست شما ثبت شد\n"
            "ادمین به‌زودی با شما تماس می‌گیرد"
        )

    elif data == "home":
        await query.message.reply_text(
            "🏠 منوی اصلی",
            reply_markup=MAIN_MENU
        )

# =========================
# RUN
# =========================
def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, on_message))
    app.add_handler(CallbackQueryHandler(button))

    print(f"Bot running | Creator: {CREATOR_NAME}")
    app.run_polling()

if __name__ == "__main__":
    main()
