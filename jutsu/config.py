__all__ = ['Config']


import os
from typing import Set

class Config:
    DB_URI = os.environ.get("DATABASE_URL")
    OWNER_ID = os.environ.get("OWNER_ID")
    ADMINS = [] 
