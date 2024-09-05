from configs.base import app
from routers.pokemons.api import pokemons
from routers.root.api import root
from routers.test.api import test
from loguru import logger


################################ Startup ################################
@app.on_event("startup")
async def startup() -> None:
    logger.info("API startup")
################################ Startup ################################


################################ Routers ################################
# Pokemons
app.include_router(router=pokemons)

# Root
app.include_router(router=root)

# Test
app.include_router(router=test)
################################ Routers ################################


############################### shutdown ################################
@app.on_event("shutdown")
async def shutdown() -> None:
    logger.info("API Shutdown")
############################### shutdown ################################
