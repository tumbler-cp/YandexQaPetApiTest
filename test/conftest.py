import pytest
import allure
from api.full_client import PetStoreAPIClient
from util.data_generators import PetDataGenerator, OrderDataGenerator, UserDataGenerator

@pytest.fixture
def api_client():
    return PetStoreAPIClient()

@pytest.fixture
def pet_client(api_client):
    return api_client.pet

@pytest.fixture
def store_client(api_client):
    return api_client.store

@pytest.fixture
def user_client(api_client):
    return api_client.user

@pytest.fixture
def sample_pet():
    return PetDataGenerator.generate_pet_data()

@pytest.fixture
def sample_order():
    return OrderDataGenerator.generate_order_data()

@pytest.fixture
def sample_user():
    return UserDataGenerator.generate_user_data()

@pytest.fixture
def created_pet(pet_client, sample_pet):
    response = pet_client.create_pet(sample_pet)
    assert response.get("id") == sample_pet["id"]
    yield sample_pet
    pet_client.delete_pet(sample_pet["id"])

@pytest.fixture
def created_user(user_client, sample_user):
    response = user_client.create_user(sample_user)
    assert response.get("code") == 200
    yield sample_user
    user_client.delete_user(sample_user["username"])

@pytest.fixture
def created_order(store_client, created_pet, sample_order):
    order_data = sample_order.copy()
    order_data["petId"] = created_pet["id"]
    response = store_client.create_order(order_data)
    assert response.get("id") == order_data["id"]
    yield order_data
    store_client.delete_order(order_data["id"])