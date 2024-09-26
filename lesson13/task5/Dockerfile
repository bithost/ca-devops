# Use Python 3.11 base image
FROM python:3.11-slim

# Set the working directory
WORKDIR /app

# Copy the necessary files
COPY requirements.txt /app/
COPY app.py /app/

# Install the required packages
RUN pip install -r requirements.txt

# Expose port 5000 to the outside world
EXPOSE 5000

# Run the Flask application
CMD ["python", "app.py"]
