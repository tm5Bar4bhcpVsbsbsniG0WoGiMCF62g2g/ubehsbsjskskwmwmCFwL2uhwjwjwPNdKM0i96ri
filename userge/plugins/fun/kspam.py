import asyncio
import os

from userge import Config, Message, userge

S_LOG = userge.getCLogger(__name__)


@userge.on_cmd(
    "kspam",
    about={
        "header": "Spam some Messages & delete before sending next message",
        "description": "Message Spam module just for fun."
        "Btw Don't over use this plugin or get"
        "ready for account ban or flood waits. "
        "For spamming text use '|' to separate count and text.",
        "usage": "{tr}kspam [spam count] | [delay] | [spam message]",
        "examples": "**For Text:** `{tr}kspam 2 | Admin will ban me for using this plugin`",
    },
)
async def kspam(message: Message):
    if len(message.text.split())!=6:
    	await message.reply("**Read help of kspam.**")
    txt=message.text.split(" ",maxsplit=1)[1]
    count,delay,msg=txt.split(" | ")
    await message.delete()
    for i in range(int(count)):
    	m=await message.reply(msg)
    	await asyncio.sleep(int(delay))
    	await m.delete()
