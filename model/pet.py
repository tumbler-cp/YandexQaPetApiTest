from typing import List, TypedDict

class CategoryType(TypedDict):
    id: int
    name: str

class TagType(TypedDict):
    id: int
    name: str

class PetType(TypedDict):
    id: int
    name: str
    category: CategoryType
    photoUrls: List[str]
    tags: List[TagType]
    status: str