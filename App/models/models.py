from typing import Optional
from uuid import uuid4, UUID
from pydantic import BaseModel
from enum import Enum

class Gender(str, Enum):
    male='male'
    female='female'

class Role(str, Enum):
    user='user'
    admin='admin'

class User(BaseModel):
    id: Optional[UUID]=uuid4()
    first_name: str
    last_name: str
    gender: Gender
    role: Role