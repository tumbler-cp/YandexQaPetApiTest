import pytest
from util.data_generators import (
    PetDataGenerator,
    OrderDataGenerator,
    UserDataGenerator,
    PetStatus,
    OrderStatus
)

@pytest.mark.edge_cases
@pytest.mark.pet_edge_cases
class TestPetEdgeCases:
    def test_create_pet_with_empty_name(self, pet_client):
        pet = PetDataGenerator.generate_pet_data(name="")
        response = pet_client.create_pet(pet)
        assert response["id"] == pet["id"]
        pet_client.delete_pet(pet["id"])

    def test_create_pet_with_very_long_name(self, pet_client):
        pet = PetDataGenerator.generate_pet_data(name="A" * 500)
        response = pet_client.create_pet(pet)
        assert response["id"] == pet["id"]
        pet_client.delete_pet(pet["id"])

    def test_create_pet_with_special_characters_in_name(self, pet_client):
        pet = PetDataGenerator.generate_pet_data(name="Pet@#$%^&*()_+-=")
        response = pet_client.create_pet(pet)
        assert response["id"] == pet["id"]
        pet_client.delete_pet(pet["id"])

    def test_pet_with_no_tags(self, pet_client):
        pet = PetDataGenerator.generate_pet_data(tags=[])
        response = pet_client.create_pet(pet)
        assert response["id"] == pet["id"]
        pet_client.delete_pet(pet["id"])

    def test_pet_update_to_different_status(self, pet_client):
        pet = PetDataGenerator.generate_pet_data(status=PetStatus.AVAILABLE)
        pet_client.create_pet(pet)
        try:
            pet["status"] = PetStatus.SOLD
            response = pet_client.update_pet(pet)
            assert response["status"] == PetStatus.SOLD
        finally:
            pet_client.delete_pet(pet["id"])



@pytest.mark.edge_cases
@pytest.mark.order_edge_cases
class TestOrderEdgeCases:
    def test_create_order_with_zero_quantity(self, store_client, created_pet):
        order = OrderDataGenerator.generate_order_data(
            pet_id=created_pet["id"],
            quantity=0
        )
        response = store_client.create_order(order)
        assert response["quantity"] == 0
        store_client.delete_order(order["id"])

    def test_create_order_with_large_quantity(self, store_client, created_pet):
        order = OrderDataGenerator.generate_order_data(
            pet_id=created_pet["id"],
            quantity=999999
        )
        response = store_client.create_order(order)
        assert response["quantity"] == 999999
        store_client.delete_order(order["id"])


@pytest.mark.edge_cases
@pytest.mark.user_edge_cases
class TestUserEdgeCases:
    def test_create_user_with_empty_password(self, user_client):
        user = UserDataGenerator.generate_user_data(password="")
        response = user_client.create_user(user)
        assert response["code"] == 200
        user_client.delete_user(user["username"])

    def test_create_user_with_special_characters_username(self, user_client):
        user = UserDataGenerator.generate_user_data(username="user_123@test")
        response = user_client.create_user(user)
        assert response["code"] == 200
        user_client.delete_user(user["username"])

    def test_create_user_with_long_email(self, user_client):
        user = UserDataGenerator.generate_user_data(email="a" * 100 + "@example.com")
        response = user_client.create_user(user)
        assert response["code"] == 200
        user_client.delete_user(user["username"])

    def test_user_status_boundary_values(self, user_client):
        for status in [0, 1, -1]:
            user = UserDataGenerator.generate_user_data(user_status=status)
            response = user_client.create_user(user)
            assert response["code"] == 200
            user_client.delete_user(user["username"])


@pytest.mark.edge_cases
@pytest.mark.boundary
class TestBoundaryConditions:
    def test_find_pets_with_all_statuses(self, pet_client):
        statuses = [PetStatus.AVAILABLE, PetStatus.PENDING, PetStatus.SOLD]
        for status in statuses:
            pet = PetDataGenerator.generate_pet_data(status=status)
            pet_client.create_pet(pet)
            response = pet_client.find_pets_by_status(status)
            assert isinstance(response, list)
            pet_client.delete_pet(pet["id"])

    def test_inventory_consistency(self, store_client):
        response = store_client.get_inventory()
        for key, value in response.items():
            assert isinstance(value, (int, float)) or value is None
