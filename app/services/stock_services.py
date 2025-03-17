from app.schemas import schemas
from app import models
from sqlalchemy.orm import Session
from app.repositories.stock_repository import StockRepository

#Too much code for a crud function

class StockService:
    def __init__(self,stock_repo:StockRepository):
        self.stock_repo =stock_repo


    def create_stock_datapoint(self, data_point: schemas.DataPointBase):
        stock = self.stock_repo.get_stock_by_symbol(data_point.symbol)
        if not stock:
            stock =self.stock_repo.create_stock(data_point)

        new_data_point = self.stock_repo.create_stock_datapoint(stock=stock, data_point=data_point)

        return new_data_point

    def get_stock_by_symbol(self,symbol:str):
        return self.stock_repo.get_stock_by_symbol(symbol)

    def get_all_stocks(self):
        return self.stock_repo.get_all_stocks()
    def get_datapoints_by_symbol(self,symbol:str):
        return self.stock_repo.get_datapoint_by_symbol(symbol)

    def delete_all_stocks(self):
        return self.stock_repo.delete_all_stocks()