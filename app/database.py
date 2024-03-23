
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import sessionmaker

from contextlib import asynccontextmanager
from app.objects import DBScore, DBMessage

import config

engine = create_async_engine(
    f'postgresql+asyncpg://{config.POSTGRES_USER}:{config.POSTGRES_PASSWORD}@{config.POSTGRES_HOST}/{config.POSTGRES_DB}'
)

session_generator = sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False
)

@asynccontextmanager
async def managed_session():
    try:
        async with session_generator() as session:
            yield session
    except:
        await session.rollback()
        raise
    finally:
        await session.close()
