FROM python:3.12-slim

# Install make and other build tools
RUN apt-get update && apt-get install -y make

RUN mkdir -p /usr/src/app

COPY requirements.txt /usr/src/app/
RUN pip install -U pip
RUN pip install -r /usr/src/app/requirements.txt
COPY . /usr/src/app
WORKDIR /usr/src/app
RUN pip install -e .
CMD ["make"]