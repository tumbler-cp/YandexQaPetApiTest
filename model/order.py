from typing import TypedDict

class OrderType(TypedDict):
    id: int
    petId: int
    quantity: int
    shipDate: str
    status: str
    complete: bool