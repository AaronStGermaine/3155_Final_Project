from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class PromoBase(BaseModel):
    promo_name: str
    discount: float
    expiration_date: str


class PromoCreate(PromoBase):
    pass


class PromoUpdate(BaseModel):
    promo_name: Optional[str] = None
    discount: Optional[float] = None
    expiration_date: Optional[str] = None


class Promo(PromoBase):
    id: int

    class ConfigDict:
        from_attributes = True