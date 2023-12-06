from fastapi.testclient import TestClient
from ..controllers import payment_info as controller
from ..main import app
import pytest
from ..models import payment_info as model

# Create a test client for the app
client = TestClient(app)


@pytest.fixture
def db_session(mocker):
    return mocker.Mock()


def test_create_payment_info(db_session):
    # Create a sample order
    payment_info_data = {
        "payment_type": "Visa",
        "card_number": "1234567890",
        "exp_date": "12/2022",
        "transaction_status": "Success"
    }

    payment_info_object = model.PaymentInfo(**payment_info_data)

    # Call the create function
    created_payment_info_object = controller.create(db_session, payment_info_object)

    # Assertions
    assert created_payment_info_object is not None
    assert created_payment_info_object.payment_type == "Visa"
    assert created_payment_info_object.card_number == "1234567890"
    assert created_payment_info_object.exp_date == "12/2022"
    assert created_payment_info_object.transaction_status == "Success"

