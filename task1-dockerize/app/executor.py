import subprocess
from core.config import Config
from infra.logger import logger

def execute_command(command):
    if command not in Config.ALLOWED_COMMANDS:
        logger.warning(f"Blocked command attempt: {command}")
        return "Command not permitted"

    try:
        result = subprocess.check_output(
            command, shell=True, stderr=subprocess.STDOUT, text=True
        )
        logger.info(f"Executed command: {command}")
        return result
    except subprocess.CalledProcessError as e:
        logger.error(e.output)
        return e.output
