from typing import Optional, List
from uuid import UUID, uuid4
from enum import Enum

from pydantic import BaseModel


class Gender(Enum):
    """Gender class for the User"""
    MALE = "male"
    FEMALE = "female"


class Role(Enum):
    """Role class for the User"""
    ADMIN = "admin"
    USER = "user"
    TESTER = "tester"


class User(BaseModel):
    """User model class"""
    id: Optional[UUID] = uuid4()
    first_name: str
    last_name: str
    middle_name: Optional[str]
    gender: Gender
    roles: List[Role]


class UserUpdateRequest(BaseModel):
    """User model class for update request"""
    first_name: Optional[str]
    last_name: Optional[str]
    middle_name: Optional[str]
    roles: Optional[List[Role]]
