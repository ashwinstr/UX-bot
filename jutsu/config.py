__all__ = ['Config']


import os


class Config:
    DB_URI = os.environ.get("DATABASE_URL")
    OWNER_ID = int(os.environ.get("OWNER_ID"))
    LOG_CHANNEL = -1001661347032