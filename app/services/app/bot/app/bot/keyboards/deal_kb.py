from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def create_deal_kb(deal_id):
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(
            text="🤝 Accept Deal",
            callback_data=f"accept:{deal_id}"
        )]
    ])

def payment_kb(deal_id):
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(
            text="💳 Simulate Payment (DEMO)",
            callback_data=f"pay:{deal_id}"
        )]
    ])

def transfer_kb(deal_id):
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(
            text="📦 Confirm Item Transfer",
            callback_data=f"transfer:{deal_id}"
        )]
    ])
