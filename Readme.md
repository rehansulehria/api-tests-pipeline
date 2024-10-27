## API Testing Pipeline
This project is a simple API testing pipeline that tests the API endpoints of server running on Docker container. The project uses Pytest as the testing framework and Requests library to make HTTP requests to the API endpoints. The project also uses Docker and Docker Compose to run the API server in a container.

### Prerequisites
- Python 3.6 or higher
- Docker
- Docker Compose
- Pytest
- Requests
- Pycharm or VsCode as IDE

# Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

# Pipeline Structure
The project has the following structure:
```
api-test-pipeline
│src
│   api
│   │   ├── __init__.py
│   │   ├── api_client.py
│   │   ├── data_generator.py
│   │   ├── model_client.py

│   tests
│   │   ├── __init__.py
│   │   ├── conftest.py
│   │   ├── test_create_model.py
│   │   ├── test_create_modal_validation.py
│   │   ├── test_get_model.py
│   │   ├── test_delete_model.py
│   │   ├── test_perform_inference.py
│   │   ├── test_get_model_version.py
│   │   ├── test_delete_modal_version.py
|Dockerfile
|docker-compose.yml
|requirements.txt
|README.md

```
1. Create Python Virtual Environment If not already setup to isolate dependencies:
```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
2. Clone the repository:
```bash
   git clone 
   ````
3. Install the dependencies:
 ```bash
   pip install -r requirements.txt
   ```
4. Start the API server using Docker:
```bash
   docker-compose up
```
5. Run the Tests
   ```bash
   cd src/tests && pytest -s
   ```
6. Run The Inside Docker Container
   ```bash
   docker build -t api-test-pipeline .
   docker run -it api-test-pipeline
   ```