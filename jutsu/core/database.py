

__all__ = ['get_collection']

import asyncio
from typing import List

from motor.motor_asyncio import AsyncIOMotorClient
from motor.core import AgnosticClient, AgnosticDatabase, AgnosticCollection

from jutsu import Config


_MGCLIENT: AgnosticClient = AsyncIOMotorClient(Config.DB_URI)
_RUN = asyncio.get_event_loop().run_until_complete

_DATABASE: AgnosticDatabase = _MGCLIENT["Userge"]
_COL_LIST: List[str] = _RUN(_DATABASE.list_collection_names())


def get_collection(name: str) -> AgnosticCollection:
    """ Create or Get Collection from your database """
    if name in _COL_LIST:
        _LOG.debug(_LOG_STR, f"{name} Collection Found :) => Now Logging to it...")
    else:
        _LOG.debug(_LOG_STR, f"{name} Collection Not Found :( => Creating New Collection...")
    return _DATABASE[name]


def _close_db() -> None:
    _MGCLIENT.close()
