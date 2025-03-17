import os

from fastapi import APIRouter, Depends, FastAPI, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
import logging

from app.repositories import ApiBase
from app.repositories.stock_repository import StockRepository
from app.repositories.ApiBase import APIBase
from app.repositories.MockApi import MockApiClient
from app.repositories.StockApi import StockApiClient
from app.services.stock_services import StockService
from app.dependencies import get_stock_service
from fastapi.responses import JSONResponse
from app import crud
from app.models import Base
from app.schemas import schemas
from app.db.database import SessionLocal, engine
from dotenv import load_dotenv


load_dotenv()
load_dotenv(dotenv_path="/app/.env")
use_mock_api = os.getenv('USE_MOCK_API', "false").lower() == "true"
app = FastAPI()
Base.metadata.create_all(bind=engine)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.StreamHandler()
    ],
)
logger = logging.getLogger(__name__)

router = APIRouter()
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()
#
#
# def get_api_client() -> APIBase:
#
#     logger.info(f"use mock api = {use_mock_api}")
#
#     client = MockApiClient() if use_mock_api else StockApiClient()
#     logger.info(f"Using API client: {client.__class__.__name__}")
#     return client


@router.post("/stock", response_model=schemas.DataPointBase)
def create_datapoint(stock_datapoint: schemas.DataPointBase, stock_service:StockService = Depends(get_stock_service)):
    try:
        return stock_service.create_stock_datapoint(stock_datapoint)
    except Exception as e:
        raise HTTPException(f"Failed to create stock. Error: {e}")


@router.get("/stocks/")
def get_stocks(stock_service:StockService = Depends(get_stock_service)):
    return stock_service.get_all_stocks()

@router.get("/datapoints/")
def get_datapoints(stock_symbol:str, stock_service:StockService = Depends(get_stock_service)):
    return stock_service.get_datapoints_by_symbol(stock_symbol)

@router.delete("/stocks/")
def delete_stocks(stock_service:StockService = Depends(get_stock_service)):
    return stock_service.delete_all_stocks()


#


# @app.post("/stocks/")
# async def update_stocks(db: Session = Depends(get_db), APIBase=Depends(get_api_client)):
#     try:
#         logger.info(f"Using API client: {ApiBase.__class__.__name__}")
#         stocks = APIBase.get_100_biggest_stocks_history()
#         for stock in stocks:
#             crud.create_stock(db, stock)
#         return JSONResponse(
#             content={"message": f"Stored {len(stocks)} stocks successfully"},
#             status_code=200)
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=f"Failed to get stocks. Error: {e}")
#
#

#
# @app.delete("/stocks/")
# def delete_stocks(db: Session = Depends(get_db)):
#     crud.delete_all_stocks(db)
#     return JSONResponse(
#         content={"message": f"deleted all stocks successfully"},
#         status_code=200)
