# Use an official lightweight Python image as the base
    FROM python:3.10-slim

    # Set the working directory inside the container
    WORKDIR /app

    # Copy just the requirements file first to leverage Docker's layer caching
    COPY ids_app/requirements.txt .

    # Install the Python dependencies
    RUN pip install --no-cache-dir -r requirements.txt

    # Copy the rest of the application code into the container
    COPY ids_app/ .

    # Expose the port the app runs on
    EXPOSE 8000

    # The command to run when the container starts
    CMD ["python", "ids_script.py"]
    
