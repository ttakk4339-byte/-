from dotenv import load_dotenv
import os

load_dotenv()

BOT_TOKEN = os.getenv("8594625847:AAF1Q-zrC-PUrV0ox2vtCl5uUkNVR1111Q4")
DATABASE_URL = os.getenv("DATABASE_URL=sqlite+aiosqlite:///./escrow.db")
ADMIN_PASSWORD = os.getenv("1133")
