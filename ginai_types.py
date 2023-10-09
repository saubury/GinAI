from typing import List
from pydantic import BaseModel

# create a PyDantic schema for output
class Ingredient(BaseModel):
    ingredient_name: str
    quantity_ml: int

class Cocktail(BaseModel):
    cocktail_name: str
    description: str
    inventor: str
    matching_song: str
    instructions: str
    ingredients: list[Ingredient]

