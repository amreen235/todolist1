# Use Python 3.9 slim image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy only the requirements file first (for better caching during builds)
COPY backend/requirements.txt /app/requirements.txt

# Install Python dependencies
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copy the entire application code into the container
COPY . /app

# Expose port 5000 (if that's the port your app uses)
EXPOSE 5000

# Set the entry point to run your app
CMD ["python", "backend/app.py"]
