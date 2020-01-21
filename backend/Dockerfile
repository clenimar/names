FROM python:3

COPY api.py /
COPY requirements.txt /
RUN mkdir /db

RUN pip3 install -r /requirements.txt

ENTRYPOINT [ "python3", "/api.py" ]