from typing import Dict, Any, List
from .base_client import BaseAPIClient
from .endpoints import UserEndpoints

class UserClient(BaseAPIClient):
    def create_user(self, user_data: Dict[str, Any]) -> Dict[str, Any]:
        response = self._request("POST", UserEndpoints.USER, json=user_data)
        return self._handle_response(response)
    
    def get_user_by_username(self, username: str) -> Dict[str, Any]:
        response = self._request("GET", UserEndpoints.USER_BY_USERNAME.format(username))
        return self._handle_response(response)
    
    def update_user(self, username: str, user_data: Dict[str, Any]) -> Dict[str, Any]:
        response = self._request("PUT", UserEndpoints.USER_BY_USERNAME.format(username), json=user_data)
        return self._handle_response(response)
    
    def delete_user(self, username: str) -> Dict[str, Any]:
        response = self._request("DELETE", UserEndpoints.USER_BY_USERNAME.format(username))
        return self._handle_response(response)
    
    def login_user(self, username: str, password: str) -> Dict[str, Any]:
        response = self._request("GET", UserEndpoints.LOGIN, params={"username": username, "password": password})
        return self._handle_response(response)
    
    def logout_user(self) -> Dict[str, Any]:
        response = self._request("GET", UserEndpoints.LOGOUT)
        return self._handle_response(response)
    
    def create_users_with_list(self, users_data: List[Dict[str, Any]]) -> Dict[str, Any]:
        response = self._request("POST", UserEndpoints.CREATE_WITH_LIST, json=users_data)
        return self._handle_response(response)
    
    def create_users_with_array(self, users_data: List[Dict[str, Any]]) -> Dict[str, Any]:
        response = self._request("POST", UserEndpoints.CREATE_WITH_ARRAY, json=users_data)
        return self._handle_response(response)