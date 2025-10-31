# pull official base image
FROM python:3.10-slim-bullseye

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install mysql dependencies
RUN apt-get update && apt-get install -y gcc default-libmysqlclient-dev pkg-config

# install Node.js and npm
RUN apt-get install -y curl
RUN curl -fsSL https://deb.nodesource.com/setup_22.x | bash -
RUN apt-get install -y nodejs

# install dependencies
RUN pip install -U pip setuptools wheel
RUN pip install --upgrade pip


# install project dependencies
COPY ./requirements.txt .
RUN pip install -r requirements.txt --no-cache-dir

# copy project
COPY . .

# Convert plain text files from Windows or Mac format to Unix
RUN apt-get install dos2unix
RUN dos2unix --newfile docker-entrypoint.sh /usr/local/bin/docker-entrypoint.sh

# Make entrypoint executable
RUN chmod +x /usr/local/bin/docker-entrypoint.sh

# Entrypoint dependencies
RUN apt-get install netcat -y

# run entrypoint.sh
ENTRYPOINT ["bash", "/usr/local/bin/docker-entrypoint.sh"]
