from fastapi import APIRouter

from database import Base, engine
from app.routes.users import users_router
from app.routes.orders import orders_router
from app.routes.login import login_router
from app.routes.products import product_router
from app.routes.categories import category_router

api = APIRouter()

Base.metadata.create_all(bind=engine)

api.include_router(login_router)
api.include_router(users_router)
api.include_router(category_router)
api.include_router(product_router)
api.include_router(orders_router)
