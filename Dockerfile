FROM python:3.12-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["sh", "-c", "gunicorn -w 2 -b 0.0.0.0:${PORT:-7860} app:learn_api"]