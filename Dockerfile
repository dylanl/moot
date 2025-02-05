FROM python:3.8

WORKDIR /app

RUN pip install poetry

COPY pyproject.toml /app
COPY poetry.lock /app

RUN poetry install

COPY . /app

CMD ["poetry", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
