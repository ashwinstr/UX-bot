__all__ = ['Config']


import os
from typing import Set
from jutsu import get_collection
from jutsu.helpers import int_list 

ADMINS = get_collection("ADMINS")

class Config:
    DB_URI = os.environ.get("DATABASE_URL")
    OWNER_ID = os.environ.get("OWNER_ID")
    ADMINS = [] 

class Admins:
    async def list_admin():
        async for data in ADMINS.find():
            one = data['admin_ids']
            break
        admins = one
    with open("cache/admin_list.txt", "r") as list_:
        adm_lst = list_.read()
    _list = adm_lst.split()
    adm_list = int_list(_list)
