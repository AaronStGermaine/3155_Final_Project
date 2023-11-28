from typing import Optional
from pydantic import BaseModel


class PaymentInfoBase(BaseModel):
    payment_type: str
    card_number: int
    exp_date: str
    transaction_status: str



class PaymentInfoCreate(PaymentInfoBase):
    pass


class PaymentInfoUpdate(BaseModel):
    payment_type: Optional[str] = None
    card_number: Optional[int] = None
    exp_date: Optional[str] = None
    transaction_status: Optional[str] = None


class PaymentInfo(PaymentInfoBase):
    id: int
    payment_type: str
    card_number: int
    exp_date: str
    transaction_status: str


    class ConfigDict:
        from_attributes = True
