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
        _list = adm_lst.split()
        adm_list = int_list(_list)
        return adm_list
