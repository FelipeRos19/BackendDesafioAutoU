FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

RUN python -m nltk.downloader stopwords

COPY . .

EXPOSE 8000

CMD ["sh", "-c", "uvicorn main:app --host :: --port ${PORT:-8000} --workers ${WORKERS:-3} --log-level info --proxy-headers"]

