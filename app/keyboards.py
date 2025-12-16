from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

main_menu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="📚 دوره‌ها", callback_data="courses")],
    [InlineKeyboardButton(text="💬 پشتیبانی", callback_data="support")],
    [InlineKeyboardButton(text="👤 حساب کاربری", callback_data="profile")]
])
