
import app.session as session

async def submit_event(name: str, *args, **kwargs):
    await session.redis.publish(
        'api', str((name, args, kwargs))
    )

async def request_stats(server: str, id: int):
    await submit_event(
        'stats_request', server, id
    )
