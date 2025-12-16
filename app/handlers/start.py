from aiogram import Router
from aiogram.types import Message
from keyboards import main_menu

router = Router()

@router.message(commands=["start"])
async def start_handler(message: Message):
    await message.answer(
        "به سامانه آموزشی برنامه‌نویسی خوش آمدید.\n"
        "دوره‌های تخصصی برای ورود حرفه‌ای به بازار کار.",
        reply_markup=main_menu
    )
