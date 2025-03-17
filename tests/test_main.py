from fastapi.testclient import TestClient
from app.main import app

import pytest
from datetime import datetime
from app.schemas import Stock

client = TestClient(app)


# @pytest.fixture
# def mock_stock():
#     return Stock(
#         date=datetime(2024, 1, 1, 10, 0, 0),
#         symbol="FAKE",
#         open_price=100.0,
#         high_price=110.0,
#         low_price=95.0,
#         close_price=105.0,
#     )


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}

def test_create_stock():
    stock_data= {
  "date": "2025-02-25T09:39:08.264Z",
  "symbol": "string",
  "open_price": 0,
  "high_price": 0,
  "low_price": 0,
  "close_price": 0
}


    response = client.post("/stock",json=stock_data)
    assert response.status_code == 200
    # assert response.json() == mock_stock()