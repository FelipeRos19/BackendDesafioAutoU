FROM python:3.12

WORKDIR /app
COPY . .
RUN pip install -r requirements.txt

CMD uvicorn main:app --host 0.0.0.0 --port ${PORT:-8000} --log-level info --proxy-headers