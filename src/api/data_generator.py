from faker import Faker
import uuid


class ModelTestData:
    def __init__(self):
        self.fake = Faker()

    def create_model_data(self) -> dict:
        """Generates data for creating a model."""
        return {
            "name": f"{self.fake.company()}_{uuid.uuid4()}",
            "owner": self.fake.name(),
        }

    def create_model_version_data(self, name) -> dict:
        """Generates data for creating a model version."""
        return {
            "name": name,
            "hugging_face_model": f"{self.fake.bs()}",
        }

    def create_model_version(self, model_id):
        """Generates invalid data for creating a model version."""
        return {
            "model_id": model_id,
            "version": "invalid_version",
            "description": self.fake.bs(),
        }

    def create_model_validation_error(self) -> dict:
        """Generates data for creating a model."""
        return {
            "name": f"{self.fake.company()}_{uuid.uuid4()}",
        }

    def create_inference_data(self) -> dict:
        """Generates data for inference."""
        return {
            "text": "Hi, how are you?"
        }
