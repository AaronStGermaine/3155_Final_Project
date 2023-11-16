from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from ..dependencies.database import Base


class Food(Base):
    __tablename__ = "foods"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    food_name = Column(String(100), unique=True, nullable=False)
    food_category = Column(String(100), unique=True, nullable=False)
    calories = Column(Integer, nullable=False)
    price = Column(DECIMAL(4, 2), nullable=False, server_default='0.0')

    recipes = relationship("Recipe", back_populates="food")
    order_details = relationship("OrderDetail", back_populates="food")
