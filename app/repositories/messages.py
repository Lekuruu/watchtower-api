
from app.repositories.wrapper import session_wrapper
from app.database import DBMessage

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

@session_wrapper
async def by_id(message_id: int, session: AsyncSession = ...):
    return (
        await session.execute(
            select(DBMessage).where(DBMessage.id == message_id)
        )
    ).scalars().first()

@session_wrapper
async def by_sender(sender_id: int, session: AsyncSession = ...):
    return (
        await session.execute(
            select(DBMessage).where(DBMessage.sender_id == sender_id)
        )
    ).scalars().all()

@session_wrapper
async def by_target(target_name: str, session: AsyncSession = ...):
    return (
        await session.execute(
            select(DBMessage).where(DBMessage.target_name == target_name)
        )
    ).scalars().all()

@session_wrapper
async def recent(target_name: str, limit: int, offset: int = 0, session: AsyncSession = ...):
    return (
        await session.execute(
            select(DBMessage).order_by(DBMessage.id.desc())
                             .where(DBMessage.target_name == target_name)
                             .limit(limit)
                             .offset(offset)
        )
    ).scalars().all()
