from typing import Optional
from pydantic import BaseModel
from .payment_info import PaymentInfo


class CustomerBase(BaseModel):
    name: str
    email: str
    phone: str
    address: str
    payment_id: int
    member: bool


class CustomerCreate(CustomerBase):
    pass


class CustomerUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    address: Optional[str] = None
    payment_id: Optional[int] = None
    member: Optional[bool] = None


class Customer(CustomerBase):
    id: int
    payment_info: PaymentInfo = None

    class ConfigDict:
        from_attributes = True
