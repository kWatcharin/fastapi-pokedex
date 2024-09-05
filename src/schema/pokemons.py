from pydantic import BaseModel, Field
from typing_extensions import Annotated, Doc


class FavoritePokemons(BaseModel):
    id: int
    name: Annotated[int, Doc("""Name of Pokemon""")] = Field(default=None)
    lv: int
    active: bool
    
    class Config:
        schema_extra = {
            "id": 1,
            "name": "ditto",
            "lv": 12,
            "active": True
        }