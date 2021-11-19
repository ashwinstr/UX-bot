from jutsu import get_collection


ADMINS = get_collection("ADMINS")


async def Admins(_, __, message) -> bool:
    await message.reply(message.from_user.id)
    async for data in ADMINS.find():
        list_ = data['admin_ids']
        break
    if message.from_user.id in list_:
        print("True")
        return True
    print("False")
    return False
