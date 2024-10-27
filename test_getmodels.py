import pytest


@pytest.mark.order(5)
def test_getModels(model_client):
    response = model_client.get_models()
    assert response is not None
    assert type(response) == list