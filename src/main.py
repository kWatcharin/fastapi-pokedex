from configs import app

from routers.pokemons.api import pokemons
from routers.root.api import root
from routers.test.api import test

################################ Routers ################################
# Pokemons
app.include_router(router=pokemons)

# Root
app.include_router(router=root)

# Test
app.include_router(router=test)
################################ Routers ################################
