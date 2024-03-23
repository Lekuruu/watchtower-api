
from app.database import session_generator, managed_session
from redis.asyncio import Redis

import config

__all__ = [
    'managed_session',
    'session_generator',
    'redis'
]

redis = Redis(
    host=config.REDIS_HOST,
    port=config.REDIS_PORT,
    password=config.REDIS_PASSWORD,
    db=config.REDIS_DB
)
