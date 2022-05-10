from typing import List
from uuid import UUID
from fastapi import APIRouter, FastAPI, HTTPException
from .models.User import Gender, Role, User, UserUpdateRequest

router = APIRouter(prefix='/api/v1')

app = FastAPI()
# TODO: move prefix to a router
# app.include_router(router, prefix='/api/v1')

db: List[User] = [
    User(
        id="16a918ad-ec33-49d9-ad16-23d7ca24262c",
        first_name="John",
        last_name="Tester",
        gender=Gender.male,
        roles=[Role.tester]
    ),
    User(
        id="97ddbd3b-defa-4202-9467-4d846b1aaa5d",
        first_name="Alex",
        last_name="Admin",
        gender=Gender.male,
        roles=[Role.admin]
    ),
]


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/api/v1/users")
async def get_users():
    return db


@app.post("/api/v1/users")
async def add_user(user: User):
    db.append(user)
    return {"id": user.id}


@app.delete("/api/v1/users/{user_id}")
async def delete_user(user_id: UUID):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return

    raise HTTPException(
        status_code=404,
        detail=f"User with ID: {user_id} not found"
    )


@app.put("/api/v1/users/{user_id}")
async def update_user(user_id: UUID, user_update: UserUpdateRequest):
    for user in db:
        if user.id == user_id:
            if user_update.first_name is not None:
                user.first_name = user_update.first_name
            if user_update.last_name is not None:
                user.last_name = user_update.last_name
            if user_update.middle_name is not None:
                user.middle_name = user_update.middle_name
            if user_update.roles is not None:
                user.roles = user_update.roles
            return user

    raise HTTPException(
        status_code=404,
        detail=f"User with ID: {user_id} not found"
    )
