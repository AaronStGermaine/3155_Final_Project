from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class FoodBase(BaseModel):
    food_name: str
    food_category: str
    calories: int
    price: float


class FoodCreate(FoodBase):
    pass


class FoodUpdate(BaseModel):
    food_name: Optional[str] = None
    food_category: Optional[str] = None
    calories: Optional[int] = None
    price: Optional[float] = None


class Food(FoodBase):
    id: int

    class ConfigDict:
        from_attributes = True