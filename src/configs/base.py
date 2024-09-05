from fastapi import FastAPI
from fastapi.middleware.gzip import GZipMiddleware
from fastapi.middleware.cors import CORSMiddleware
from middlewares.timout import TimeoutMiddleware
from loguru import logger


async def startup_log() -> None:
    logger.info("API startup!")
    
async def shutdown_log() -> None:
    logger.info("API Shutting down!")    

app = FastAPI(
    title="FastAPI-Pokedex", 
    version="0.0.1",
    servers=[
        {
            "url": "https://localhost:<port>", 
            "description": "Dev environment"
        }
    ],
    on_startup=[startup_log],
    on_shutdown=[shutdown_log]
)

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