# Use the official Python image from the Docker Hub
FROM python:3.8-slim-buster

# Install necessary packages
RUN apt-get update \
    && apt-get install -y libpq-dev gcc \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /py-docker

# Copy the requirements file and install dependencies
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose port 5000
EXPOSE 5000

# Set the default environment variable for port
ENV PORT=5000

# Command to run the Flask application
CMD ["python", "app.py"]
