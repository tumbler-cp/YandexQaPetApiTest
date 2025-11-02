from .pet_client import PetClient
from .store_client import StoreClient
from .user_client import UserClient
from typing import Dict, Any, List

class PetStoreAPIClient:
    def __init__(self):
        self.pet = PetClient()
        self.store = StoreClient()
        self.user = UserClient()
    
    def create_pet(self, pet_data: Dict[str, Any]) -> Dict[str, Any]:
        return self.pet.create_pet(pet_data)
    
    def get_pet_by_id(self, pet_id: int) -> Dict[str, Any]:
        return self.pet.get_pet_by_id(pet_id)
    
    def update_pet(self, pet_data: Dict[str, Any]) -> Dict[str, Any]:
        return self.pet.update_pet(pet_data)
    
    def delete_pet(self, pet_id: int) -> Dict[str, Any]:
        return self.pet.delete_pet(pet_id)
    
    def find_pets_by_status(self, status: str) -> List[Dict[str, Any]]:
        return self.pet.find_pets_by_status(status)
    
    def upload_pet_image(self, pet_id: int, file_data: Dict[str, Any]) -> Dict[str, Any]:
        return self.pet.upload_pet_image(pet_id, file_data)
    
    def create_order(self, order_data: Dict[str, Any]) -> Dict[str, Any]:
        return self.store.create_order(order_data)
    
    def get_order_by_id(self, order_id: int) -> Dict[str, Any]:
        return self.store.get_order_by_id(order_id)
    
    def delete_order(self, order_id: int) -> Dict[str, Any]:
        return self.store.delete_order(order_id)
    
    def get_inventory(self) -> Dict[str, Any]:
        return self.store.get_inventory()
    
    def create_user(self, user_data: Dict[str, Any]) -> Dict[str, Any]:
        return self.user.create_user(user_data)
    
    def get_user_by_username(self, username: str) -> Dict[str, Any]:
        return self.user.get_user_by_username(username)
    
    def update_user(self, username: str, user_data: Dict[str, Any]) -> Dict[str, Any]:
        return self.user.update_user(username, user_data)
    
    def delete_user(self, username: str) -> Dict[str, Any]:
        return self.user.delete_user(username)
    
    def login_user(self, username: str, password: str) -> Dict[str, Any]:
        return self.user.login_user(username, password)
    
    def logout_user(self) -> Dict[str, Any]:
        return self.user.logout_user()
    
    def create_users_with_list(self, users_data: List[Dict[str, Any]]) -> Dict[str, Any]:
        return self.user.create_users_with_list(users_data)