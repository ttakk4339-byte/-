from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from sqlalchemy import select
from app.core.database import SessionLocal
from app.models.deal import Deal
from fastapi.templating import Jinja2Templates

app = FastAPI(title="Escrow Demo Admin")
templates = Jinja2Templates(directory="app/admin/templates")

@app.get("/", response_class=HTMLResponse)
async def dashboard(request: Request):
    async with SessionLocal() as session:
        result = await session.execute(select(Deal))
        deals = result.scalars().all()
    return templates.TemplateResponse(
        "dashboard.html",
        {"request": request, "deals": deals}
    )
