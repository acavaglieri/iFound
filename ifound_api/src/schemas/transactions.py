from datetime import date, datetime
from typing import Optional, List
from pydantic import BaseModel


class TransactionData(BaseModel):
    user_id: int
    amount: int
    date: date
    to_or_from: str
    credit_or_debit: str

class Event(BaseModel):
    id: str
    subscription: str
    created: datetime
    log: dict

class AllEvents(BaseModel):
    events: List[Event]