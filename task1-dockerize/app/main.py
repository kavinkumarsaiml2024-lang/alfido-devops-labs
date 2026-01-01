from flask import Flask, jsonify, request
from app.config import APP_NAME, APP_ENV, APP_PORT
from app.logger import logger
import time

app = Flask(__name__)

# In-memory data store (enough for intern task)
notes = []

@app.route("/health", methods=["GET"])
def health():
    return jsonify({
        "status": "UP",
        "service": APP_NAME,
        "environment": APP_ENV
    }), 200


@app.route("/notes", methods=["GET"])
def get_notes():
    logger.info("Fetching all notes")
    return jsonify({
        "count": len(notes),
        "data": notes
    })


@app.route("/notes", methods=["POST"])
def create_note():
    payload = request.get_json()

    if not payload or "message" not in payload:
        logger.warning("Invalid request payload")
        return jsonify({"error": "message field is required"}), 400

    note = {
        "id": len(notes) + 1,
        "message": payload["message"],
        "created_at": time.time()
    }

    notes.append(note)
    logger.info(f"Note created: {note['id']}")

    return jsonify(note), 201


if __name__ == "__main__":
    logger.info(f"Starting {APP_NAME} in {APP_ENV} mode")
    app.run(host="0.0.0.0", port=APP_PORT)
