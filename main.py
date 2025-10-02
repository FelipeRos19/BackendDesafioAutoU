import os

from fastapi import FastAPI, Request

from middlewares.cors import setup_cors
from middlewares.rate_limiter import RateLimiter
from routes.api_routes import api_router

app = FastAPI()

rate_limiter = RateLimiter(int(os.getenv("RATE_LIMIT")), int(os.getenv("TIME_WINDOW")))
setup_cors(app)

app.middleware("http")(rate_limiter)
app.include_router(api_router)