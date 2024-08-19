from fastapi import (APIRouter, status, Request)
import asyncio, time


router = APIRouter(prefix="/test", tags=["Test"])

@router.get(path="/req_timeout")
async def req_timeout(req: Request) -> dict:
    await asyncio.sleep(10)
    
    return {
        "detail": "test request timeout" 
    }