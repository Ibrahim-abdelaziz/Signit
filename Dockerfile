FROM python:3.7-alpine


EXPOSE 5000


RUN apk update && apk add curl postgresql-dev gcc python3-dev musl-dev curl git openssh-client

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements /app/requirements

WORKDIR /app
ENV FLASK_APP autoapp.py
ENV FLASK_ENV production

RUN pip install -r requirements/base.txt

COPY . /app

CMD gunicorn --bind 0.0.0.0:5000
