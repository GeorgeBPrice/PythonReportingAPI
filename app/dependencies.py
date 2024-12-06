from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import SessionLocal

async def get_db() -> AsyncGenerator[AsyncSession, None]:
    """
    Dependency to provide a database session.
    """
    async with SessionLocal() as session:
        try:
            yield session
        finally:
            await session.close()