from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from ..dependencies.database import Base

class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    phone = Column(Integer, nullable=False)
    address = Column(String(255), nullable=False)
    payment_method = Column(String(100), nullable=False)

    sandwich = relationship("Sandwich", back_populates="customers")
