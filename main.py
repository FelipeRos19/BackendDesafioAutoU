import os

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

from middlewares.rate_limiter import RateLimiter
from routes.api_routes import api_router

app = FastAPI()

origins = [
    "https://emails.felipe.fun",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
)

rate_limiter = RateLimiter(int(os.getenv("RATE_LIMIT")), int(os.getenv("TIME_WINDOW")))

app.middleware("http")(rate_limiter)
app.include_router(api_router)