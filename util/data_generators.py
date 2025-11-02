from faker import Faker
from datetime import datetime, timedelta
from typing import List, Optional
from model.pet import PetType, TagType
from model.order import OrderType
from model.user import UserType

fake = Faker()

class PetStatus:
    AVAILABLE = "available"
    PENDING = "pending"
    SOLD = "sold"

class OrderStatus:
    PLACED = "placed"
    APPROVED = "approved"
    DELIVERED = "delivered"

class PetDataGenerator:    
    @staticmethod
    def generate_pet_data(
        pet_id: Optional[int] = None,
        name: Optional[str] = None,
        category_id: Optional[int] = None,
        category_name: Optional[str] = None,
        photo_urls: Optional[List[str]] = None,
        tags: Optional[List[TagType]] = None,
        status: str = PetStatus.AVAILABLE
    ) -> PetType:
        
        return {
            "id": pet_id or fake.random_int(min=1, max=999999),
            "name": name or fake.first_name(),
            "category": {
                "id": category_id or fake.random_int(min=1, max=100),
                "name": category_name or fake.word().capitalize()
            },
            "photoUrls": photo_urls or [fake.image_url()],
            "tags": tags or [{"id": fake.random_int(min=1, max=100), "name": fake.word()}],
            "status": status
        }
    
    @staticmethod
    def generate_pet_with_multiple_photos() -> PetType:
        return PetDataGenerator.generate_pet_data(
            photo_urls=[fake.image_url() for _ in range(fake.random_int(min=2, max=5))]
        )
    
    @staticmethod
    def generate_pet_with_multiple_tags() -> PetType:
        tags = [{"id": i, "name": fake.word()} for i in range(1, fake.random_int(min=2, max=4))]
        return PetDataGenerator.generate_pet_data(tags=tags)

class OrderDataGenerator:    
    @staticmethod
    def generate_order_data(
        order_id: Optional[int] = None,
        pet_id: Optional[int] = None,
        quantity: int = 1,
        ship_date: Optional[str] = None,
        status: str = OrderStatus.PLACED,
        complete: bool = False
    ) -> OrderType:
        
        return {
            "id": order_id or fake.random_int(min=1, max=1000),
            "petId": pet_id or fake.random_int(min=1, max=999999),
            "quantity": quantity,
            "shipDate": ship_date or (datetime.now() + timedelta(days=1)).isoformat(),
            "status": status,
            "complete": complete
        }

class UserDataGenerator:    
    @staticmethod
    def generate_user_data(
        user_id: Optional[int] = None,
        username: Optional[str] = None,
        first_name: Optional[str] = None,
        last_name: Optional[str] = None,
        email: Optional[str] = None,
        password: Optional[str] = None,
        phone: Optional[str] = None,
        user_status: int = 0
    ) -> UserType:
        
        return {
            "id": user_id or fake.random_int(min=1, max=999999),
            "username": username or fake.user_name(),
            "firstName": first_name or fake.first_name(),
            "lastName": last_name or fake.last_name(),
            "email": email or fake.email(),
            "password": password or fake.password(),
            "phone": phone or fake.phone_number(),
            "userStatus": user_status
        }
    
    @staticmethod
    def generate_user_list(count: int = 3) -> List[UserType]:
        return [UserDataGenerator.generate_user_data() for _ in range(count)]