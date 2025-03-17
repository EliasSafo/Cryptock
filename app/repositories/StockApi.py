
import requests
import os
from dotenv import load_dotenv

from app.repositories.ApiBase import APIBase
from app.mock.stock_mock_data import mock_data_historical, mock_data_top_100,mock_data_historical_top_100

class StockApiClient(APIBase):
    load_dotenv()
    load_dotenv(dotenv_path="/app/.env")
    API_KEY = os.getenv('STOCK_API_KEY')
    BASE_URL = "https://api.marketstack.com/v1"

    #

    def get_stock_history(self,symbol):

        querystring = {"symbols":"AAPL"}

        response = requests.get(self.url, params=querystring)
        response = mock_data_historical

    def get_100_biggest_stocks(self):


      # Fetch the top 100 most valuable companies
        params = {
            "access_key": self.API_KEY,
            "limit": 100,
            "sort": "DESC",
            "exchange": "XNAS"  # Optional: Get companies from NASDAQ (XNAS) or NYSE
            # (XNYS)
        }

        response = requests.get(f"{self.BASE_URL}/tickers", params=params)

        if response.status_code == 200:
            stocks_data = response.json().get("data", [])
            symbols = [stock["symbol"] for stock in stocks_data]  # Extract symbols
            return symbols
        else:
            print(f"Error {response.status_code}: {response.text}")
            return []

            return response


    def get_100_biggest_stocks_history(self):
        symbols = self.get_100_biggest_stocks()

        if not symbols:
            return "No symbols found."

        symbols_string = ",".join(symbols[:100])  # Max 100 symbols
        params = {
            "access_key": self.API_KEY,
            "symbols": symbols_string
        }

        response = requests.get(f"{self.BASE_URL}/eod", params=params)

        if response.status_code == 200:
            return response.json().get("data", [])
        else:
            print(f"Error {response.status_code}: {response.text}")
            return []
    # stocks=get_100_biggest_stocks_history()
    # for stock in stocks:
    #     print(stock)


