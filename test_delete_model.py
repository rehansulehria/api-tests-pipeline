import pytest

@pytest.mark.order(-1)
def test_delete_model(model_client, create_model):
    model_id_value, name_value = create_model
    print(f"model_id_value is : {model_id_value}")
    resp = model_client.delete_model(model_id_value)
    assert resp.status_code == 200