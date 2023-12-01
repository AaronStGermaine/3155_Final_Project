from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME, BOOLEAN
from sqlalchemy.orm import relationship
from ..dependencies.database import Base

class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100))
    phone = Column(Integer, nullable=False)
    address = Column(String(255), nullable=False)
    payment_id = Column(Integer, ForeignKey("payment_info.id"))
    member = Column(BOOLEAN, default=False, nullable=False)

    payment_info = relationship("PaymentInfo", back_populates="customer")
