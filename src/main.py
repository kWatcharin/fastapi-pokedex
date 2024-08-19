from fastapi import FastAPI, Request
from fastapi.middleware.gzip import GZipMiddleware
from fastapi.middleware.cors import CORSMiddleware
from middlewares.timout import TimeoutMiddleware

from routers.pokemons.api import router as pokemons
from routers.test.api import router as test

app = FastAPI(title="FastAPI-Pokedex")
app.mount(path="/fastapi-pokedex", app=app)

############################## Middlewares ##############################
# Request Timeout
app.add_middleware(middleware_class=TimeoutMiddleware)

# Cors
app.add_middleware(
    middleware_class=CORSMiddleware, 
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "PATCH", "DELETE"],
    allow_headers=["Content-Type"]
)

# Gzip
app.add_middleware(middleware_class=GZipMiddleware, minimum_size=500)
############################## Middlewares ##############################

################################ Routers ################################
app.include_router(router=pokemons)
app.include_router(router=test)
################################ Routers ################################

@app.get("/")
@app.post("/")
async def main(request: Request) -> dict:
    match request.method:
        case "GET":
            return {
                "detail": "hello, world",
                "method": "GET"
            }
            
        case "POST":
            return {
                "detail": "hello, world",
                "method": "POST"
            }
       
    
    
# CMD with uvicorn ASGI

# Production
# uvicorn main:app --host 0.0.0.0 --port 9090 --workers 4;
# fastapi run --host 0.0.0.0 --port 9090 --workers 4;

# Develop
# fastapi dev