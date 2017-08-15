FROM python:2.7.13-slim

RUN apt-get update && apt-get install -y git

RUN git clone https://github.com/udaykumarbpatel/golink.git

RUN cd golink

WORKDIR golink

RUN pip install -r requirement.txt

EXPOSE 5000

ENV FLASK_APP=myflaskapp.py

CMD ["flask", "run", "--host", "0.0.0.0"]
