import heroku3
import os
from os import system
import asyncio
import time

from pyrogram import Client, filters
from git import Repo
from git.exc import GitCommandError

from jutsu import Config
from jutsu.helpers import telegrapher


HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", None)
HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME", None)
HEROKU_ENV = True
HEROKU_APP = (
        heroku3.from_key(HEROKU_API_KEY).apps()[HEROKU_APP_NAME]
        if HEROKU_ENV and HEROKU_API_KEY and HEROKU_APP_NAME
        else None
    )


@Client.on_message(
    filters.command(["restart"], prefixes="?")
    & filters.user([1013414037])
    & filters.group,
    group=0
)
async def updater_(bot, message):
    if HEROKU_APP:
        await bot.send_message(
            message.chat.id,
            "`Restarting the bot...\nIt will take upto 10 sec to update.`",
        )
        HEROKU_APP.restart()
        time.sleep(10)
    else:
        await bot.send_message(message.chat.id, "`Restarting [HARD] ...`")
        asyncio.get_event_loop().create_task(bot.restart(hard=True))


@Client.on_message(
    filters.command("update", prefixes="?")
    & filters.user([1013414037])
    & filters.group,
    group=1
)
async def updater_two(bot, message):
    msg_ = await message.reply("`Checking for updates, please wait....`")
    text_ = message.text
    if " " in text_:
        flag = text_.split(" ", 1)[1]
    else:
        flag = None
    branch = "main"
    repo = Repo()
    try:
        os.system(f"git remote add upstream {Config.UPSTREAM_REPO}.git")
    except Exception as e:
        await bot.send_message(Config.LOG_CHANNEL, str(e))
    try:
        out = _get_updates(repo, branch)
    except GitCommandError as g_e:
        if "128" in str(g_e):
            system(
                f"git fetch {Config.UPSTREAM_REPO} {branch} && git checkout -f {branch}"
            )
            out = _get_updates(repo, branch)
        else:
            await msg_.edit(g_e)
            return
    if flag != "-pull":
        if out:
            change_log = (
                f"**New UPDATE available for [{branch}]:\n\n📄 CHANGELOG 📄**\n\n"
            )
            if len(change_log) <= 4096:
                await msg_.edit(
                    change_log + out, disable_web_page_preview=True
                )
            else:
                link_ = telegrapher("UX-jutsu changelog.", change_log)
                await msg_.edit(f"**UX-jutsu** changelog is [**HERE**]({link_}).")
        else:
            await msg_.edit(f"**UX-bot is up-to-date with [{branch}]**")
    else:
        if out:
            await msg_.edit(f"`New update found for [{branch}], Now pulling...`")
            await _pull_from_repo(repo, branch)
            await msg_.edit("**UX-jutsu updated successfully.**")


def _get_updates(repo: Repo, branch: str) -> str:
    repo.remote(Config.UPSTREAM_REMOTE).fetch(branch)
    upst = Config.UPSTREAM_REPO.rstrip("/")
    out = ""
    for i in repo.iter_commits(f"HEAD..{Config.UPSTREAM_REMOTE}/{branch}"):
        out += f"🔨 **#{i.count()}** : [{i.summary}]({upst}/commit/{i}) 👷 __{i.author}__\n\n"
    return out


async def _pull_from_repo(repo: Repo, branch: str) -> None:
    repo.git.checkout(branch, force=True)
    repo.git.reset("--hard", branch)
    repo.remote(Config.UPSTREAM_REMOTE).pull(branch, force=True)
    await asyncio.sleep(1)