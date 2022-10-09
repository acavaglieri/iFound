from datetime import date, datetime
from typing import Optional, List
from pydantic import BaseModel
from src.schemas.status import StatusModel


class PaymentBase(BaseModel):
    receiver_id: int
    amount: int
    scheduled_date: date
    pay_on_schedule: bool
    paid: bool
    description: str
    approved: str


class Payment(PaymentBase):
    id: int
    created_at: datetime
    updated_at: datetime


class PaymentsFilter(BaseModel):
    id: Optional[int] = None
    receiver_federal_id: Optional[str] = None
    amount: Optional[int] = None
    scheduled_date: Optional[date] = None
    description: Optional[str] = None
    after_date: Optional[date] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = False
    skip: Optional[int] = None
    limit: Optional[int] = None
    order: Optional[bool] = None
    sort: Optional[str] = None


class AllPayments(StatusModel):
    users_total_count: int
    users: List[Payment]

    class Config:
        orm_mode = True


class PaymentCreateRequest(BaseModel):
    receiver_federal_id: str
    amount: int
    scheduled_date: date
    paid: bool = False
    description: str


class PaymentUpdateRequest(BaseModel):
    receiver_id: Optional[int] = None
    amount: Optional[int] = None
    pay_on_schedule: Optional[bool] = None
    scheduled_date: Optional[date] = None
    description: Optional[str] = None
    paid: Optional[bool] = None
    approved: Optional[str] = None


class PaymentUpdateResponse(StatusModel):
    payment: Payment
