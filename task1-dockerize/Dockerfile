# -------- Stage 1: Builder --------
FROM python:3.10 AS builder
WORKDIR /build
COPY requirements.txt .
RUN pip install --user -r requirements.txt

# -------- Stage 2: Runtime --------
FROM python:3.10-slim
WORKDIR /app

COPY --from=builder /root/.local /root/.local
ENV PATH=/root/.local/bin:$PATH

COPY core ./core
COPY infra ./infra
COPY ui ./ui
RUN mkdir -p logscd

EXPOSE 8501

HEALTHCHECK CMD python -c "import psutil; exit(0)"

CMD ["streamlit", "run", "ui/dashboard.py", "--server.address=0.0.0.0"]

FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

EXPOSE 8501

CMD ["streamlit", "run", "app.py", "--server.address=0.0.0.0"]
FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app /app/app

ENV APP_NAME="DevOps Intern Service"
ENV APP_ENV="production"
ENV APP_PORT=5000

EXPOSE 5000


FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

EXPOSE 8501

CMD ["streamlit", "run", "app.py", "--server.address=0.0.0.0"]
CMD ["python", "app/main.py"]

FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["python", "app.py"]

# -------- Stage: Dev (includes polling watcher for local development) --------
FROM python:3.11-slim AS dev
WORKDIR /app
# copy regular + dev requirements and install both
COPY requirements.txt requirements-dev.txt ./
RUN pip install --no-cache-dir -r requirements.txt -r requirements-dev.txt
# copy source
COPY . .
# make the dev entrypoint executable
RUN chmod +x /app/dev-entrypoint.sh
EXPOSE 5000 8501
# The dev entrypoint decides how to run based on $SERVICE and $WATCHDOG_USE_POLLING
# Use `sh` to invoke the script so it works even if the bind-mounted file on the host
# doesn't have the executable bit set.
ENTRYPOINT ["sh", "/app/dev-entrypoint.sh"]

