
from redis.asyncio import Redis

import config

redis = Redis(
    host=config.REDIS_HOST,
    port=config.REDIS_PORT,
    password=config.REDIS_PASSWORD,
    db=config.REDIS_DB
)
