#! /usr/bin/env sh
set -e

# Export variables
export APP_MODULE=${MODULE_NAME:-app.main:app}
export GUNICORN_CONF=${GUNICORN_CONF:-gunicorn_conf.py}
export WORKER_CLASS=${WORKER_CLASS:-"uvicorn.workers.UvicornWorker"}

# Prestart script
sleep 5
echo "Running alembic migrations ..."
alembic upgrade head

# Start app server
if [ "${DEBUG}" = "True" ]; then
  exec uvicorn "$APP_MODULE" --host 0.0.0.0 --port 8000 --reload
else
  exec gunicorn -k "$WORKER_CLASS" -c "$GUNICORN_CONF" "$APP_MODULE"
fi
