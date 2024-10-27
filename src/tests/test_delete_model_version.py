import pytest

@pytest.mark.order(5)
def test_delete_model_version(model_client, create_model, create_version):
    model_id_value, name_value = create_model
    version_id_value = create_version
    print(f"model_id_value is : {model_id_value}")
    print(f"version_id_value is : {version_id_value}")
    response = model_client.delete_model_version(model_id_value, version_id_value)
    assert response.status_code == 200