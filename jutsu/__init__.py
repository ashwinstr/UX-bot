
from jutsu.core.database import get_collection
from jutsu.config import Config
from jutsu.helpers import int_list


def load_adm():
    with open("cache/admin_list.txt", "r") as list_:
        adm_lst = list_.read()
    _list = adm_lst.split()
    _list = int_list(_list)
    return _list
    
