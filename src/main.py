from configs import app

from routers.pokemons.api import router as pokemons
from routers.test.api import router as test

################################ Routers ################################
# Pokemons
app.include_router(router=pokemons)

# Test
app.include_router(router=test)
################################ Routers ################################
