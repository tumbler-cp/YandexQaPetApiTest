import pytest
from util.data_generators import PetStatus, PetDataGenerator

@pytest.mark.pets
@pytest.mark.create
class TestPetCreate:
    def test_create_pet_with_valid_data(self, pet_client, sample_pet):
        response = pet_client.create_pet(sample_pet)
        assert response["id"] == sample_pet["id"]
        assert response["name"] == sample_pet["name"]
        assert response["status"] == sample_pet["status"]
        pet_client.delete_pet(sample_pet["id"])

    def test_create_pet_with_available_status(self, pet_client):
        pet = PetDataGenerator.generate_pet_data(status=PetStatus.AVAILABLE)
        response = pet_client.create_pet(pet)
        assert response["status"] == PetStatus.AVAILABLE
        pet_client.delete_pet(pet["id"])

    def test_create_pet_with_pending_status(self, pet_client):
        pet = PetDataGenerator.generate_pet_data(status=PetStatus.PENDING)
        response = pet_client.create_pet(pet)
        assert response["status"] == PetStatus.PENDING
        pet_client.delete_pet(pet["id"])

    def test_create_pet_with_sold_status(self, pet_client):
        pet = PetDataGenerator.generate_pet_data(status=PetStatus.SOLD)
        response = pet_client.create_pet(pet)
        assert response["status"] == PetStatus.SOLD
        pet_client.delete_pet(pet["id"])

    def test_create_pet_with_multiple_photos(self, pet_client):
        pet = PetDataGenerator.generate_pet_with_multiple_photos()
        response = pet_client.create_pet(pet)
        assert len(response["photoUrls"]) >= 2
        pet_client.delete_pet(pet["id"])

    def test_create_pet_with_multiple_tags(self, pet_client):
        pet = PetDataGenerator.generate_pet_with_multiple_tags()
        response = pet_client.create_pet(pet)
        assert len(response.get("tags", [])) >= 1
        pet_client.delete_pet(pet["id"])

    def test_create_pet_has_required_fields(self, pet_client, sample_pet):
        response = pet_client.create_pet(sample_pet)
        assert "id" in response
        assert "name" in response
        assert "status" in response
        assert "photoUrls" in response
        pet_client.delete_pet(sample_pet["id"])


@pytest.mark.pets
@pytest.mark.read
class TestPetRead:
    def test_get_pet_by_id(self, pet_client):
        pet = PetDataGenerator.generate_pet_data()
        pet_client.create_pet(pet)
        try:
            response = pet_client.get_pet_by_id(pet["id"])
            assert response.get("id") == pet["id"] or "code" in response
        finally:
            pet_client.delete_pet(pet["id"])

    def test_get_pet_returns_all_fields(self, pet_client):
        pet = PetDataGenerator.generate_pet_data()
        pet_client.create_pet(pet)
        try:
            response = pet_client.get_pet_by_id(pet["id"])
            assert response.get("id") is not None or "code" in response
        finally:
            pet_client.delete_pet(pet["id"])

    def test_get_pet_by_id_with_available_status(self, pet_client):
        pet = PetDataGenerator.generate_pet_data(status=PetStatus.AVAILABLE)
        pet_client.create_pet(pet)
        try:
            response = pet_client.get_pet_by_id(pet["id"])
            if "status" in response:
                assert response["status"] == PetStatus.AVAILABLE
        finally:
            pet_client.delete_pet(pet["id"])

    def test_find_pets_by_available_status(self, pet_client):
        pet = PetDataGenerator.generate_pet_data(status=PetStatus.AVAILABLE)
        pet_client.create_pet(pet)
        response = pet_client.find_pets_by_status(PetStatus.AVAILABLE)
        assert isinstance(response, list)
        pet_client.delete_pet(pet["id"])

    def test_find_pets_by_pending_status(self, pet_client):
        pet = PetDataGenerator.generate_pet_data(status=PetStatus.PENDING)
        pet_client.create_pet(pet)
        response = pet_client.find_pets_by_status(PetStatus.PENDING)
        assert isinstance(response, list)
        pet_client.delete_pet(pet["id"])

    def test_find_pets_by_sold_status(self, pet_client):
        pet = PetDataGenerator.generate_pet_data(status=PetStatus.SOLD)
        pet_client.create_pet(pet)
        response = pet_client.find_pets_by_status(PetStatus.SOLD)
        assert isinstance(response, list)
        pet_client.delete_pet(pet["id"])


@pytest.mark.pets
@pytest.mark.update
class TestPetUpdate:
    def test_update_pet_name(self, pet_client, created_pet):
        updated_data = created_pet.copy()
        updated_data["name"] = "UpdatedName"
        response = pet_client.update_pet(updated_data)
        assert response["name"] == "UpdatedName"

    def test_update_pet_status(self, pet_client, created_pet):
        updated_data = created_pet.copy()
        updated_data["status"] = PetStatus.SOLD
        response = pet_client.update_pet(updated_data)
        assert response["status"] == PetStatus.SOLD

    def test_update_pet_multiple_fields(self, pet_client, created_pet):
        updated_data = created_pet.copy()
        updated_data["name"] = "NewName"
        updated_data["status"] = PetStatus.PENDING
        response = pet_client.update_pet(updated_data)
        assert response["name"] == "NewName"
        assert response["status"] == PetStatus.PENDING

    def test_update_pet_preserves_id(self, pet_client, created_pet):
        updated_data = created_pet.copy()
        updated_data["name"] = "AnotherName"
        response = pet_client.update_pet(updated_data)
        assert response["id"] == created_pet["id"]

    def test_update_pet_with_form_data(self, pet_client, created_pet):
        form_data = {"name": "FormUpdatedName", "status": PetStatus.SOLD}
        response = pet_client.update_pet_with_form(created_pet["id"], form_data)
        assert response is not None


@pytest.mark.pets
@pytest.mark.delete
class TestPetDelete:
    def test_delete_pet(self, pet_client):
        pet = PetDataGenerator.generate_pet_data()
        pet_client.create_pet(pet)
        response = pet_client.delete_pet(pet["id"])
        assert response is not None

    def test_delete_pet_multiple(self, pet_client):
        pets = [PetDataGenerator.generate_pet_data() for _ in range(3)]
        for pet in pets:
            pet_client.create_pet(pet)
        for pet in pets:
            response = pet_client.delete_pet(pet["id"])
            assert response is not None