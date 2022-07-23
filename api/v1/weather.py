from fastapi import APIRouter

from weather import weather

router = APIRouter()


@router.get("/")
async def current_forecast():
    current = weather.get_current()

    return current


@router.get("/forecast")
async def five_day_forecast():
    forecasts = weather.get_forecast()
    dict_forecasts = [obj.dict() for obj in forecasts]

    return {"forecasts": dict_forecasts}
