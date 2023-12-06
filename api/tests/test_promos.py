from fastapi.testclient import TestClient
from ..controllers import promos as controller
from ..main import app
import pytest
from ..models import promos as model

# Create a test client for the app
client = TestClient(app)


@pytest.fixture
def db_session(mocker):
    return mocker.Mock()


def test_create_promo(db_session):
    # Create a sample order
    promo_data = {
        "promo_name": "Test Promo",
        "discount": "1.99",
        "expiration_date": "2021-10-01"
    }

    promo_object = model.Promo(**promo_data)

    # Call the create function
    created_promo = controller.create(db_session, promo_object)

    # Assertions
    assert created_promo is not None
    assert created_promo.promo_name == "Test Promo"
    assert created_promo.discount == "1.99"
    assert created_promo.expiration_date == "2021-10-01"
