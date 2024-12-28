
FROM python:3.10-slim


# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose a default port (if your script runs a server; otherwise, omit this line)
# EXPOSE 5000

# Command to run your Python script
CMD ["python", "ml_lab_exam_(aman_kumar_sinha).py"]

