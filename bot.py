# bot.py
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes
from config import TOKEN, ADMINS
from utils import get_categories, get_courses_by_category, get_course_by_id
from data import courses

# =========================
# منو اصلی
# =========================
async def main_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton(cat, callback_data=f"category_{cat}")]
        for cat in get_categories()
    ]
    keyboard.append([InlineKeyboardButton("📦 دوره‌های رایگان", callback_data="free_courses")])
    keyboard.append([InlineKeyboardButton("📞 تماس با ادمین", callback_data="contact_admin")])
    reply_markup = InlineKeyboardMarkup(keyboard)

    if update.message:
        await update.message.reply_text("👋 سلام! منوی اصلی AMIRSAMDERAKHSHAN:", reply_markup=reply_markup)
    elif update.callback_query:
        await update.callback_query.edit_message_text("👋 منوی اصلی AMIRSAMDERAKHSHAN:", reply_markup=reply_markup)

# =========================
# Callback Handler
# =========================
async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    data = query.data

    if data.startswith("category_"):
        category = data.replace("category_", "")
        keyboard = [
            [InlineKeyboardButton(course["name"], callback_data=f"course_{category}_{course['id']}")]
            for course in get_courses_by_category(category)
        ]
        keyboard.append([InlineKeyboardButton("🏠 منوی اصلی", callback_data="main_menu")])
        await query.edit_message_text(f"📚 دوره‌های {category}:", reply_markup=InlineKeyboardMarkup(keyboard))

    elif data.startswith("course_"):
        _, category, course_id = data.split("_")
        course_id = int(course_id)
        course = get_course_by_id(category, course_id)
        if not course:
            await query.edit_message_text("❌ دوره پیدا نشد.")
            return
        keyboard = [
            [InlineKeyboardButton("💬 درخواست خرید", callback_data=f"buy_{category}_{course_id}")],
            [InlineKeyboardButton("⬅️ بازگشت به دسته‌بندی", callback_data=f"category_{category}")],
            [InlineKeyboardButton("🏠 منوی اصلی", callback_data="main_menu")]
        ]
        await query.edit_message_text(
            f"📝 دوره: {course['name']}\n"
            f"💲 قیمت: {course['price']}$\n"
            f"📄 توضیحات: {course['description']}",
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
                text=f"کاربر {user.first_name} ({user.id}) درخواست خرید دوره '{course['name']}' داده."
            )

        await query.edit_message_text(
            "✅ درخواست شما ثبت شد. ادمین‌ها به‌زودی با شما تماس می‌گیرند."
        )

    elif data == "free_courses":
        free_courses = []
        for cat in get_categories():
            for c in get_courses_by_category(cat):
                if c.get("price") == 0:
                    free_courses.append((cat, c))
        if not free_courses:
            await query.edit_message_text("❌ دوره رایگان موجود نیست.")
            return
        keyboard = [[InlineKeyboardButton(c["name"], callback_data=f"course_{cat}_{c['id']}")] for cat, c in free_courses]
        keyboard.append([InlineKeyboardButton("🏠 منوی اصلی", callback_data="main_menu")])
        await query.edit_message_text("📚 دوره‌های رایگان:", reply_markup=InlineKeyboardMarkup(keyboard))

    elif data == "contact_admin":
        await query.edit_message_text("📞 لطفا با ادمین‌ها تماس بگیرید. شناسه سازنده: AMIRSAMDERAKHSHAN")

    elif data == "main_menu":
        await main_menu(update, context)

# =========================
# شروع بات
# =========================
def main():
    app = ApplicationBuilder().token(TOKEN).build()
    # نمایش منوی اصلی خودکار با دستور start
    app.add_handler(CommandHandler("start", main_menu))
    app.add_handler(CallbackQueryHandler(button))

    print("Bot is running... AMIRSAMDERAKHSHAN")
    app.run_polling()


if __name__ == "__main__":
    main()
