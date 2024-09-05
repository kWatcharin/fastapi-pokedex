from typing import (Dict, Any)
from pydantic import (BaseModel, ConfigDict)

from fastapi import APIRouter, status
from fastapi.requests import Request
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from errors.my_error import MyExc, RequiredException

class TestDict(BaseModel):
    model_config = ConfigDict(
        extra='forbid', 
        str_strip_whitespace=True,
        json_schema_extra={
            "example": {
                "data": {
                    "text": "hello"
                }
            }
        }
    )
    
    data: Dict[str, Any]
    
    
async def poke_start():
    print("Router pokemons start!")
    
async def poke_stop():
    print("Router pokemons stop!")
    
pokemons = APIRouter(
    prefix="/pokemons", 
    tags=["Pokemons"],
    # on_startup=[poke_start],
    # on_shutdown=[poke_stop]
)


@pokemons.get("/list")
async def list_api(_request: Request) -> Dict[str, Any]:
    content = jsonable_encoder({ 
        "detail": [
            {
                "id": 1, 
                "name": "ditto"
            }
        ] 
    })
    return JSONResponse(content=content, status_code=status.HTTP_200_OK, media_type="application/json")


@pokemons.get("/my_exc")
async def my_exc() -> Dict[str, Any]:
    raise RequiredException(field="tewst")


@pokemons.post("/test_dict")
async def test_dict_api(request: Request, model: TestDict) -> Dict[str, Any]:
    return model.data