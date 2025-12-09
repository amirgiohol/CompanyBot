# bot.py
import telebot
from config import TOKEN, ADMINS
from courses import categories
from admin import send_to_admins

bot = telebot.TeleBot(TOKEN)

# ---------- START ----------
@bot.message_handler(commands=['start'])
def send_welcome(message):
    text = "سلام! من ربات فروش دوره‌های برنامه‌نویسی هستم.\nلطفا یک دسته انتخاب کنید:"
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    for category in categories.keys():
        markup.add(category)
    bot.send_message(message.chat.id, text, reply_markup=markup)

# ---------- دسته‌بندی ----------
@bot.message_handler(func=lambda m: m.text in categories.keys())
def show_courses(message):
    cat = message.text
    markup = telebot.types.InlineKeyboardMarkup()
    for course in categories[cat]:
        btn = telebot.types.InlineKeyboardButton(
            text=course["name"], callback_data=f"buy_{cat}_{course['name']}"
        )
        markup.add(btn)
    bot.send_message(message.chat.id, f"دوره‌های {cat}:", reply_markup=markup)

# ---------- خرید دوره ----------
@bot.callback_query_handler(func=lambda call: call.data.startswith("buy_"))
def buy_course(call):
    parts = call.data.split("_")
    category = parts[1]
    course_name = "_".join(parts[2:])
    
    # پیام به ادمین
    msg = f"کاربر @{call.from_user.username} ({call.from_user.id}) درخواست خرید داده:\nدوره: {course_name}\nدسته: {category}"
    send_to_admins(bot, msg)
    
    bot.answer_callback_query(call.id, "درخواست شما ثبت شد. ادمین با شما تماس می‌گیرد.")
    bot.send_message(call.from_user.id, "درخواست شما ثبت شد. لطفا منتظر پیام ادمین باشید.")

# ---------- پیام‌های دیگر ----------
@bot.message_handler(func=lambda m: True)
def default_msg(message):
    bot.send_message(message.chat.id, "لطفا یکی از دسته‌ها را انتخاب کنید یا /start را بزنید.")

# ---------- اجرای ربات ----------
if __name__ == "__main__":
    print("Bot is running...")
    bot.infinity_polling()
