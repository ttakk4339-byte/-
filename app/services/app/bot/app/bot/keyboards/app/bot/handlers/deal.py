from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from app.services.deal_service import DealService
from app.bot.keyboards.deal_kb import create_deal_kb, payment_kb, transfer_kb
from app.bot.ui import deal_card

router = Router()

@router.message(F.text == "/deal")
async def create_deal(message: Message):
    deal = await DealService.create(message.from_user.id)
    await message.answer(
        deal_card("created"),
        reply_markup=create_deal_kb(deal.id),
        parse_mode="HTML"
    )

@router.callback_query(F.data.startswith("accept"))
async def accept(callback: CallbackQuery):
    deal_id = int(callback.data.split(":")[1])
    await DealService.join(deal_id, callback.from_user.id)
    await callback.message.edit_text(
        deal_card("accepted"),
        reply_markup=payment_kb(deal_id),
        parse_mode="HTML"
    )

@router.callback_query(F.data.startswith("pay"))
async def pay(callback: CallbackQuery):
    deal_id = int(callback.data.split(":")[1])
    await DealService.update_status(deal_id, "paid")
    await callback.message.edit_text(
        deal_card("paid") + "\n\n✅ Demo payment confirmed",
        reply_markup=transfer_kb(deal_id),
        parse_mode="HTML"
    )

@router.callback_query(F.data.startswith("transfer"))
async def transfer(callback: CallbackQuery):
    deal_id = int(callback.data.split(":")[1])
    await DealService.update_status(deal_id, "completed")
    await callback.message.edit_text(
        deal_card("completed") + "\n\n🎉 Deal completed (DEMO)",
        parse_mode="HTML"
    )
