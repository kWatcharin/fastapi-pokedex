from typing import (Any, Dict, Union)
from typing_extensions import (Annotated, Doc)
from fastapi import (HTTPException, Request, status)
from fastapi.responses import JSONResponse
from configs.base import app


class MyErrorException(HTTPException):
    def __init__(
        self, status_code: int, 
        detail: Dict[str, Any], 
        headers: Dict[str, str] | None = None
    ) -> dict:
        super().__init__(status_code=status_code, detail=detail, headers=headers)
        
        
class MyErrorExceptionV2(Exception):
    def __init__(self, name: str) -> None:
        self.name = name
        
@app.exception_handler(MyErrorExceptionV2)
async def unicorn_exception_handler(request: Request, exc: MyErrorExceptionV2) -> Dict[str, Any]:
    return JSONResponse(
        status_code=418,
        content={"message": f"Oops! {exc.name} did something. There goes a rainbow..."},
    )
    
    
class MyExc(Exception):
    def __init__(self, name: str) -> None:
        self.name = name
        
@app.exception_handler(MyExc)
async def my_exc(request: Request, exc: MyExc) -> Dict[str, Any]:
    return JSONResponse(
        content={"data": "test"},
        status_code=status.HTTP_502_BAD_GATEWAY
    )
    
    
class RequiredException(Exception):
    """Required Field Exception Handler."""
    def __init__(
        self, 
        field: str, 
        detail: Annotated[Union[str, None], Doc("Any text that you need to describe it.")] = None
    ) -> None:
        self.field = field
        self.detail = detail
    
@app.exception_handler(RequiredException)
async def required_exception_handler(request: Request, exc: RequiredException) -> Dict[str, Any]:
    match exc.detail:
        case None:
            detail_text = " is required."
        case _:
            detail_text = f" {exc.detail}" 
    
    status_code = status.HTTP_400_BAD_REQUEST
    return JSONResponse(
        status_code=status_code,
        content={
            "data": f"{exc.field}{detail_text}",
            "status_code": status_code
        }
    )