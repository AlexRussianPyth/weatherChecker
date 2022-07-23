import uvicorn
from fastapi import FastAPI

from . import config
from api.v1 import weather

app = FastAPI(
    title=config.PROJECT_NAME,
    docs_url="/api/openapi",
    openapi_url="/api/openapi.json",
)

app.include_router(weather.router, prefix="/api/v1/weather", tags=["weather"])


def api_run():
    uvicorn.run("api.main:app", reload=config.UVICORN_RELOAD, host="0.0.0.0", port=8000)
