

__all__ = ['get_collection']

import asyncio
from typing import List

from motor.motor_asyncio import AsyncIOMotorClient
from motor.core import AgnosticClient, AgnosticDatabase, AgnosticCollection

from jutsu.config import Config


_MGCLIENT: AgnosticClient = AsyncIOMotorClient(Config.DB_URI)
try:
    _RUN = asyncio.get_event_loop().run_until_complete
except:
    _RUN = asyncio.get_event()

_DATABASE: AgnosticDatabase = _MGCLIENT["jutsu"]
_COL_LIST: List[str] = _RUN(_DATABASE.list_collection_names())


def get_collection(name: str) -> AgnosticCollection:
    """ Create or Get Collection from your database """
    return _DATABASE[name]


def _close_db() -> None:
    _MGCLIENT.close()
