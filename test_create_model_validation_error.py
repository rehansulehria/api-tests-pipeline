import pytest
import requests

from src.tests.conftest import model_client

@pytest.mark.order(7)
def test_create_model_validation_error(model_test_data, model_client, create_model):
    model_data = model_test_data.create_model_validation_error()
    response = model_client.create_model(model_data)
    assert response["detail"][0]["msg"] == "Input should be a valid string", \
        f"Expected 'Input should be a valid string', got {response['detail'][0]['msg']}"