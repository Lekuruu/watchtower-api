
from fastapi.responses import HTMLResponse
from fastapi import APIRouter

from . import spectating
from . import updates
from . import scores
from . import stats

router = APIRouter()
router.include_router(spectating.router)
router.include_router(updates.router)
router.include_router(scores.router)
router.include_router(stats.router)
