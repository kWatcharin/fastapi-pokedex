from fastapi import FastAPI

from fastapi.middleware.gzip import GZipMiddleware
from fastapi.middleware.cors import CORSMiddleware
from middlewares.timout import TimeoutMiddleware


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