from app.schemas import schemas
from app import models
from sqlalchemy.ext.asyncio import AsyncSession



class StockRepository:
    def __init__(self,db:AsyncSession):
        self.db = db

    def create_stock(self,stock: schemas.Stock):
        new_stock = models.Stock(symbol=stock.symbol)
        self.db.add(new_stock)
        self.db.commit()
        self.db.refresh(new_stock)
        return new_stock

    def create_stock_datapoint(self,data_point: schemas.DataPointBase,stock:schemas.Stock):
        new_datapoint = models.DataPoint(low_price=data_point.low_price,
                                      date=data_point.date,
                                      high_price=data_point.high_price,
                                      close_price=data_point.close_price,
                                      open_price=data_point.open_price,
                                      symbol=stock.symbol,
                                      stock_id=stock.id)
        self.db.add(new_datapoint)
        self.db.commit()
        self.db.refresh(new_datapoint)
        return new_datapoint

    def get_stock_by_symbol(self,stock_symbol:str):
        return self.db.query(models.Stock).filter(
            models.Stock.symbol == stock_symbol).first()

    def get_all_stocks(self):
        return self.db.query(models.Stock).all()


    def get_datapoint_by_symbol(self,stock_symbol:str):

        """Find stock_id first, then get all related data points"""
        stock = self.db.query(models.Stock).filter(models.Stock.symbol == stock_symbol).first()
        if not stock:
            return []  # No stock found

        return self.db.query(models.DataPoint).filter(models.DataPoint.stock_id == stock.id).all()
    def get_stocks(self):
        return self.db.query(models.Stock).all()


    def delete_all_stocks(self):
        self.db.query(models.DataPoint).delete()
        self.db.query(models.Stock).delete()
        self.db.commit()
        return self.db.query(models.Stock).all()

