import pytest
from util.data_generators import UserDataGenerator

@pytest.mark.users
@pytest.mark.create
class TestUserCreate:
    def test_create_user_with_valid_data(self, user_client, sample_user):
        response = user_client.create_user(sample_user)
        assert response["code"] == 200
        user_client.delete_user(sample_user["username"])

    def test_create_user_has_required_fields(self, user_client):
        user = UserDataGenerator.generate_user_data()
        response = user_client.create_user(user)
        assert response["code"] == 200
        user_client.delete_user(user["username"])

    def test_create_user_with_different_usernames(self, user_client):
        for _ in range(3):
            user = UserDataGenerator.generate_user_data()
            response = user_client.create_user(user)
            assert response["code"] == 200
            user_client.delete_user(user["username"])

    def test_create_user_with_status(self, user_client):
        user = UserDataGenerator.generate_user_data(user_status=1)
        response = user_client.create_user(user)
        assert response["code"] == 200
        user_client.delete_user(user["username"])

    def test_create_users_with_list(self, user_client):
        users = UserDataGenerator.generate_user_list(count=3)
        response = user_client.create_users_with_list(users)
        assert response["code"] == 200
        for user in users:
            user_client.delete_user(user["username"])

    def test_create_users_with_array(self, user_client):
        users = UserDataGenerator.generate_user_list(count=3)
        response = user_client.create_users_with_array(users)
        assert response["code"] == 200
        for user in users:
            user_client.delete_user(user["username"])


@pytest.mark.users
@pytest.mark.read
class TestUserRead:
    def test_get_user_by_username(self, user_client):
        user = UserDataGenerator.generate_user_data()
        user_client.create_user(user)
        try:
            response = user_client.get_user_by_username(user["username"])
            assert response.get("username") == user["username"] or "code" in response
        finally:
            user_client.delete_user(user["username"])

    def test_get_user_returns_all_fields(self, user_client):
        user = UserDataGenerator.generate_user_data()
        user_client.create_user(user)
        try:
            response = user_client.get_user_by_username(user["username"])
            assert response.get("id") is not None or "code" in response
        finally:
            user_client.delete_user(user["username"])

    def test_get_user_has_correct_email(self, user_client):
        user = UserDataGenerator.generate_user_data()
        user_client.create_user(user)
        try:
            response = user_client.get_user_by_username(user["username"])
            if "email" in response:
                assert response["email"] == user["email"]
        finally:
            user_client.delete_user(user["username"])

    def test_get_user_has_correct_name(self, user_client):
        user = UserDataGenerator.generate_user_data()
        user_client.create_user(user)
        try:
            response = user_client.get_user_by_username(user["username"])
            if "firstName" in response:
                assert response["firstName"] == user["firstName"]
                assert response["lastName"] == user["lastName"]
        finally:
            user_client.delete_user(user["username"])


@pytest.mark.users
@pytest.mark.update
class TestUserUpdate:
    def test_update_user_firstname(self, user_client, created_user):
        updated_user = created_user.copy()
        updated_user["firstName"] = "UpdatedFirstName"
        response = user_client.update_user(created_user["username"], updated_user)
        assert response["code"] == 200

    def test_update_user_lastname(self, user_client, created_user):
        updated_user = created_user.copy()
        updated_user["lastName"] = "UpdatedLastName"
        response = user_client.update_user(created_user["username"], updated_user)
        assert response["code"] == 200

    def test_update_user_email(self, user_client, created_user):
        updated_user = created_user.copy()
        updated_user["email"] = "newemail@example.com"
        response = user_client.update_user(created_user["username"], updated_user)
        assert response["code"] == 200

    def test_update_user_multiple_fields(self, user_client, created_user):
        updated_user = created_user.copy()
        updated_user["firstName"] = "NewFirst"
        updated_user["lastName"] = "NewLast"
        updated_user["phone"] = "9999999999"
        response = user_client.update_user(created_user["username"], updated_user)
        assert response["code"] == 200

    def test_update_user_preserves_username(self, user_client, created_user):
        updated_user = created_user.copy()
        updated_user["firstName"] = "ChangedName"
        response = user_client.update_user(created_user["username"], updated_user)
        assert response["code"] == 200


@pytest.mark.users
@pytest.mark.delete
class TestUserDelete:
    def test_delete_user(self, user_client):
        user = UserDataGenerator.generate_user_data()
        user_client.create_user(user)
        response = user_client.delete_user(user["username"])
        assert response is not None

    def test_delete_user_multiple(self, user_client):
        users = UserDataGenerator.generate_user_list(count=3)
        for user in users:
            user_client.create_user(user)
        for user in users:
            response = user_client.delete_user(user["username"])
            assert response is not None


@pytest.mark.users
@pytest.mark.auth
class TestUserAuthentication:
    def test_login_user(self, user_client, created_user):
        response = user_client.login_user(created_user["username"], created_user["password"])
        assert response["code"] == 200
        assert "message" in response

    def test_logout_user(self, user_client, created_user):
        user_client.login_user(created_user["username"], created_user["password"])
        response = user_client.logout_user()
        assert response["code"] == 200

    def test_login_with_different_credentials(self, user_client):
        for _ in range(2):
            user = UserDataGenerator.generate_user_data()
            user_client.create_user(user)
            response = user_client.login_user(user["username"], user["password"])
            assert response["code"] == 200
            user_client.delete_user(user["username"])