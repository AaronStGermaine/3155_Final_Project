from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from ..dependencies.database import Base

class OrderDetail(Base):
    __tablename__ = "order_details"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey("orders.id"))
    food_id = Column(Integer, ForeignKey("foods.id"))
    promo_id = Column(Integer, ForeignKey("promos.id"))
    status = Column(String(200), nullable=False)
    amount = Column(Integer, index=True, nullable=False)

    food = relationship("Food", back_populates="order_detail")
    order = relationship("Order", back_populates="order_detail")
    promo = relationship("Promo", back_populates="order_detail")