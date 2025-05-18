FROM python:3.11-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir fastapi uvicorn pycryptodome requests

EXPOSE 8000

CMD ["uvicorn", "user_api:app", "--host", "0.0.0.0", "--port", "8000"]