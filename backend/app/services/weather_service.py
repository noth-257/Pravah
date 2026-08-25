import httpx


OPEN_METEO_URL = "https://api.open-meteo.com/v1/forecast"

# Gorakhpur coordinates
GORAKHPUR_LATITUDE = 26.7606
GORAKHPUR_LONGITUDE = 83.3732


async def get_weather_data():
    params = {
        "latitude": GORAKHPUR_LATITUDE,
        "longitude": GORAKHPUR_LONGITUDE,
        "current": "rain,precipitation,temperature_2m",
        "hourly": "rain,precipitation_probability",
        "forecast_days": 2,
    }

    async with httpx.AsyncClient() as client:
        response = await client.get(
            OPEN_METEO_URL,
            params=params,
            timeout=10.0,
        )

        response.raise_for_status()

        data = response.json()

    return data