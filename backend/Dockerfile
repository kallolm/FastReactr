FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

COPY . /app

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

ENV PORT=8000
