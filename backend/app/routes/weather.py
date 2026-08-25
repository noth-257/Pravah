from fastapi import APIRouter, HTTPException

from app.services.weather_service import get_weather_data


router = APIRouter(
    prefix="/api/weather",
    tags=["Weather"],
)


@router.get("/")
async def get_weather():
    try:
        weather_data = await get_weather_data()

        return weather_data

    except Exception as error:
        raise HTTPException(
            status_code=500,
            detail=f"Failed to fetch weather data: {str(error)}",
        )