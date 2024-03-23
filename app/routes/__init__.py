
from fastapi.responses import HTMLResponse
from fastapi import APIRouter

from . import updates
from . import stats

router = APIRouter()
router.include_router(updates.router)
router.include_router(stats.router)
