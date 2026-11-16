FROM python:3.12-slim

WORKDIR /app

RUN apt-get update \
    && apt-get install --no-install-recommends --yes socat \
    && rm -rf /var/lib/apt/lists/*

COPY main.py .
COPY logs .

CMD ["socat", "TCP-LISTEN:31337,reuseaddr,fork", "EXEC:python -u /app/main.py"]
