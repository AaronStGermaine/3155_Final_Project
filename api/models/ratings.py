from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from ..dependencies.database import Base

class Rating(Base):
    __tablename__ = "ratings"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    stars = Column(Integer, nullable=False)
    description = Column(String(255), nullable=False)
    order_id = Column(Integer, ForeignKey('orders.id'))

    order = relationship("Order", back_populates="rating")