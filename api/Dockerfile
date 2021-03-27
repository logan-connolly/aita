FROM python:3.8-slim AS builder

ENV PATH="/opt/venv/bin:$PATH" \
    ENV_PIP_NO_CACHE_DIR=1

COPY ./requirements.txt .
RUN set -eux \
    && python -m venv /opt/venv \
    && pip install -U pip setuptools wheel \
    && pip install -r requirements.txt


FROM tiangolo/uvicorn-gunicorn:python3.8-slim AS deploy

WORKDIR /app
ENV PATH="/opt/venv/bin:$PATH" \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONPATH=/app
COPY --from=builder /opt/venv /opt/venv
COPY . .
