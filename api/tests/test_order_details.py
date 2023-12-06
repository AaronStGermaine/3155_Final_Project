from fastapi.testclient import TestClient
from ..controllers import order_details as controller
from ..main import app
import pytest
from ..models import order_details as model

# Create a test client for the app
client = TestClient(app)


@pytest.fixture
def db_session(mocker):
    return mocker.Mock()


def test_create_order_detail(db_session):
    # Create a sample order
    order_detail_data = {
        "order_id": "1",
        "food_id": "1",
        "promo_id": "1",
        "status": "1",
        "amount": "1"
    }

    order_detail_object = model.OrderDetail(**order_detail_data)

    # Call the create function
    created_order_detail = controller.create(db_session, order_detail_object)

    # Assertions
    assert created_order_detail is not None
    assert created_order_detail.order_id == "1"
    assert created_order_detail.food_id == "1"
    assert created_order_detail.promo_id == "1"
    assert created_order_detail.status == "1"
    assert created_order_detail.amount == "1"
