import logging
import json
from datetime import datetime

class JsonFormatter(logging.Formatter):
    def format(self, record):
        log = {
            "timestamp": datetime.utcnow().isoformat(),
            "level": record.levelname,
            "message": record.getMessage(),
            "module": record.module,
        }
        return json.dumps(log)

logger = logging.getLogger("control-plane")
logger.setLevel(logging.INFO)

handler = logging.FileHandler("logs/app.json.log")
handler.setFormatter(JsonFormatter())
logger.addHandler(handler)
