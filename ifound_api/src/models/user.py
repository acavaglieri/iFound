from sqlalchemy import Boolean, Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from src.database.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True, nullable=False)
    name = Column(String(255), index=True, nullable=False)
    email = Column(String(255), unique=True, index=True, nullable=False)
    federal_id = Column(String(255), unique=True, index=True, nullable=False)
    cellphone = Column(String(255), unique=True, index=True, nullable=False)
    encrypted_password = Column(String(255), nullable=False)
    birthday = Column(DateTime, nullable=True)
    is_inactive = Column(Boolean, default=False, nullable=False)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)
    token = Column(String(255), unique=True, nullable=True)
    is_confirmed = Column(Boolean, nullable=False)
    role = Column(String(255), unique=False, nullable=False)

    payments = relationship("Payments", back_populates="users")