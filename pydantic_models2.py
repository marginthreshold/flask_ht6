from pydantic import BaseModel, Field
from datetime import date


class UserIn(BaseModel):
    name: str = Field(min_length=2)
    lastname: str = Field(min_length=2)
    birthdate: date = Field(None)
    email: str
    address: str = Field(min_length=5)


class UserOut(UserIn):
    id: int


class GoodsIn(BaseModel):
    name: str = Field(min_length=2)
    description: str = Field(min_length=2)
    price: int


class GoodsOut(UserIn):
    id: int


class OrdersIn(BaseModel):
    user_id: int
    order_id: int
    order_date: date = Field(None)
    status: str


class OrdersOut(UserIn):
    id: int
