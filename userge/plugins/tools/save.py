# New Update Soon😅
from userge import Message, userge


@userge.on_cmd("save", about={"header": "Save message"}, allow_channels=True)
async def savemsg(message: Message):
    if isinstance(message.reply_to_message, type(None)):
        await userge.send_message(
            message.chat.id,
            "**Master** `Please reply to someone message🥺`",
            reply_to_message_id=message.message_id,
        )
    else:
        await userge.forward_messages(
            "me", message.chat.id, message.reply_to_message.message_id
        )
