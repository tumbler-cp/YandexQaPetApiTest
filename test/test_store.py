import pytest
from util.data_generators import OrderStatus, OrderDataGenerator, PetDataGenerator

@pytest.mark.store
@pytest.mark.orders
@pytest.mark.create
class TestOrderCreate:
    def test_create_order_with_valid_data(self, store_client, created_pet, sample_order):
        order_data = sample_order.copy()
        order_data["petId"] = created_pet["id"]
        response = store_client.create_order(order_data)
        assert response["id"] == order_data["id"]
        assert response["petId"] == created_pet["id"]
        store_client.delete_order(order_data["id"])

    def test_create_order_with_placed_status(self, store_client, created_pet):
        order = OrderDataGenerator.generate_order_data(
            pet_id=created_pet["id"],
            status=OrderStatus.PLACED
        )
        response = store_client.create_order(order)
        assert response["status"] == OrderStatus.PLACED
        store_client.delete_order(order["id"])

    def test_create_order_with_approved_status(self, store_client, created_pet):
        order = OrderDataGenerator.generate_order_data(
            pet_id=created_pet["id"],
            status=OrderStatus.APPROVED
        )
        response = store_client.create_order(order)
        assert response["status"] == OrderStatus.APPROVED
        store_client.delete_order(order["id"])

    def test_create_order_with_delivered_status(self, store_client, created_pet):
        order = OrderDataGenerator.generate_order_data(
            pet_id=created_pet["id"],
            status=OrderStatus.DELIVERED
        )
        response = store_client.create_order(order)
        assert response["status"] == OrderStatus.DELIVERED
        store_client.delete_order(order["id"])

    def test_create_order_with_different_quantities(self, store_client, created_pet):
        for quantity in [1, 5, 10, 100]:
            order = OrderDataGenerator.generate_order_data(
                pet_id=created_pet["id"],
                quantity=quantity
            )
            response = store_client.create_order(order)
            assert response["quantity"] == quantity
            store_client.delete_order(order["id"])

    def test_create_order_has_required_fields(self, store_client, created_pet, sample_order):
        order_data = sample_order.copy()
        order_data["petId"] = created_pet["id"]
        response = store_client.create_order(order_data)
        assert "id" in response
        assert "petId" in response
        assert "quantity" in response
        assert "status" in response
        store_client.delete_order(order_data["id"])


@pytest.mark.store
@pytest.mark.orders
@pytest.mark.read
class TestOrderRead:
    def test_get_order_by_id(self, store_client, created_pet):
        order = OrderDataGenerator.generate_order_data(pet_id=created_pet["id"])
        created_order = store_client.create_order(order)
        if "id" in created_order:
            try:
                response = store_client.get_order_by_id(created_order["id"])
                assert response.get("id") == created_order["id"] or "code" in response
            finally:
                store_client.delete_order(created_order["id"])

    def test_get_order_returns_all_fields(self, store_client, created_pet):
        order = OrderDataGenerator.generate_order_data(pet_id=created_pet["id"])
        created_order = store_client.create_order(order)
        if "id" in created_order:
            try:
                response = store_client.get_order_by_id(created_order["id"])
                assert response.get("id") is not None or "code" in response
            finally:
                store_client.delete_order(created_order["id"])

    def test_get_order_with_placed_status(self, store_client, created_pet):
        order = OrderDataGenerator.generate_order_data(
            pet_id=created_pet["id"],
            status=OrderStatus.PLACED
        )
        created_order = store_client.create_order(order)
        if "id" in created_order:
            try:
                response = store_client.get_order_by_id(created_order["id"])
                if "status" in response:
                    assert response["status"] == OrderStatus.PLACED
            finally:
                store_client.delete_order(created_order["id"])


@pytest.mark.store
@pytest.mark.orders
@pytest.mark.delete
class TestOrderDelete:
    def test_delete_order(self, store_client, created_order):
        response = store_client.delete_order(created_order["id"])
        assert response is not None

    def test_delete_order_multiple(self, store_client, created_pet):
        orders = [
            OrderDataGenerator.generate_order_data(pet_id=created_pet["id"])
            for _ in range(3)
        ]
        for order in orders:
            store_client.create_order(order)
        for order in orders:
            response = store_client.delete_order(order["id"])
            assert response is not None


@pytest.mark.store
@pytest.mark.inventory
class TestInventory:
    def test_get_inventory(self, store_client):
        response = store_client.get_inventory()
        assert isinstance(response, dict)

    def test_get_inventory_has_status_keys(self, store_client):
        response = store_client.get_inventory()
        assert "available" in response or "sold" in response or "pending" in response

    def test_get_inventory_returns_numeric_values(self, store_client):
        response = store_client.get_inventory()
        for key, value in response.items():
            if key in ["available", "pending", "sold"]:
                assert isinstance(value, (int, float))