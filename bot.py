from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes
from server import keep_alive
from config import TOKEN, ADMINS
from data import courses
from utils import get_categories, get_courses_by_category, get_course_by_id
keep_alive()
# پیام خوش آمد
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[InlineKeyboardButton(cat, callback_data=f"category_{cat}")] for cat in get_categories()]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("👋 سلام! دسته‌بندی حوزه‌های برنامه‌نویسی:", reply_markup=reply_markup)

# هندلر کال‌بک‌ها
async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    data = query.data

    if data.startswith("category_"):
        category = data.split("_")[1]
        keyboard = [[InlineKeyboardButton(course["name"], callback_data=f"course_{category}_{course['id']}")] 
                    for course in get_courses_by_category(category)]
        await query.edit_message_text(f"📚 دوره‌های {category}:", reply_markup=InlineKeyboardMarkup(keyboard))

    elif data.startswith("course_"):
        _, category, course_id = data.split("_")
        course_id = int(course_id)
        course = get_course_by_id(category, course_id)
        if course:
            keyboard = [[InlineKeyboardButton("💬 درخواست خرید", callback_data=f"buy_{category}_{course_id}")]]
            await query.edit_message_text(
                f"دوره: {course['name']}\n💲 قیمت: {course['price']}$\n📝 توضیحات: {course['description']}",
                reply_markup=InlineKeyboardMarkup(keyboard)
            )

    elif data.startswith("buy_"):
        _, category, course_id = data.split("_")
        course_id = int(course_id)
        course = get_course_by_id(category, course_id)
        user = update.callback_query.from_user
        for admin_id in ADMINS:
            await context.bot.send_message(
                chat_id=admin_id,
                text=f"کاربر {user.first_name} ({user.id}) درخواست خرید دوره '{course['name']}' را داده."
            )
        await query.edit_message_text("✅ درخواست شما ارسال شد. ادمین‌ها با شما تماس می‌گیرند.")


# اپلیکیشن اصلی
app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(button))

app.run_polling()
