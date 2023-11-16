from typing import Optional
from pydantic import BaseModel


class CustomerBase(BaseModel):
    name: str
    phone: int
    address: str
    payment_method: str


class CustomerCreate(CustomerBase):
    pass


class CustomerUpdate(BaseModel):
    name: Optional[str] = None
    phone: Optional[int] = None
    address: Optional[str] = None
    payment_method: Optional[str] = None


class Customer(CustomerBase):
    id: int
    name: str
    phone: int

    class ConfigDict:
        from_attributes = True
