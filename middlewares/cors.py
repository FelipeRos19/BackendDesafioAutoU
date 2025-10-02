import os

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

def setup_cors(app: FastAPI):
    origins = [
        "https://emails.felipe.fun"
    ]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )