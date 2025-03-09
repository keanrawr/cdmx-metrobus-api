FROM python:3.12-slim-bookworm

EXPOSE 8000

WORKDIR /app/
COPY . /app

RUN pip install pip --upgrade
RUN pip install poetry
RUN poetry install --without dev
# TODO: Use a non root user

CMD ["poetry", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0"]
