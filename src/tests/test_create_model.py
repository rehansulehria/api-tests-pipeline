from importlib.metadata import version

import pytest

from src.api.data_generator import ModelTestData

@pytest.mark.order(1)
def test_create_model(create_model):
    # assert model_id is not None from the model_id fixture
    assert create_model is not None

@pytest.mark.order(2)
def test_create_model_version(model_client, create_model, create_version):
    assert create_model is not None
    assert create_version is not None