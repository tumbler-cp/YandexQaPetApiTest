from typing import TypedDict

class UserType(TypedDict):
    id: int
    username: str
    firstName: str
    lastName: str
    email: str
    password: str
    phone: str
    userStatus: int