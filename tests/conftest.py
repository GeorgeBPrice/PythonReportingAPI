import asyncio
import pytest
from app.database import engine

@pytest.fixture(scope="function", autouse=True)
async def clean_db_connections():
    """
    Ensure all database connections are closed after each test.
    """
    yield
    await engine.dispose()
