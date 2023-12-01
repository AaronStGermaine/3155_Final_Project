from typing import Optional
from pydantic import BaseModel
from .payment_info import PaymentInfo


class CustomerBase(BaseModel):
    name: str
    email: str
    phone: int
    address: str
    payment_id: int
    member: bool


class CustomerCreate(CustomerBase):
    pass


class CustomerUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[int] = None
    address: Optional[str] = None
    payment_id: Optional[str] = None
    member: Optional[bool] = None


class Customer(CustomerBase):
    id: int
    payment_id: PaymentInfo = None

    class ConfigDict:
        from_attributes = True
