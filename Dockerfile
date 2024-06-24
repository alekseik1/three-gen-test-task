FROM python:3.12
WORKDIR /app
RUN pip install poetry
COPY poetry.lock pyproject.toml ./
RUN poetry install --no-root --only main
COPY . /app
RUN poetry install --only-root
CMD ["poetry", "run", "python", "bittensor_test_task/main.py"]
