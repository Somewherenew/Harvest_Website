import os


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "change-me-before-deploying")
    # Cache static files for a week in production
    SEND_FILE_MAX_AGE_DEFAULT = 0 if os.environ.get("FLASK_DEBUG") == "1" else 604800
