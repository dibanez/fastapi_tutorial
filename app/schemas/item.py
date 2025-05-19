from pydantic import BaseModel

class ItemCreate(BaseModel):
    name: str
    price: float
    in_stock: bool = True

class ItemOut(ItemCreate):
    id: int

    class Config:
        orm_mode = True
