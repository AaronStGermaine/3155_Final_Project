from sqlalchemy import Column, ForeignKey, Integer, String, BOOLEAN, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    customer_name = Column(String(100), nullable=False)
    customer_phone = Column(String(100), nullable=False)
    customer_address = Column(String(255), nullable=False)
    customer_member = Column(BOOLEAN, default=False)
    order_date = Column(DATETIME, nullable=False, server_default=str(datetime.now()))
    description = Column(String(300))

    rating = relationship("Rating", back_populates="order")
    order_detail = relationship("OrderDetail", back_populates="order")
