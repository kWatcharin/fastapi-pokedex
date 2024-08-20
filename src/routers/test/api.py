from fastapi import (APIRouter, status, Request)
import asyncio, time


test = APIRouter(prefix="/test", tags=["Test"])

@test.get(path="/req_timeout")
async def req_timeout(req: Request) -> dict:
    await asyncio.sleep(10)
    
    return {
        "detail": "test request timeout" 
    }