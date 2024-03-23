
from fastapi import APIRouter
from .stats import stats

import app.session as session
import json

router = APIRouter()

@router.get('/spectating/{server}')
async def spectating(server: str):
    user_ids = await session.redis.lrange(
        f'spectating:{server}', 0, -1
    )

    default_user = {
        "id": 0,
        "name": "Loading...",
        "country": "XX",
        "server": server,
        "stats": {
            "rscore": 0,
            "tscore": 0,
            "acc": 0.00,
            "pp": 0,
            "playcount": 0,
            "rank": 0
        },
        "status": {
            "action": 0,
            "text": "",
            "checksum": "",
            "mods": 0,
            "mode": 0,
            "beatmap_id": -1
        }
    }

    return {
        user_id: json.loads(
            await session.redis.get(
                f'players:{server}:{int(user_id)}'
            ) or str(default_user)
        )
        for user_id in user_ids
    }
