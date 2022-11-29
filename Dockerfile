FROM python:3.8.13-slim-buster

LABEL maintainer="trydocker@gmail.com"

# set working directory
RUN mkdir app
WORKDIR /app

# python env variables pyc to disk false, stdout&stderror false
ENV PYTHONBUFFERED 1    
# ENV PYTHONDONTWRITEBYTECODE 1  

#COPY requirements.txt requirements.txt

COPY . .

# apk add --no-cache gcc musl-dev python3-dev && \
RUN python3 -m venv /venv && \
    /venv/bin/pip install --upgrade pip && \
    /venv/bin/pip install --upgrade pip wheel && \
    /venv/bin/pip install -r requirements.txt && \
    adduser --disabled-password --no-create-home user

ENV PATH="/venv/bin:$PATH"
ENV PORT=8000

USER user

CMD gunicorn cd CoreBackend && gunicorn blightcnncore.wsgi:application --bind 0.0.0.0:$PORT