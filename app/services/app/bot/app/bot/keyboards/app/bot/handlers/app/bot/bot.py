from aiogram import Bot, Dispatcher
from app.core.config import BOT_TOKEN
from app.bot.handlers import deal

bot = Bot(BOT_TOKEN, parse_mode="HTML")
dp = Dispatcher()
dp.include_router(deal.router)
