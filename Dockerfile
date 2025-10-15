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

