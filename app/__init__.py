
from fastapi import FastAPI

from . import routes

import logging
import uvicorn
import config

logging.basicConfig(
    format='[%(asctime)s] - <%(name)s> %(levelname)s: %(message)s',
    level=logging.INFO
)

api = FastAPI(
    title='API',
    version='0.0.1',
    redoc_url=None,
    debug=config.DEBUG
)

api.include_router(routes.router, prefix='/api')

def run():
    uvicorn.run(
        api,
        host=config.API_HOST,
        port=config.API_PORT,
        log_config=None
    )
