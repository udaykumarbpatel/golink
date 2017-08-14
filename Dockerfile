FROM python:2.7.13-slim

RUN mkdir /opt/golink-app

WORKDIR /opt/golink-app

ADD . .

RUN pip install -r requirement.txt

EXPOSE 5000

ENV FLASK_APP=myflaskapp.py

CMD ["flask", "run", "--host", "0.0.0.0"]
