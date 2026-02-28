import asyncio
from app.bot.bot import dp, bot
from app.admin.main import app
from app.core.database import engine, Base
import uvicorn

async def start_bot():
    await dp.start_polling(bot)

async def create_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

async def main():
    await create_db()
    asyncio.create_task(start_bot())
    config = uvicorn.Config(app, host="0.0.0.0", port=8000)
    server = uvicorn.Server(config)
    await server.serve()

asyncio.run(main())
