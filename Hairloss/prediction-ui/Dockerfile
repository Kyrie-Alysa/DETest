# Using python 3.10.7-slim as base image
FROM python:3.10.7-slim

WORKDIR /usr/src/myapp
COPY requirements.txt .
# Install required python packages
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
# In prediction-api app.py last line shows the port which we want to expose
EXPOSE 5000
# Environment variables
ENV PREDICTOR_API=http://prediction-api-server:5000/hairloss_predictor

# Add some metadata to the image
LABEL prediction="0.0.1 mila"
# Specify the command to run on container start
CMD [ "python3", "app.py" ]