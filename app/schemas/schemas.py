from pydantic import BaseModel
from datetime import date, datetime


class Stock(BaseModel):
    symbol: str


class DataPointBase(Stock):
    date: datetime
    open_price: float
    high_price: float
    low_price: float
    close_price: float

