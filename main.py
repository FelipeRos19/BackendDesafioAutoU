import os

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

from middlewares.rate_limiter import RateLimiter
from routes.api_routes import api_router
from fastapi.responses import RedirectResponse

app = FastAPI()

origins = [
    "https://emails.felipe.fun",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://frontenddesafioautou-production.up.railway.app"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=False
)

@app.middleware("http")
async def https_redirect(request: Request, call_next):
    if request.headers.get("x-forwarded-proto") == "http":
        url = request.url.replace(scheme="https")
        return RedirectResponse(url)
    response = await call_next(request)
    return response

#rate_limiter = RateLimiter(int(os.getenv("RATE_LIMIT")), int(os.getenv("TIME_WINDOW")))

#app.middleware("http")(rate_limiter)
app.include_router(api_router)