import pytest

from src.api.data_generator import ModelTestData
from src.api.model_client import ModelClient


@pytest.fixture(scope="session")
def model_client():
    base_url = "http://localhost:8000"  # base_url is the URL of the API
    return ModelClient(base_url=base_url)


@pytest.fixture(scope="session")
def model_test_data():
    """Fixture that provides an instance of ModelTestData for generating fake data."""
    return ModelTestData()


"""Fixture to create a model and return its ID."""


@pytest.fixture(scope="session")
def create_model(model_client, model_test_data):
    model_data = model_test_data.create_model_data()
    if model_data is not None:
        try:
            response = model_client.create_model(model_data)
            model_id_value = response.get("id")
            assert model_id_value is not None
            assert response.get("name") == model_data["name"]
            assert response.get("owner") == model_data["owner"]
            name = model_data["name"]
            yield model_id_value, name
        except Exception as e:
            print(f"Error creating model: {e}")


"""Fixture to create a version and return its ID."""


@pytest.fixture(scope="session")
def create_version(model_client, create_model):
    model_id_value, name_value = create_model
    print(f"model_id_value is: {model_id_value}")
    model_version_data = ModelTestData().create_model_version_data(name_value)
    if model_id_value is not None:
        try:
            response = model_client.create_version(model_id_value, model_version_data)
            assert response.get("id") is not None
            assert response.get("name") == model_version_data["name"]
            version_id = response.get("id")
            yield version_id
        except Exception as e:
            print(f"Error creating model version: {e}")
