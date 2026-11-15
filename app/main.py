import logging
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from fastapi import FastAPI
from sqlalchemy import text
from app.db.database import engine
from app.routers import admin, staff, category, sub_category, cabinet, level, file, transaction, auth

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("db_logger")

# test database connection
@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Checking MySQL database connection...")
    try:
        with engine.connect() as connection:
            result = connection.execute(text("SELECT 1"))
            result.fetchone()
        logger.info("Successfully connected to the MySQL database!")
    except Exception as e:
        logger.error(f"Database connection failed: {e}")
    yield


app = FastAPI()

# enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# test api response
@app.get("/")
async def root():
    return {"message": "Ping pong!"}

app.include_router(admin.router)
app.include_router(staff.router)
app.include_router(category.router)
app.include_router(sub_category.router)
app.include_router(cabinet.router)
app.include_router(level.router)
app.include_router(file.router)
app.include_router(transaction.router)

app.include_router(
    auth.router,
    prefix="/api/auth",
    tags=["Authentication"]
)
