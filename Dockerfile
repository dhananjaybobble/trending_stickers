FROM alpine:3.14

WORKDIR /api-server

RUN apt-get update && apt-get install -y python3 python3-dev python3-pip

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

CMD ["gunicorn", "--workers=4", "--worker-class=gevent", "--threads=4", "--bind=0.0.0.0:8111", "--access-logfile=-", "--error-logfile=-", "--log-level=debug", "wsgi:application"]
