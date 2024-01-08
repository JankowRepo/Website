from uuid import uuid4
from fastapi import FastAPI
from typing import List
from App.models.models import User, Gender, Role

app = FastAPI()

db:List[User]=[
    User(id=uuid4(),
         first_name='Adam',
         last_name='Jankowiak',
         gender=Gender.male,
         role=Role.admin),
    User(id=uuid4(),
         first_name='Jan',
         last_name='Kowalski',
         gender=Gender.male,
         role=Role.user)
]


@app.get("/users", response_model=List[User])
async def get_users():
    return db

@app.post("/users", response_model=User)
async def add_user(user: User):
    db.append(user)
    return user

@app.put("/users/{item_id}", response_model=User)
async def update_item(item_id: int, item: User):
    db[item_id] = item
    return item

@app.delete("/users/{item_id}")
async def delete_item(item_id: int):
    del db[item_id]
    return {"message": "Item deleted"}
