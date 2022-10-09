from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel
from src.schemas.status import StatusModel


class BrCodePreviewModel(StatusModel):
    br_code: str

class BrCodePreviewResponseModel(StatusModel):
    account_number: int
    branch_code: int
    name: str
    federal_id: str
    amount: float

class BrCodePaymentModel(StatusModel):
    br_code: str
    federal_id: str
    description: Optional[str]
    schedule_date: Optional[str]

class ChargeDataModel(StatusModel):
    amount: float
    to_default_workspace: bool

class ChargeResponseModel(StatusModel):
    amount: float
    br_code: str

class Transactions(BaseModel):
    amount: str = None
    created: datetime = None
    description: str = None
    external_id: str = None
    fee: int = None
    id: str = None
    receiver_id: str = None
    sender_id: str = None
    source: str = None
    balance: str = None
    tags: List[str] = None

class SingleTransactionId(BaseModel):
    id: str
    account_type: str

class CreateTransactionRequest(BaseModel):
    amount: float
    receiver_id: str
    description: str

class GetWorkspaceStatementRequest(BaseModel):
    #Filtros:
    limit: Optional[int]
    after: Optional[datetime]
    before: Optional[datetime]
    external_ids: Optional[List[str]]
    tags: Optional[List[str]]
    ids: Optional[List[str]]

class GetWorkspaceStatementResponse(StatusModel):
    transactions_total_count: int
    transactions: List[Transactions]

class GetWorkspaceBalanceResponse(StatusModel):
    balance: int

class GetWorkspaceRequest(BaseModel):
    id: str