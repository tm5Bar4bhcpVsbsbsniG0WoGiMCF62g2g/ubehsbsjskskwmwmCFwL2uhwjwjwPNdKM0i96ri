from pyrogram import filters

from userge import userge

app = userge
cmd = "/"


@app.on_message(filters.command("enc2_list", cmd))
async def encode_start(app, message):
    await message.reply_text(
        f"**List of cmd for diff bot:-**\n\n/enc2 - @Encoding_Stuffs_Bot\n/enc2_1 - @WZI_Encoder_Bot"
    )
