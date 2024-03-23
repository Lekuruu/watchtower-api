
from fastapi import (
    HTTPException,
    Response,
    Request,
    FastAPI
)

from . import routes

import logging
import uvicorn

logging.basicConfig(
    format='[%(asctime)s] - <%(name)s> %(levelname)s: %(message)s',
    level=logging.INFO
)

api = FastAPI(
    title='API',
    version='0.0.1',
    redoc_url=None
)

api.include_router(routes.router, prefix='/api')

def run():
    uvicorn.run(
        api,
        host='0.0.0.0', # TODO
        port=8080,      # TODO
        log_config=None
    )
