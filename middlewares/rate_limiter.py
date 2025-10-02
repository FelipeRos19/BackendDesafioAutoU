import time
from collections import defaultdict
from fastapi import Request, Response

class RateLimiter:
    def __init__(self, limit: int, window: int):
        self.limit = limit
        self.window = window
        self.requests_per_ip = defaultdict(list)

    async def __call__(self, request: Request, call_next):
        if request.method == "OPTIONS":
            return Response(status_code=200)

        ip = request.client.host
        now = time.time()

        if ip not in self.requests_per_ip:
            self.requests_per_ip[ip] = []

        self.requests_per_ip[ip] = [t for t in self.requests_per_ip[ip] if now - t < self.window]

        if len(self.requests_per_ip[ip]) >= self.limit:
            return Response(content="Too many requests", status_code=429)

        self.requests_per_ip[ip].append(now)
        return await call_next(request)