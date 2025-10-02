import os

from fastapi import FastAPI, Request

from middlewares.cors import setup_cors
from middlewares.rate_limiter import RateLimiter
from routes.api_routes import api_router

app = FastAPI()

setup_cors(app)
rate_limiter = RateLimiter(int(os.getenv("RATE_LIMIT")), int(os.getenv("TIME_WINDOW")))

app.middleware("http")(rate_limiter)
app.include_router(api_router)