FROM tecktron/python-bjoern:python-3.7

RUN apt-get update
RUN apt-get install -y python3-dev

WORKDIR /app
COPY requirements.txt /app

RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

COPY . /app

EXPOSE 8080