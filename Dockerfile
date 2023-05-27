# Use the official Python image as the base image
FROM python:3.8

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the working directory
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code to the container
COPY . .

# Set the environment variables
ENV FLASK_APP=server.py
ENV FLASK_RUN_HOST=0.0.0.0

# Expose the port on which the Flask app will run
EXPOSE 8800

# Run the command to start the Flask app
CMD ["gunicorn", "server:app", "--bind", "0.0.0.0:8800"]
