from fastapi.testclient import TestClient
from ..controllers import foods as controller
from ..main import app
import pytest
from ..models import foods as model

# Create a test client for the app
client = TestClient(app)


@pytest.fixture
def db_session(mocker):
    return mocker.Mock()


def test_create_food(db_session):
    # Create a sample order
    food_data = {
        "food_name": "Pizza",
        "food_category": "Italian",
        "food_ingredients": "Dough, Cheese, Sauce",
        "calories": 500,
        "price": 10.99
    }

    food_object = model.Food(**food_data)

    # Call the create function
    created_food = controller.create(db_session, food_object)

    # Assertions
    assert created_food is not None
    assert created_food.food_name == "Pizza"
    assert created_food.food_category == "Italian"
    assert created_food.food_ingredients == "Dough, Cheese, Sauce"
    assert created_food.calories == 500
    assert created_food.price == 10.99
