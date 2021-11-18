
import aiofiles
import os
from jutsu import get_collection
import _init

ADMINS = get_collection("ADMINS")


async def _init():
    if not os.path.isdir("cache/"):
        os.mkdir("cache/")
    found = await ADMINS.find_one({'chat_id': -1001331162912})
    if not found:
        return
    list_ = found['admin_ids']
    async with aiofiles.open("cache/admin_list.txt", "w+") as fn:
        for one in list_:
            await fn.writelines(f"{one} ")
