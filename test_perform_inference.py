import pytest

from src.api.data_generator import ModelTestData

@pytest.mark.order(3)
def test_perform_inference(model_client, create_model, create_version, model_test_data):
    model_id_value, name_value = create_model
    print(f"model_id_value is : {model_id_value}")
    version_id=create_version
    print(f"version_id is : {version_id}")
    inference_data=model_test_data.create_inference_data()
    response = model_client.perform_inference(model_id_value, version_id, inference_data)
    assert "predictions" in response
    assert response["predictions"] == [0.5, 0.3]
    assert response["model_id"] == model_id_value
    assert response["version_id"] == version_id
    assert response["model_name"] == name_value
