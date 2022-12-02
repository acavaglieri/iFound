FROM python:3.9

WORKDIR /ifound_api

COPY ./requirements.txt /ifound_api/requirements.txt

RUN pip3 install -r requirements.txt

# Install dependencies
RUN apt-get update && apt-get install \ 
    -y --no-install-recommends \
    build-essential \
    mariadb-client