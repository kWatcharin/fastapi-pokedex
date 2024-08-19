from fastapi import Request
from errors.my_error import MyErrorExceptionV2

from routers.pokemons.api import router as pokemons
from routers.test.api import router as test

from configs import app


################################ Routers ################################
# Pokemons
app.include_router(router=pokemons)

# Test
app.include_router(router=test)
################################ Routers ################################

@app.get("/")
@app.post("/")
async def main(request: Request) -> dict:
    match request.method:
        case "GET":
            raise MyErrorExceptionV2(name="GET")
            
        case "POST":
            raise MyErrorExceptionV2(name="POST")
       
          
### CMD with uvicorn ASGI

### Development
### fastapi dev --port 9090;

### Production
### uvicorn main:app --host 0.0.0.0 --port 9090 --workers 4;
### fastapi run --host 0.0.0.0 --port 9090 --workers 4;

