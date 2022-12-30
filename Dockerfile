FROM python:3.8-slim-buster

WORKDIR /Sample2

RUN apt-get update && apt-get install -y python3 python3-dev python3-pip

COPY requirement.txt requirement.txt
RUN pip3 install -r requirement.txt


EXPOSE 5000
CMD [ "python", "-m", "flask", "run"]
