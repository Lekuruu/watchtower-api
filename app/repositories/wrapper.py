
from sqlalchemy.ext.asyncio import AsyncSession
from functools import wraps

import app.session

def session_wrapper(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        if kwargs.get('session'):
            # Use existing session
            return await func(*args, **kwargs)

        if args and isinstance(args[-1], AsyncSession):
            # Use existing session
            return await func(*args, **kwargs)

        async with app.session.managed_session() as session:
            # Get new session for this function
            kwargs['session'] = session
            return await func(*args, **kwargs)

    return wrapper
