from fastapi import APIRouter, status
from fastapi.requests import Request
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse


pokemons = APIRouter(prefix="/pokemons", tags=["Pokemons"])


@pokemons.get("/list")
async def list_api(_request: Request) -> dict:
    content = jsonable_encoder({ 
        "detail": [
            {
                "id": 1, 
                "name": "ditto"
            }
        ] 
    })
    return JSONResponse(content=content, status_code=status.HTTP_200_OK)