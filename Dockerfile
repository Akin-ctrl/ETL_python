# Base image
FROM python:3.12

# Set working directory
WORKDIR /app

# Copy files
COPY requirements.txt .
RUN pip install --default-timeout=100 -r requirements.txt

# RUN pip install -r requirements.txt

COPY . .

# Run the ETL script
CMD ["python", "etl.py"]

# # Use Python 3.12 as base image
# FROM python:3.12-slim

# # Set environment variables
# ENV PYTHONDONTWRITEBYTECODE=1 \
#     PYTHONUNBUFFERED=1 \
#     PIP_NO_CACHE_DIR=off \
#     PIP_DISABLE_PIP_VERSION_CHECK=on \
#     PIP_DEFAULT_TIMEOUT=100

# # Create app directory
# WORKDIR /app

# # Copy requirements and ETL files into container
# COPY . .

# # Retry logic for pip install due to potential timeout issues
# RUN apt-get update && apt-get install -y curl && \
#     pip install --upgrade pip && \
#     bash -c ' \
#         for i in {1..5}; do \
#             pip install -r requirements.txt && break || sleep 15; \
#         done \
#     '

# # Set default command (can be overridden in docker-compose or CLI)
# CMD ["python", "extract.py"]
