# Use Python 3.11 base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements file
COPY ../requirements.txt .

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy the rest of your project
COPY ../ ./

# Expose port (example for FastAPI or Flask)
EXPOSE 8000

# Command to run your app (change as needed)
# For FastAPI: uvicorn app.main:app --host 0.0.0.0 --port 8000
# For Flask: python app.py
CMD ["python", "app.py"]
