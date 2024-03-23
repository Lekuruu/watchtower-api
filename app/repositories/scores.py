
from app.repositories.wrapper import session_wrapper
from app.database import DBScore

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

@session_wrapper
async def by_id(score_id: int, session: AsyncSession = ...):
    return (
        await session.execute(
            select(DBScore).where(DBScore.id == score_id)
        )
    ).scalars().first()

@session_wrapper
async def by_user(user_id: int, server: str, session: AsyncSession = ...):
    return (
        await session.execute(
            select(DBScore).where(DBScore.user_id == user_id, DBScore.server == server)
        )
    ).scalars().all()

@session_wrapper
async def by_checksum(checksum: str, session: AsyncSession = ...):
    return (
        await session.execute(
            select(DBScore).where(DBScore.checksum == checksum)
        )
    ).scalars().first()

@session_wrapper
async def recent(limit: int, offset: int = 0, session: AsyncSession = ...):
    return (
        await session.execute(
            select(DBScore).order_by(DBScore.id.desc())
                           .limit(limit)
                           .offset(offset)
        )
    ).scalars().all()
