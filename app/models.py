# from app.database import Base
# from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
# from sqlalchemy.orm import relationship
#
# class Stock(Base):
#
#     __tablename__ = 'stocks'
#
#     id = Column(Integer, primary_key=True)
#     symbol = Column(String, unique=True, index=True)
#
#
#
#
# class DataPoint(Base):
#     __tablename__ = 'data_points'
#
#     id = Column(Integer, primary_key=True)
#     date = Column(DateTime, index=True)
#     open_price = Column(Float)
#     high_price = Column(Float)
#     low_price = Column(Float)
#     close_price = Column(Float)
#     symbol = Column(String, unique=False, index=True)
#     stock_id = Column(Integer, ForeignKey('stocks.id'))
