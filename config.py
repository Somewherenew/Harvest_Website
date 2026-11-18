import os

from dotenv import load_dotenv


load_dotenv()


def _database_url():
    url = os.environ.get("DATABASE_URL", "").strip()
    for prefix in ("postgres://", "postgresql://"):
        if url.startswith(prefix):
            return "postgresql+psycopg://" + url[len(prefix):]
    return url


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "change-me-before-deploying")

    SEND_FILE_MAX_AGE_DEFAULT = 0 if os.environ.get("FLASK_DEBUG") == "1" else 604800

    SQLALCHEMY_DATABASE_URI = _database_url()
    SQLALCHEMY_ENGINE_OPTIONS = {"pool_pre_ping": True, "pool_recycle": 300}

    VISITOR_COOKIE = "hg_visitor"
    VISITOR_COOKIE_DAYS = 90