from typing import Dict, Any
from .base_client import BaseAPIClient
from .endpoints import StoreEndpoints

class StoreClient(BaseAPIClient):
    def create_order(self, order_data: Dict[str, Any]) -> Dict[str, Any]:
        response = self._request("POST", StoreEndpoints.ORDER, json=order_data)
        return self._handle_response(response)
    
    def get_order_by_id(self, order_id: int) -> Dict[str, Any]:
        response = self._request("GET", StoreEndpoints.ORDER_BY_ID.format(order_id))
        return self._handle_response(response)
    
    def delete_order(self, order_id: int) -> Dict[str, Any]:
        response = self._request("DELETE", StoreEndpoints.ORDER_BY_ID.format(order_id))
        return self._handle_response(response)
    
    def get_inventory(self) -> Dict[str, Any]:
        response = self._request("GET", StoreEndpoints.INVENTORY)
        return self._handle_response(response)