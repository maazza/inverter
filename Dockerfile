FROM python:3.10-alpine

ARG ROOT=/source
WORKDIR ${ROOT}

RUN pip install poetry

COPY pyproject.toml poetry.lock ${ROOT}/

RUN poetry config virtualenvs.create false
RUN poetry install

COPY . .

CMD ["uvicorn", "--reload", "main:app", "--app-dir", "./src"]