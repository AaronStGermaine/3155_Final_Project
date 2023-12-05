from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME, BOOLEAN
from sqlalchemy.orm import relationship
from ..dependencies.database import Base

class PaymentInfo(Base):
    __tablename__ = "payment_info"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    payment_type = Column(String(100), nullable=False)
    card_number = Column(String(100))
    exp_date = Column(String(100))
    transaction_status = Column(String(100))

    customer = relationship("Customer", back_populates="payment_info")
