import requests
from typing import Dict, Any, Optional
from config import BASE_URL, TIMEOUT, MAX_RETRIES

class BaseAPIClient:
    def __init__(self):
        self.base_url = BASE_URL
        self.session = requests.Session()
        self.session.headers.update({"Content-Type": "application/json"})
    
    def _request(self, method: str, endpoint: str, **kwargs) -> requests.Response:
        url = f"{self.base_url}{endpoint}"
        for attempt in range(MAX_RETRIES):
            try:
                response = self.session.request(method, url, timeout=TIMEOUT, **kwargs)
                return response
            except requests.exceptions.RequestException:
                if attempt == MAX_RETRIES - 1:
                    raise
    
    def _handle_response(self, response: requests.Response) -> Dict[str, Any]:
        try:
            return response.json()
        except ValueError:
            return {"status_code": response.status_code, "text": response.text}