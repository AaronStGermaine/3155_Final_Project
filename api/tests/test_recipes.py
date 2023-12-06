from fastapi.testclient import TestClient
from ..controllers import recipes as controller
from ..main import app
import pytest
from ..models import recipes as model

# Create a test client for the app
client = TestClient(app)


@pytest.fixture
def db_session(mocker):
    return mocker.Mock()


def test_create_recipe(db_session):
    # Create a sample order
    recipe_data = {
        "food_id": "1",
        "resource_id": "1",
        "amount": "1"
    }

    recipe_object = model.Recipe(**recipe_data)

    # Call the create function
    created_rating = controller.create(db_session, recipe_object)

    # Assertions
    assert created_rating is not None
    assert created_rating.food_id == "1"
    assert created_rating.resource_id == "1"
    assert created_rating.amount == "1"
