# Dockerfile --> This is for a simulation, not a real production deployment!!!
# Use an official lightweight Python image.
FROM python:3.9-slim
# Set the working directory to /app
WORKDIR /app
# Copy the requirements file into the container
COPY requirements.txt .
# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
# Copy the rest of the application code
COPY . .
# Expose port 8000 and Run the application
EXPOSE 8000
CMD ["python", "main.py"] 
