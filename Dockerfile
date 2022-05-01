FROM python:3.8.0

RUN mkdir /srv/docker-server
ADD . /srv/docker-server

WORKDIR /srv/docker-server


COPY . .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python","server.py"]


