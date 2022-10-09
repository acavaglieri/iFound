from typing import Optional
from pydantic import BaseModel

class StatusModel(BaseModel):
    status: Optional[str]
    message: Optional[str]