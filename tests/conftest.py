# import pytest
# from fastapi.testclient import TestClient
# from app.main import app
#
# @pytest.fixture(scope="function")
# def client():
#     return TestClient(app)
#
# def override_get_db():
#     """Returns None to prevent DB connection in tests."""
#     return None
#
# app.dependency_overrides = {"get_db": override_get_db}
