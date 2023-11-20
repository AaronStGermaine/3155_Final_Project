from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from .foods import Food
from .promos import Promo

class OrderDetailBase(BaseModel):
    amount: int


class OrderDetailCreate(OrderDetailBase):
    order_id: int
    food_id: int
    promo_id: int
    status: str

class OrderDetailUpdate(BaseModel):
    order_id: Optional[int] = None
    food_id: Optional[int] = None
    promo_id: Optional[int] = None
    status: Optional[str] = None
    amount: Optional[int] = None


class OrderDetail(OrderDetailBase):
    id: int
    order_id: int
    promo: Promo = None
    food: Food = None
    status: str

    class ConfigDict:
        from_attributes = True