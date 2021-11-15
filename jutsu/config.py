__all__ = ['Config']


import os
from typing import Set
from jutsu.helpers import int_list


class Config:
    DB_URI = os.environ.get("DATABASE_URL")
    OWNER_ID = os.environ.get("OWNER_ID")
    ADMINS = [] 

class Admins:
    def admins_list_():
        with open("cache/admin_list.txt", "r") as list_:
            adm_lst = list_.read()
        adm_lst = adm_lst.split()
        _list = int_list(adm_lst)
        return _list
