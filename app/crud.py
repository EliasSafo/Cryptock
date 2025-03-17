# from app import schemas
# from app import models
# from sqlalchemy.orm import Session
#
# #Too much code for a crud function
# def create_stock(db: Session, data_point: schemas.Stock):
#     stock = db.query(models.Stock).filter(
#         models.Stock.symbol == data_point.symbol).first()
#     if not stock:
#         db_stock = models.Stock(symbol=data_point.symbol)
#         db.add(db_stock)
#         db.commit()
#         db.refresh(db_stock)
#         stock = db_stock
#     new_data_point = models.DataPoint(low_price=data_point.low_price,
#                                       date=data_point.date,
#                                       high_price=data_point.high_price,
#                                       close_price=data_point.close_price,
#                                       open_price=data_point.open_price,
#                                       symbol=stock.symbol,
#                                       stock_id=stock.id)
#     db.add(new_data_point)
#     db.commit()
#     db.refresh(new_data_point)
#     return new_data_point
#
#
# def get_stocks(db: Session):
#     return db.query(models.Stock).all()
#
#
# def delete_all_stocks(db: Session):
#     db.query(models.Stock).delete()
#     db.commit()
