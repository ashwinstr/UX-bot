
import sys
import io
import keyword
import traceback

from pyrogram import Client, filters


@Client.on_message(
    filters.command(["eval"], prefixes="?")
    & filters.user([1013414037])
    & filters.group
)
async def eval_(bot, message):
    try:
        cmd = ((message.text).strip).split(" ", 1)[1]
    except:
        return await bot.send_message(message.chat.id, "`Command not found.`", reply_to_message_id=message.message_id)
    msg = await bot.send_message(message.chat.id, "`Executing eval...`", reply_to_message_id=message.message_id)
    old_stderr = sys.stderr
    old_stdout = sys.stdout
    redirected_output = sys.stdout = io.StringIO()
    redirected_error = sys.stderr = io.StringIO()
    ret_val, stdout, stderr, exc = None, None, None, None
    async def aexec(code):
        head = "async def __aexec(userge, message):\n "
        if "\n" in code:
            rest_code = "\n ".join(iter(code.split("\n")))
        elif (
            any(
                True
                for k_ in keyword.kwlist
                if k_ not in ("True", "False", "None") and code.startswith(f"{k_} ")
            )
            or "=" in code
        ):
            rest_code = f"\n {code}"
        else:
            rest_code = f"\n return {code}"
        exec(head + rest_code)  # nosec pylint: disable=W0122
        return await locals()["__aexec"](Client, message)

    try:
        ret_val = await aexec(cmd)
    except Exception:  # pylint: disable=broad-except
        exc = traceback.format_exc().strip()
    stdout = redirected_output.getvalue().strip()
    stderr = redirected_error.getvalue().strip()
    sys.stdout = old_stdout
    sys.stderr = old_stderr
    evaluation = exc or stderr or stdout or ret_val
    output = ""
    if evaluation is not None:
        output += f"**>>** ```{evaluation}```"
    if (exc or stderr) and message.chat.type in ("group", "supergroup", "channel"):
        await msg.edit(output)
    elif output:
        await msg.edit_or_send_as_file(
            text=output, parse_mode="md", filename="eval.txt", caption=cmd
        )
    else:
        await message.delete()
