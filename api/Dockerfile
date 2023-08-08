FROM python:3.11-slim-buster as production

COPY requirements/requirements.txt /tmp/requirements.txt

RUN apt-get update && apt-get install -y gcc \
  && python -m venv /opt/venv \
  && /opt/venv/bin/pip install --no-cache -U pip setuptools wheel \
  && /opt/venv/bin/pip install --no-cache -r /tmp/requirements.txt \
  && /opt/venv/bin/python -m spacy download en_core_web_sm \
  && apt-get purge -y gcc \
  && apt-get autoremove -y \
  && rm -rf /var/lib/apt/list/*

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONPATH=/usr/src/app \
    PATH="/opt/venv/bin:$PATH"

WORKDIR /usr/src/app
COPY . .
EXPOSE 8000
CMD ["./start.sh"]

FROM production as development
COPY ./requirements/dev-requirements.txt /tmp/requirements.txt
RUN /opt/venv/bin/pip install -r /tmp/requirements.txt
