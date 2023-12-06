from fastapi.testclient import TestClient
from ..controllers import ratings as controller
from ..main import app
import pytest
from ..models import ratings as model

# Create a test client for the app
client = TestClient(app)


@pytest.fixture
def db_session(mocker):
    return mocker.Mock()


def test_create_rating(db_session):
    # Create a sample order
    rating_data = {
        "stars": "1",
        "description": "Terrible",
        "order_id": "1"
    }

    rating_object = model.Rating(**rating_data)

    # Call the create function
    created_rating = controller.create(db_session, rating_object)

    # Assertions
    assert created_rating is not None
    assert created_rating.stars == "1"
    assert created_rating.description == "Terrible"
    assert created_rating.order_id == "1"
