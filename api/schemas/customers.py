from typing import Optional
from pydantic import BaseModel


class CustomerBase(BaseModel):
    name: str
    email: str
    phone: int
    address: str
    payment_method: str
    member: bool


class CustomerCreate(CustomerBase):
    pass


class CustomerUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[int] = None
    address: Optional[str] = None
    payment_method: Optional[str] = None
    member: Optional[bool] = None


class Customer(CustomerBase):
    id: int
    name: str
    email: str
    phone: int
    member: bool

    class ConfigDict:
        from_attributes = True
