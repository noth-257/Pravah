from fastapi import FastAPI

from app.routes.weather import router as weather_router


app = FastAPI(
    title="PRAVAH API",
    description="Backend API for the PRAVAH flood monitoring and prediction platform",
    version="0.1.0",
)


@app.get("/")
async def root():
    return {
        "message": "PRAVAH backend is running"
    }


@app.get("/health")
async def health_check():
    return {
        "status": "healthy"
    }


app.include_router(weather_router)