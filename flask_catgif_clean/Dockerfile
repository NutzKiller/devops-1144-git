FROM python:3.10-slim

# Install necessary packages
RUN pip install flask requests

# Copy the application files
COPY . /app

WORKDIR /app

# Expose the port the app runs on
EXPOSE 5000

# Run the Flask app
CMD ["python", "app.py"]
