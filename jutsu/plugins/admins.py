from jutsu import get_collection


ADMINS = get_collection("ADMINS")


async def admins(_, __, message) -> bool:
    async for data in ADMINS.find():
        list_ = data['admin_ids']
        break
    if message.from_user.id in list_:
        return True
    return False
