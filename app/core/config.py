from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "Stock Market API"
    VERSION: str = "1.0.0"
    DATABASE_URL: str = "postgresql+asyncpg://user:password@localhost/stock_db"
    ALLOWED_ORIGINS: list[str] = ["*"]  # CORS settings, change in production

    class Config:
        env_file = ".env"  # Load environment variables from `.env`

settings = Settings()
