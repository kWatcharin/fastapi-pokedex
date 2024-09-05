from fastapi import (Request, status)
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware
import asyncio


class TimeoutMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        try:
            return await asyncio.wait_for(call_next(request), timeout=1.00)
        
        except asyncio.TimeoutError:            
            return JSONResponse(
                content=jsonable_encoder({
                    "detail": "Request timeout"
                }), 
                status_code=status.HTTP_408_REQUEST_TIMEOUT
            )