# Use official Python image
FROM python:3.11-slim

# Set working directory inside container
WORKDIR /app

# Copy the entire repo into the container
COPY . /app

# Upgrade pip and install dependencies
RUN pip install --upgrade pip \
    && pip install bandit pytest pytest-json-report fastapi[all] flask requests

# Create folders for reports
RUN mkdir -p reports/banditreports reports/unittest_reports

# Set environment variable for Python path inside container (optional)
ENV PYTHONPATH=/app

# Default command: run bash to allow manual execution
CMD ["bash"]
