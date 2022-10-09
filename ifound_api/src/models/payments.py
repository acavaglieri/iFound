from sqlalchemy import Column, ForeignKey, Integer, String, Date, DateTime, event
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import Boolean
from fastapi import Depends
from ..routes.get_db import get_db
from ..database.database import Base


class Payments(Base):
    __tablename__ = "payments"

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    receiver_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    amount = Column(Integer, nullable=False)
    scheduled_date = Column(Date, nullable=False)
    pay_on_schedule = Column(Boolean, nullable=True)
    paid = Column(Boolean, nullable=False)
    description = Column(String(255), nullable=False)
    approved = Column(String(255), nullable=False)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)

    users = relationship("User", back_populates="payments")
