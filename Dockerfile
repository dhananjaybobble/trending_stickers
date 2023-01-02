FROM python:3.8-slim-buster

WORKDIR /sample


COPY requirement.txt requirement.txt
RUN pip3 install -r requirement.txt
COPY . .

EXPOSE 5000
CMD [ "flask", "run","--host","0.0.0.0","--port","5000"]