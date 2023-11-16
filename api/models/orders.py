from sqlalchemy import Column, ForeignKey, Integer, String, BOOLEAN, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    customer_name = Column(String(100), ForeignKey('customers.name'))
    customer_phone = Column(Integer, ForeignKey('customers.phone'))
    customer_address = Column(String(255), ForeignKey('customers.address'))
    customer_member = Column(BOOLEAN, ForeignKey('customers.member'), default=False)
    order_date = Column(DATETIME, nullable=False, server_default=str(datetime.now()))
    description = Column(String(300))

    order_details = relationship("OrderDetail", back_populates="order")
    customers = relationship("Customer", back_populates="order")