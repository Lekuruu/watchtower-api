
from fastapi.responses import JSONResponse, StreamingResponse
from fastapi import APIRouter, Depends, Query, Response

from app.database import get_session
from app.responses import score_dict
from app.repositories import scores

import app.session as session

router = APIRouter()

@router.get("/scores/recent")
async def get_recent_scores(
    limit: int = Query(50, ge=1, le=100),
    offset: int = Query(0, ge=0),
    session=Depends(get_session)
):
    recent_scores = await scores.recent(
        limit=limit,
        offset=offset,
        session=session
    )
    return [score_dict(score) for score in recent_scores]

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
    score = await scores.by_checksum(checksum)

    if not score:
        return JSONResponse(
            status_code=404,
            content={"error": "Score not found"}
        )

    if not score.replay_available:
        return JSONResponse(
            status_code=404,
            content={"error": "Replay not available"}
        )

    if replay := await session.redis.get(f"replays:{checksum}"):
        return Response(
            replay,
            media_type="application/octet-stream",
            headers={
                "Content-Disposition": f"attachment; filename={score.replay_filename}"
            }
        )

    # TODO: Implement replay storage

    return JSONResponse(
        status_code=404,
        content={"error": "Replay not found"}
    )
