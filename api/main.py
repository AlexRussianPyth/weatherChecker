import uvicorn
from fastapi import FastAPI

from . import config
from .models.weekday import Weekday
from weather.weather import get_forecast


app = FastAPI(
    title=config.PROJECT_NAME,
    docs_url="/api/openapi",
    openapi_url="/api/openapi.json",
)

love = "sdgsgs"


@app.get("/")
async def index():
    return {"tex222t3": "tes3t"}


@app.get("/weathers/forecast")
async def weather_forecast():
    forecasts = get_forecast()
    dict_forecasts = [obj.dict() for obj in forecasts]
    return {"forecasts": dict_forecasts}


@app.get("/weathers/{day}")
async def weather_for_day(day: str):
    return {"specific_weather": day}


# TODO Make function to return weather by day of week (use enum)
@app.get("/week/{weekday}")
async def weather_by_weekday(weekday: Weekday):

    match weekday:
        case Weekday.MONDAY:
            return {"message": "You try monday weather"}
        case Weekday.TUESDAY:
            return {"message": "You try tuesday weather"}


def api_run():
    uvicorn.run("api.main:app", reload=config.UVICORN_RELOAD, host="0.0.0.0", port=8000)
