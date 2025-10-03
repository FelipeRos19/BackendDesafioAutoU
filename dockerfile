# Dockerfile
FROM python:3.12-slim

WORKDIR /app

# Copia e instala dependências
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante do código
COPY . .

# Expõe a porta que o Railway vai usar
EXPOSE 8000

# Comando para rodar o app
# Usa Gunicorn com UvicornWorker, 1 worker, porta dinâmica
CMD ["sh", "-c", "gunicorn -k uvicorn.workers.UvicornWorker main:app --bind 0.0.0.0:${PORT:-8000} --workers 1"]
