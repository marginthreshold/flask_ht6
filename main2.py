from contextlib import asynccontextmanager
from fastapi import FastAPI
from sqlalchemy import create_engine, select, insert, update, delete
import databases
from typing import List

from pydantic_models2 import UserIn, UserOut, OrdersOut, OrdersIn, GoodsOut, GoodsIn
from sqlalchemy_models2 import Base, User2, Goods, Orders

DATABASE_URL = "sqlite:///sqlite.db"
database = databases.Database(DATABASE_URL)
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

Base.metadata.create_all(bind=engine)


@asynccontextmanager
async def lifespan(app: FastAPI):
    await database.connect()

    yield

    await database.disconnect()


app = FastAPI(lifespan=lifespan)


@app.get('/', response_model=List[UserOut])
async def index():
    users = select(User2)
    return await database.fetch_all(users)


@app.post('/users/', response_model=UserIn)
async def create_user(user: UserIn):
    new_user = insert(User2).values(**user.model_dump())
    await database.execute(new_user)

    return new_user


@app.get('/users/{users_id}', response_model=UserOut)
async def get_user(user_id: int):
    user = await database.fetch_one(select(User2).where(User2.id == user_id))
    return user


@app.put('/users/{users_id}', response_model=UserOut)
async def update_user(user_id: int, new_user: UserIn):
    user_update = update(User2).where(User2.id == user_id).values(**new_user.model_dump())
    await database.execute(user_update)
    return await database.fetch_one(select(User2).where(User2.id == user_id))


@app.delete('/users/{users_id}')
async def delete_user(user_id: int):
    deleted_user = delete(User2).where(User2.id == user_id)

    await database.execute(deleted_user)
    return {"result": "success", "deleted_user_id": user_id}


@app.post('/orders/', response_model=OrdersIn)
async def create_order(order: OrdersIn):
    new_order = insert(Orders).values(**order.model_dump())
    await database.execute(new_order)

    return new_order


@app.get('/orders/{orders_id}', response_model=OrdersOut)
async def get_order(order_id: int):
    order = await database.fetch_one(select(Orders).where(Orders.id == order_id))
    return order


@app.put('/orders/{orders_id}', response_model=OrdersOut)
async def update_order(order_id: int, new_order: OrdersIn):
    order_update = update(Orders).where(Orders.id == order_id).values(**new_order.model_dump())
    await database.execute(order_update)
    return await database.fetch_one(select(Orders).where(Orders.id == order_id))


@app.delete('/orders/{orders_id}')
async def delete_order(order_id: int):
    deleted_order = delete(Orders).where(Orders.id == order_id)

    await database.execute(deleted_order)
    return {"result": "success", "deleted_order_id": order_id}


@app.post('/goods/', response_model=GoodsIn)
async def create_good(good: GoodsIn):
    new_good = insert(Goods).values(**good.model_dump())
    await database.execute(new_good)

    return new_good


@app.get('/goods/{goods_id}', response_model=GoodsOut)
async def get_good(good_id: int):
    good = await database.fetch_one(select(Goods).where(Goods.id == good_id))
    return good


@app.put('/goods/{goods_id}', response_model=GoodsOut)
async def update_good(good_id: int, new_good: GoodsIn):
    good_update = update(Goods).where(Goods.id == good_id).values(**new_good.model_dump())
    await database.execute(good_update)
    return await database.fetch_one(select(Goods).where(Goods.id == good_id))


@app.delete('/goods/{goods_id}')
async def delete_good(good_id: int):
    deleted_good = delete(Goods).where(Goods.id == good_id)

    await database.execute(deleted_good)
    return {"result": "success", "deleted_good_id": good_id}