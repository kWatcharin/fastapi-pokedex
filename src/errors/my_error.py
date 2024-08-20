
from fastapi import HTTPException, Request
from fastapi.responses import JSONResponse
from typing import Any, Dict
from configs import app


class MyErrorException(HTTPException):
    def __init__(
        self, status_code: int, 
        detail: Dict[str, Any], 
        headers: Dict[str, str] | None = None
    ) -> dict:
        super().__init__(status_code=status_code, detail=detail, headers=headers)
        
        
class MyErrorExceptionV2(Exception):
    def __init__(self, name: str) -> dict:
        self.name = name
        
@app.exception_handler(MyErrorExceptionV2)
async def unicorn_exception_handler(request: Request, exc: MyErrorExceptionV2) -> dict:
    return JSONResponse(
        status_code=418,
        content={"message": f"Oops! {exc.name} did something. There goes a rainbow..."},
    )