# Use a lightweight Python image as base
FROM python:3.9-slim AS builder

# Set working directory
WORKDIR /app

# Copy only requirements first for caching
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Use a second stage to reduce image size
FROM python:3.9-slim

# Set a non-root user for security
RUN useradd -m appuser
WORKDIR /app

# Ensure the app directory is owned by appuser
RUN chown -R appuser:appuser /app

# Switch to non-root user
USER appuser

# Copy installed dependencies and application files
COPY --from=builder /usr/local/lib/python3.9/site-packages /usr/local/lib/python3.9/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin
COPY . .

# Expose Flask application port
EXPOSE 5000

# Run Flask app
CMD ["python", "app.py"]
