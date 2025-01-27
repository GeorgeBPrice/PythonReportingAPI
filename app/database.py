import os
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# grab the connection string (store in KeyVault in prod) 
DATABASE_URL = os.getenv("DATABASE_URL")

# Set up the database engine for async operations
engine = create_async_engine(DATABASE_URL, future=True, echo=True)

# Use async_sessionmaker for async sessions
SessionLocal = async_sessionmaker(
    bind=engine,
    expire_on_commit=False,
)