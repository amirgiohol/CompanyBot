import asyncio
from aiogram import Bot, Dispatcher
from app.config import get_bot_token
from app.handlers import start

async def main():
    bot = Bot(token=get_bot_token())
    dp = Dispatcher()
    dp.include_router(start.router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
