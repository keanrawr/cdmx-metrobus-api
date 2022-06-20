FROM python:3.10-slim-buster

EXPOSE 8000

WORKDIR /app/
COPY . /app

RUN pip install pip --upgrade
RUN pip install poetry
RUN poetry install
# TODO: Use a non root user

CMD poetry run uvicorn app.main:app --host 0.0.0.0