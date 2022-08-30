FROM openstax/python3-poetry

RUN mkdir -p /opt

WORKDIR /opt

COPY pyproject.toml ./pyproject.toml
# COPY poetry.lock ./poetry.lock

RUN poetry install

COPY ./app ./app

EXPOSE 8000

CMD ["poetry", "run", "uvicorn", "app.api.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]