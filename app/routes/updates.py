
from fastapi import APIRouter, WebSocket

import app.session as session

router = APIRouter()

@router.websocket('/ws')
async def updates(websocket: WebSocket):
    await websocket.accept()

    async with session.redis.pubsub() as pubsub:
        await pubsub.subscribe('spectator')

        while True:
            message = await pubsub.get_message()

            if message is None:
                continue

            if message['data'] == 1:
                continue

            name, args, kwargs = eval(message['data'])

            await websocket.send_json({
                'event': name,
                'args': args,
                'kwargs': kwargs
            })
