
from fastapi.responses import JSONResponse, StreamingResponse
from fastapi import APIRouter, Depends

from app.database import get_session
from app.responses import score_dict
from app.repositories import scores

import app.session as session

router = APIRouter()

@router.get("/scores/{checksum}")
async def get_scores(
    checksum: str,
    session=Depends(get_session)
):
    score = await scores.by_checksum(checksum, session)

    if not score:
        return JSONResponse(
            status_code=404,
            content={"error": "Score not found"}
        )

    return score_dict(score)

@router.get("/scores/{checksum}/replay")
async def get_replay(checksum: str):
    if replay := session.redis.get(f"replay:{checksum}"):
        return StreamingResponse(
            replay, media_type="application/octet-stream"
        )

    # TODO: Implement replay storage

    return JSONResponse(
        status_code=404,
        content={"error": "Replay not found"}
    )
