

from jutsu.core.database import get_collection
from jutsu.config import Config
from jutsu.helpers.tools import telegrapher

ADMINS = get_collection("ADMINS") 


async def admin_list():
    if not os.path.exists("cache/"):
        os.mkdir("cache/")
    list_ = []
    found = await ADMINS.find_one({'chat_id': -1001331162912})
    if found:
        list_ = found['admin_ids']
    owner = int(str(Config.OWNER_ID).split()[0])
    list_.append(owner)
    with open("cache/admin_list.txt", "w+") as adm_lst:
        for one in list_:
            adm_lst.write(f"{one} ")
