from app.models.deal import Deal
from app.core.database import SessionLocal

class DealService:

    @staticmethod
    async def create(user_id: int):
        async with SessionLocal() as session:
            deal = Deal(creator_id=user_id)
            session.add(deal)
            await session.commit()
            await session.refresh(deal)
            return deal

    @staticmethod
    async def join(deal_id: int, user_id: int):
        async with SessionLocal() as session:
            deal = await session.get(Deal, deal_id)
            deal.partner_id = user_id
            deal.status = "accepted"
            await session.commit()
            return deal

    @staticmethod
    async def update_status(deal_id: int, status: str):
        async with SessionLocal() as session:
            deal = await session.get(Deal, deal_id)
            deal.status = status
            await session.commit()
            return deal

    @staticmethod
    async def get(deal_id: int):
        async with SessionLocal() as session:
            return await session.get(Deal, deal_id)
