### Ходжаев Абдужалол Абдужаборович
# Petstore API Autotest Project

## Описание

Проект автоматизированного тестирования для Petstore API (https://petstore.swagger.io). Тесты покрывают основные операции CRUD для трёх основных модулей API: Pet (Питомцы), Store (Магазин) и User (Пользователи).

## Установка

### Требования
- Python 3.8+
- pip

### Шаги установки

1. Клонируйте репозиторий:
```bash
git clone https://github.com/tumbler-cp/YandexQaPetApiTest.git
```

2. Создайте виртуальное окружение:
```bash
python -m venv .venv
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # Linux/Mac
```

3. Установите зависимости:
```bash
pip install -r requirements.txt
```

## Конфигурация

В файле `config.py` настраиваются основные параметры:

```python
BASE_URL = "https://petstore.swagger.io/v2"  # URL базовой API
TIMEOUT = 30  # Таймаут для запросов (секунды)
MAX_RETRIES = 3  # Количество повторов при ошибке
```

## Запуск тестов

### Все тесты
```bash
pytest
```

### Тесты по маркам
```bash
# Только тесты Pet API
pytest -m pets

# Только тесты Store API
pytest -m store

# Только тесты User API
pytest -m users

# Только CRUD тесты (create, read, update, delete)
pytest -m "create or read or update or delete" 

# Только edge cases
pytest -m edge_cases 

# Только boundary условия
pytest -m boundary 
```

### С минимальным выводом
```bash
pytest -q
```

### С подробной информацией об ошибках
```bash
pytest -v --tb=short
```

### С указанием директории allure
```bash
pytest --alluredir=allure-results
```

## Доступные маркеры

- `pets` - тесты Pet API
- `create` - тесты создания (CREATE)
- `read` - тесты чтения (READ)
- `update` - тесты обновления (UPDATE)
- `delete` - тесты удаления (DELETE)
- `store` - тесты Store API
- `orders` - тесты для заказов
- `inventory` - тесты инвентаря
- `users` - тесты User API
- `auth` - тесты аутентификации
- `edge_cases` - edge case тесты
- `pet_edge_cases` - edge cases для Pet API
- `order_edge_cases` - edge cases для Order API
- `user_edge_cases` - edge cases для User API
- `boundary` - boundary condition тесты

## Описание тестовых примеров

### Pet API (test_pet.py)
Покрытие основных операций с питомцами:
- **TestPetCreate**: создание питомцев с разными статусами и параметрами
- **TestPetRead**: получение информации о питомцах, поиск по статусу
- **TestPetUpdate**: обновление данных питомца
- **TestPetDelete**: удаление питомцев

### Store API (test_store.py)
Тесты для работы с заказами и инвентарем:
- **TestOrderCreate**: создание заказов
- **TestOrderRead**: получение информации о заказах
- **TestOrderDelete**: удаление заказов
- **TestInventory**: проверка инвентаря

### User API (test_user.py)
Тесты для работы с пользователями:
- **TestUserCreate**: создание пользователей (одиночные и списками)
- **TestUserRead**: получение информации о пользователях
- **TestUserUpdate**: обновление данных пользователя
- **TestUserDelete**: удаление пользователей
- **TestUserAuthentication**: логин/логаут и проверка аутентификации

### Edge Cases (test_edge_cases.py)
Тесты граничных случаев:
- **TestPetEdgeCases**: пустые имена, длинные имена, спецсимволы, пустые теги
- **TestOrderEdgeCases**: нулевые и очень большие количества
- **TestUserEdgeCases**: пустые пароли, спецсимволы в именах пользователя
- **TestBoundaryConditions**: поиск по всем статусам, проверка консистентности инвентаря

## Генерация тестовых данных

Проект использует библиотеку `Faker` для генерации случайных тестовых данных.

Основные классы генераторов в `util/data_generators.py`:
- `PetDataGenerator` - генерирует данные питомцев
- `OrderDataGenerator` - генерирует данные заказов
- `UserDataGenerator` - генерирует данные пользователей

Примеры использования:
```python
from util.data_generators import PetDataGenerator, PetStatus

# Генерирование простого питомца
pet = PetDataGenerator.generate_pet_data()

# С конкретным статусом
pet = PetDataGenerator.generate_pet_data(status=PetStatus.AVAILABLE)
```

## Fixtures

В `test/conftest.py` определены основные fixtures:

- `api_client` - основной API клиент
- `pet_client` - клиент для Pet API
- `store_client` - клиент для Store API
- `user_client` - клиент для User API
- `sample_pet` - тестовые данные питомца
- `sample_order` - тестовые данные заказа
- `sample_user` - тестовые данные пользователя
- `created_pet` - созданный питомец (с автоудалением после теста)
- `created_user` - созданный пользователь (с автоудалением после теста)
- `created_order` - созданный заказ (с автоудалением после теста)

## Статистика

- **Всего тестов**: 67
- **Тесты Pet API**: 20
- **Тесты Store API**: 14
- **Тесты User API**: 17
- **Edge cases**: 16

## Зависимости

- `pytest` - фреймворк для тестирования
- `requests` - библиотека для HTTP запросов
- `faker` - генератор случайных данных
- `pytest-allure` - интеграция с Allure 
