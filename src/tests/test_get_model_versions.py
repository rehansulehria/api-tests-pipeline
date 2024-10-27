import pytest

from src.tests.conftest import create_model

@pytest.mark.order(4)
def test_get_model_version(model_client, create_model, create_version):
    model_id_value, name_value = create_model
    response = model_client.get_model_versions(model_id_value)