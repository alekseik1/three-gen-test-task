FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9
RUN pip install fastapi pydantic
WORKDIR /app
COPY . /app
CMD ["python", "bittensor_test_task/main.py"]
