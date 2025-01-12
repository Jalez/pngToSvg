FROM python:3.8-slim

WORKDIR /app

# Install system dependencies first (rarely changes)
RUN --mount=type=cache,target=/var/cache/apt \
    apt-get update && \
    apt-get install -y \
    potrace \
    libpotrace0 && \
    rm -rf /var/lib/apt/lists/* && \
    # Verify potrace installation
    potrace --version

# Copy only requirements first to leverage cache
COPY requirements.txt .

# Use BuildKit cache mount for pip
RUN --mount=type=cache,target=/root/.cache/pip \
    pip install --no-cache-dir -r requirements.txt

# Copy the application (changes frequently)
COPY . .

CMD ["python", "script.py"]
