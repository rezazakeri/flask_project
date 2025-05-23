# Use the official Python image as the base
FROM python:3.12

# Set the working directory inside the container
WORKDIR /app

# Copy your project files into the container
COPY . .

#Install required Python packages inside the container
RUN pip install flask psycopg2-binary

#Set the command to run your flask app
CMD ["python","app.py"]

