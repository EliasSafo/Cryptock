import logging

from app.repositories.ApiBase import APIBase
from app.mock.stock_mock_data import mock_data_historical_top_100

class MockApiClient(APIBase):
    def get_100_biggest_stocks_history(self):

        return mock_data_historical_top_100.get("data", [])


# if __name__ == "__main__":
#     client = MockApiClient()
#     stocks_history = client.get_100_biggest_stocks_history()
#
#     # ✅ Print the first 5 stock histories
#     for stock in stocks_history[:5]:
#         print(stock)