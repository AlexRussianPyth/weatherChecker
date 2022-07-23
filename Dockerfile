FROM python:3.10

RUN mkdir /api
WORKDIR /api

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
COPY ./requirements.txt requirements.txt

RUN  pip install --upgrade pip && pip install -r requirements.txt

COPY . .

ENTRYPOINT ["python3", "script.py"]
