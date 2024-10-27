import requests

from src.api.api_client import ApiClient

class ModelClient(ApiClient):
    def create_model(self, model_data: dict) -> dict:
        return self.post("/models", model_data)

    def delete_model(self, model_id: str) -> requests.Response:
        return self.delete(f"/models/{model_id}")

    def get_models(self) -> list:
        response = requests.get(f"{self.base_url}/models")
        response.raise_for_status()
        return response.json()

    def create_version(self, model_id, version_data: dict) -> dict:
        return self.post(f"/models/{model_id}/versions", version_data)

    def get_model_versions(self, model_id: str) -> dict:
        return self.get(f"/models/{model_id}/versions")

    def delete_model_version(self, model_id: str, version_id: str) -> requests.Response:
        return self.delete(f"/models/{model_id}/versions/{version_id}")

    def perform_inference(self, model_id: str, version_id: str, input_data: dict) -> dict:
        return self.post(f"/models/{model_id}/versions/{version_id}/infer",
                         input_data)
