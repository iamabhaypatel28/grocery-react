from pydantic import BaseModel
from uuid import UUID



class ProductRequest(BaseModel):
    # admin_id: str
    name: str
    price: float
    datels: str
    quantity: int
    file: str


class ProductResponse(BaseModel):
    message: str
    product_id: UUID

