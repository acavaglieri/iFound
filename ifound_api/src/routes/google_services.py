from main import *
from src.schemas import google_services as gs_schema
from src.services import google_services as gs_service

@app.post("/google_service/slice_address", tags=["Google Services"], response_model=gs_schema.SliceAddress)
def slice_address(full_address: gs_schema.FullAddress):
    response = gs_service.slice_address(full_address.full_address)
    slice_address = []
    return response