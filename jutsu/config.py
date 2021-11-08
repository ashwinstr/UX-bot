__all__ = ['Config']


import os

class Config:
    DB_URI = os.environ.get("DATABASE_URL")
