FROM python:3.11-slim

# Install system dependencies
RUN apt-get update && apt-get install -y build-essential

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy only the API directory
COPY ./src/api ./src/api

# Expose FastAPI port (usado solo por uvicorn)
EXPOSE ${PORT}

# Por default, arranca el servidor FastAPI
CMD uvicorn src.api.main:app --host ${HOST} --port ${PORT}


