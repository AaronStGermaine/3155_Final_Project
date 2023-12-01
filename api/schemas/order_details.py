from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from .foods import Food
from .promos import Promo
from .orders import Order

class OrderDetailBase(BaseModel):
    order_id: int
    food_id: int
    promo_id: int
    status: str
    amount: float


class OrderDetailCreate(OrderDetailBase):
    pass

class OrderDetailUpdate(BaseModel):
    order_id: Optional[int] = None
    food_id: Optional[int] = None
    promo_id: Optional[int] = None
    status: Optional[str] = None
    amount: Optional[float] = None


class OrderDetail(OrderDetailBase):
    id: int
    order: Order = None
    promo: Promo = None
    food: Food = None


    class ConfigDict:
        from_attributes = True
