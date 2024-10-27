# Dockerfile for running tester
FROM python:3.9
WORKDIR /app
# Copy requirements and install dependencies
COPY requirements.txt /app/
RUN pip install -r requirements.txt --no-cache-dir

# Copy all the rest of the code
COPY . .

CMD ["pytest", "src/tests/"]
