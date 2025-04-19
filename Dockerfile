FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy everything from the backend folder into the container
COPY backend/ /app/backend/

# Install dependencies
RUN pip install --no-cache-dir -r /app/backend/requirements.txt

# Expose Flask port
EXPOSE 5000

# Run the Flask app
CMD ["python", "/app/backend/app.py"]
