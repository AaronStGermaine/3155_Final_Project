from fastapi.testclient import TestClient
from ..controllers import customers as controller
from ..main import app
import pytest
from ..models import customers as model

# Create a test client for the app
client = TestClient(app)


@pytest.fixture
def db_session(mocker):
    return mocker.Mock()


def test_create_customer(db_session):
    # Create a sample order
    customer_data = {
        "name": "John Doe",
        "email": "jdoe@gmail.com",
        "phone": "1234567890",
        "address": "123 Main St",
        "payment_id": 1,
        "member": True
    }

    customer_object = model.Customer(**customer_data)

    # Call the create function
    created_customer = controller.create(db_session, customer_object)

    # Assertions
    assert created_customer is not None
    assert created_customer.name == "John Doe"
    assert created_customer.email == "jdoe@gmail.com"
    assert created_customer.phone == "1234567890"
    assert created_customer.address == "123 Main St"
    assert created_customer.payment_id == 1
    assert created_customer.member is True
