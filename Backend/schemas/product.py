from pydantic import BaseModel
from uuid import UUID



class ProductRequest(BaseModel):
    name: str
    price: float
    datels: str
    quantity: int

 
class ProductResponse(BaseModel):
    message: str
    product_id: UUID

class AddproductRequest(BaseModel):
   product_id: UUID
   user_id: UUID
   name: str
   details: str
   price: float
   quantity: int