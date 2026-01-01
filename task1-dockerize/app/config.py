import os

class Config:
    APP_ENV = os.getenv("APP_ENV", "production")
    ALLOWED_COMMANDS = os.getenv(
        "ALLOWED_COMMANDS",
        "ls,uptime,df -h,free -m"
    ).split(",")

    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
