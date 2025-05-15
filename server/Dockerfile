# Use Python 3.11 as base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements first to leverage Docker cache
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . .

# Create a non-root user
RUN useradd -m appuser

# Switch to non-root user
USER appuser

# Expose the port the app runs on
EXPOSE 8001

# Command to run the application
CMD ["uvicorn", "server.main:app", "--host", "0.0.0.0", "--port", "8001"] 