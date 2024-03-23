
from fastapi.responses import JSONResponse
from fastapi import APIRouter

import app.session as session
import app.utils as utils
import json

router = APIRouter()

@router.get('/stats/{server}/{id}')
async def stats(server: str, id: int):
    # Re-fetch stats from spectator service
    await utils.request_stats(server, id)

    data = await session.redis.get(
        f'players:{server}:{id}'
    )

    if not data:
        return JSONResponse(
            {'error': 'No data available'},
            status_code=404
        )

    return JSONResponse(
        json.loads(data),
        status_code=200
    )
