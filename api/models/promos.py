from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME, FLOAT
from sqlalchemy.orm import relationship
from ..dependencies.database import Base


class Promo(Base):
    __tablename__ = "promos"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    promo_name = Column(String(100), nullable=False)
    discount = Column(FLOAT, nullable=False, server_default='0.0')
    expiration_date = Column(String(100))

