import pytest
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.sql import text  # Import text to wrap raw SQL
from app.database import DATABASE_URL
from app.models.asset_models import Base

@pytest.mark.asyncio
async def test_database_connection():
    # Create a temporary database engine
    engine = create_async_engine(DATABASE_URL, echo=True)
    
    try:
        # Test schema creation
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)

        # Test basic query execution
        async with AsyncSession(engine) as session:
            result = await session.execute(text("SELECT 1"))
            assert result.scalar() == 1  # Assuming the query returns 1 result
    finally:
        await engine.dispose()
