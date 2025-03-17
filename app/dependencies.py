from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.repositories.stock_repository import StockRepository
from app.services.stock_services import StockService

def get_stock_service(db: Session = Depends(get_db)):

    stock_repo = StockRepository(db)
    return StockService(stock_repo)
