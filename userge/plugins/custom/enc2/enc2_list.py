from pyrogram import filters

from userge import userge

app = userge
cmd = "/"


@app.on_message(filters.command("enc2_list", cmd))
async def encode_start(app, message):
    await message.reply_text(
        f"""**List of cmd for diff bot:-**

/enc2 - @Encoding_Stuffs_Bot
/enc2_1 - @WZI_Encoder_Bot
/enc2_2 - @bACkUpbObot
/enc2_3 - @bACKUPWZIBOT"""
    )
