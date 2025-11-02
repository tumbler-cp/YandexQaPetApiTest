from typing import TypedDict, Any

class ApiResponseType(TypedDict):
    code: int
    type: str
    message: str

class InventoryType(TypedDict):
    available: int
    pending: int
    sold: int