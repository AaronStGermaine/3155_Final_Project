from typing import Optional
from pydantic import BaseModel
from .order_details import OrderDetail


class RatingBase(BaseModel):
    stars: int
    description: str


class RatingCreate(RatingBase):
    pass


class RatingUpdate(BaseModel):
    stars: Optional[int] = None
    description: Optional[str] = None
    order_id: Optional[int] = None


class Rating(RatingBase):
    id: int
    stars: int
    description: str
    order_id: OrderDetail = None

    class ConfigDict:
        from_attributes = True
