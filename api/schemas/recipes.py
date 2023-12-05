from typing import Optional, List
from pydantic import BaseModel
from .resources import Resource
from .foods import Food


class RecipeBase(BaseModel):
    amount: int
    food_id: int
    resource_id: List[int]

class RecipeCreate(RecipeBase):
    pass

class RecipeUpdate(BaseModel):
    food_id: Optional[int] = None
    resource_id: Optional[List[int]] = None
    amount: Optional[int] = None

class Recipe(RecipeBase):
    id: int
    food: Food = None
    resource: List[Resource] = None

    class ConfigDict:
        from_attributes = True