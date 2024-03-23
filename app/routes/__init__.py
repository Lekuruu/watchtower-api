
from fastapi.responses import HTMLResponse
from fastapi import APIRouter

from . import updates

router = APIRouter()
router.include_router(updates.router)
