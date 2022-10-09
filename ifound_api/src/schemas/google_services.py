from pydantic import BaseModel
from typing import Optional

class FullAddress(BaseModel):
    full_address: Optional[str] = None

class SliceAddress(FullAddress):
    street: Optional[str] = None
    city: Optional[str] = None
    country: Optional[str] = None
    district: Optional[str] = None
    house_number: Optional[str] = None
    zip_code: Optional[str] = None
    state: Optional[str] = None