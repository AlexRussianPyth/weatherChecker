import uvicorn
from fastapi import FastAPI

import config

from models.weekday import Weekday

app = FastAPI(
    title=config.PROJECT_NAME,
    docs_url='/api/openapi',
    openapi_url='/api/openapi.json',
)

@app.get('/')
async def index():
    return {'tex222t3': 'tes3t'}

@app.get('/weathers/{day}')
async def weather_for_day(day: str):
    return {
        'specific_weather': day
    }

# TODO Make function to return weather by day of week (use enum)
@app.get("/week/{weekday}")
async def weather_by_weekday(weekday: Weekday):

    match weekday:
        case Weekday.MONDAY:
            return {"message": 'You try monday weather'}
        case Weekday.TUESDAY:
            return {"message": 'You try tuesday weather'}


if __name__ == '__main__':
    uvicorn.run(
        'main:app',
        reload=config.UVICORN_RELOAD,
        host='0.0.0.0',
        port=8000, # так как порт 8000 уже занят нашей админкой
    )
