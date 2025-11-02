from typing import Dict, Any, List
from .base_client import BaseAPIClient
from .endpoints import PetEndpoints

class PetClient(BaseAPIClient):
    def create_pet(self, pet_data: Dict[str, Any]) -> Dict[str, Any]:
        response = self._request("POST", PetEndpoints.PET, json=pet_data)
        return self._handle_response(response)
    
    def get_pet_by_id(self, pet_id: int) -> Dict[str, Any]:
        response = self._request("GET", PetEndpoints.PET_BY_ID.format(pet_id))
        return self._handle_response(response)
    
    def update_pet(self, pet_data: Dict[str, Any]) -> Dict[str, Any]:
        response = self._request("PUT", PetEndpoints.PET, json=pet_data)
        return self._handle_response(response)
    
    def delete_pet(self, pet_id: int) -> Dict[str, Any]:
        response = self._request("DELETE", PetEndpoints.PET_BY_ID.format(pet_id))
        return self._handle_response(response)
    
    def find_pets_by_status(self, status: str) -> List[Dict[str, Any]]:
        response = self._request("GET", PetEndpoints.FIND_BY_STATUS, params={"status": status})
        return self._handle_response(response)
    
    def update_pet_with_form(self, pet_id: int, form_data: Dict[str, Any]) -> Dict[str, Any]:
        response = self._request("POST", PetEndpoints.PET_BY_ID.format(pet_id), data=form_data)
        return self._handle_response(response)
    
    def upload_pet_image(self, pet_id: int, file_data: Dict[str, Any]) -> Dict[str, Any]:
        response = self._request("POST", PetEndpoints.UPLOAD_IMAGE.format(pet_id), files=file_data)
        return self._handle_response(response)