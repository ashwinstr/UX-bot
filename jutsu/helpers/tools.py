from telegraph import Telegraph
from jutsu import get_collection


ADMINS = get_collection("ADMINS")
tele_ = Telegraph()

def telegrapher(a_title: str, content: str) -> str:
    auth_name = tele_.create_account(short_name="Kakashi")
    resp = tele_.create_page(
        title=a_title,
        author_name=auth_name,
        author_url="https://t.me/xplugin",
        html_content=content,
    )
    link_ = resp["url"]
    return link_


def int_list(list_):
    intlist = []
    for one in list_:
        if one.isdigit():
            one = int(one)
        intlist.append(one)
    return intlist

async def username_list(list_):
    u_list = []
    for one in list_:
        u_list.append((await bot.get_users(one)).username)
    return u_list


def _admins_list_(_, __, message) -> bool:
    with open("jutsu/cache/admin_list.txt", "r") as list_:
        adm_lst = list_.read()
    adm_lst = adm_lst.split()
    _list = int_list(adm_lst)
    if message.from_user.id in _list:
        return True
    return False



async def admins(_, __, message) -> bool:
    async for data in ADMINS.find():
        list_ = data['admin_ids']
        break
    if message.from_user.id in list_:
        return True
    return False 
