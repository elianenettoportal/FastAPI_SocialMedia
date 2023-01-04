FROM python:3.10.6
# Run commands from /FastAPI_SocialMedia directory inside container
WORKDIR /FastAPI_SocialMedia
# Copy requirements from local to docker image
COPY requirements.txt /FastAPI_SocialMedia
# Install the dependencies in the docker image
RUN pip3 install -r requirements.txt --no-cache-dir
# Copy everything from the current dir to the image
COPY . .