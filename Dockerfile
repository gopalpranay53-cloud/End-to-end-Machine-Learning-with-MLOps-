# Dockerfile (recommended)
FROM python:3.8-slim-bullseye

ENV PYTHONUNBUFFERED=1
WORKDIR /app

# Install system deps needed for building wheels / unzip etc.
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    unzip \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# Install Python deps
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "app.py"]

