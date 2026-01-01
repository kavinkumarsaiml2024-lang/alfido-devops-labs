# Task 1 – Dockerize a Simple Flask App

For this task, I created a simple Flask application and containerized it using Docker and docker-compose.  
The app exposes a single `/` endpoint that returns a JSON message.

## Files
- app.py – flask application
- requirements.txt – dependencies
- Dockerfile – container instructions
- docker-compose.yml – run configuration

## Commands I used
### Build the image
docker-compose build

### Start the container
docker-compose up -d

### Check running containers
docker ps

### Test the endpoint
curl http://localhost:5000/

Expected output:
{ "message": "Hello from Dockerized Flask App!" }

## What I learned
- How Docker builds images using a Dockerfile
- How docker-compose simplifies running containers
- How to expose ports and test endpoints

## Development (live reload / file-watch) ✅
You can run the project in development mode with live reload for both Flask (port 5000) and Streamlit (port 8501).

1. Start dev services (the `docker-compose.override.yml` mounts your files and runs dev servers):

   ```bash
   docker compose up --build
   ```

2. Test endpoints / UI:
   - Flask: http://localhost:5000/
   - Streamlit: http://localhost:8501/

3. Edit files locally (for example `app.py` or files under `ui/`) — changes should be picked up automatically.

4. If your host filesystem doesn't support inotify (e.g., certain VM/shared folders), enable polling:
   - Set `WATCHDOG_USE_POLLING=1` in `.env` and restart the services. The dev image includes `watchdog` and the dev entrypoint will use `watchmedo auto-restart` to restart Flask/Streamlit processes when files change.

Notes:
- Compose reads `docker-compose.override.yml` automatically for local development and now uses the `dev` image target which includes dev dependencies.
- If you'd like, I can add a convenience `Makefile` to start the dev environment or make the dev image a separate Dockerfile named `Dockerfile.dev` — tell me which you prefer.

