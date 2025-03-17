import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


TESTING = os.getenv("TESTING", "false").lower() == "true"

if TESTING:
    SQLALCHEMY_DATABASE_URL = os.getenv("TEST_DATABASE_URL", "sqlite:///./test.db")
else:
    db_host = os.getenv("DB_HOST", "localhost")
    SQLALCHEMY_DATABASE_URL = f"postgresql+psycopg2://elias:secret_123@{db_host}:5432/Cryptock"

engine = create_engine(SQLALCHEMY_DATABASE_URL, future=True, echo=True)

SessionLocal = sessionmaker(
    bind=engine,
    autocommit=False,
    autoflush=False,
)


Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
