# Use a Python base image
FROM python:3.11

# Set working directory
WORKDIR /app

# Copy the code into the container
COPY thousand_app.py .

# Install dependencies
RUN pip install requests

# Specify the command to run when the container starts
CMD [ "python", "thousand_app.py" ]
