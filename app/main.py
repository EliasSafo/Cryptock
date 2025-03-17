from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes import stocks
from app.db.database import engine

from app.core.config import settings

# Initialize FastAPI app
app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    description="FastAPI project using Layered Architecture",
)

# Middleware (CORS, Logging, etc.)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register API routes
app.include_router(stocks.router, prefix="/api/v1/stocks", tags=["Stocks"])

# Database Initialization
@app.on_event("startup")
async def startup():
    print("Application is starting...")  # Add DB connection or cache setup here

@app.on_event("shutdown")
async def shutdown():
    print("Application is shutting down...")  # Cleanup tasks here

# Root route (Health Check)
@app.get("/")
async def root():
    return {"message": "FastAPI Layered Architecture is running 🚀"}
