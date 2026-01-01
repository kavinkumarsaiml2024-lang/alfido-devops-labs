#!/bin/sh
set -e

echo "DEV entrypoint: service=$SERVICE, WATCHDOG_USE_POLLING=${WATCHDOG_USE_POLLING:-0}"

if [ "${WATCHDOG_USE_POLLING:-0}" = "1" ]; then
  echo "Polling mode enabled — using watchmedo to restart on changes"
  if [ "$SERVICE" = "streamlit" ]; then
    exec watchmedo auto-restart --directory=/app/ui --pattern="*.py" --recursive -- streamlit run ui/dashboard.py --server.address=0.0.0.0 --server.runOnSave=true
  else
    exec watchmedo auto-restart --directory=/app --pattern="*.py" --recursive -- python -m flask run --host=0.0.0.0 --port=5000
  fi
else
  echo "Inotify mode (default) — running normal servers"
  if [ "$SERVICE" = "streamlit" ]; then
    exec streamlit run ui/dashboard.py --server.address=0.0.0.0 --server.runOnSave=true
  else
    exec python -m flask run --host=0.0.0.0 --port=5000 --reload
  fi
fi
