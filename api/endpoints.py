class PetEndpoints:
    PET = "/pet"
    PET_BY_ID = "/pet/{}"
    FIND_BY_STATUS = "/pet/findByStatus"
    UPLOAD_IMAGE = "/pet/{}/uploadImage"

class StoreEndpoints:
    ORDER = "/store/order"
    ORDER_BY_ID = "/store/order/{}"
    INVENTORY = "/store/inventory"

class UserEndpoints:
    USER = "/user"
    USER_BY_USERNAME = "/user/{}"
    LOGIN = "/user/login"
    LOGOUT = "/user/logout"
    CREATE_WITH_LIST = "/user/createWithList"
    CREATE_WITH_ARRAY = "/user/createWithArray"