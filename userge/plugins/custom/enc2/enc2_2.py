import os
import shutil

from pyrogram import filters

from userge import userge

app = userge

list0 = []
ebot = 2098837300
sudo = [866874030, 885190545]

cmd = "/"
signal = 0
i = 1


def var_reset():
    global signal, i
    signal = 0
    i = 1
    try:
        os.remove("downloads/enc2_2_data.py")
    except BaseException:
        pass
    try:
        shutil.rmtree("downloads/__pycache__")
    except BaseException:
        pass


# Help Cmd


@app.on_message(filters.command("enc2_2_help", cmd))
async def encode_start(app, message):
    sudoD = ""
    for user in sudo:
        u = await app.get_users(user)
        try:
            name = u.first_name + " " + u.last_name
        except Exception:
            name = u.first_name
        sudoD += f"[{name}](tg://user?id={u.id})"
        if user != sudo[len(sudo) - 1]:
            sudoD += ","
    await app.send_message(
        message.chat.id,
        f"**Currently Sudo Can Use**\n{sudoD} are in sudo\n\n{cmd}enc2_2_help - You get this message\n{cmd}enc2_2_input - This will send input_data.py make list of episode by running that file & then /enc2_2 work\n{cmd}enc2_2 [staring ep. no. if you encoded 1 to 10 so enter 11] [reply to data file which you generated by input_data.py]\n{cmd}enc2_2_stop - Stop AI Bot\n{cmd}enc2_2_value - See all variable current value\n\n**",
    )


# Send Input Data file


@app.on_message(filters.command("enc2_2_input", cmd) & filters.user(sudo))
async def encode2_2_input_file(app, message):
    await app.send_document(
        message.chat.id,
        "userge/plugins/custom/enc2_2/input_data.py",
        caption="**Here it is🙂**",
        reply_to_message_id=message.message_id,
    )


# Start AI Bot


@app.on_message(filters.command("enc2_2", cmd) & filters.user(sudo))
async def encode2_2_start(app, message):
    global list0, signal, i
    commands = message.command
    if signal == 1:
        await message.reply_text("```😶Bot already Started🙂```")
        return
    if message.reply_to_message and message.reply_to_message.document:
        await app.send_message(message.chat.id, "🤖Auto Encoding AI **Started**")
    else:
        await app.send_message(
            message.chat.id,
            "```You didn't reply to message\nOR\nReplied message is not document(enc2_2_data.py)```",
        )
        return
    try:
        os.remove("downloads/enc2_2_data.py")
        shutil.rmtree("downloads/__pycache__")
    except BaseException:
        pass
    if len(commands) > 1:
        i = int(commands[1])
    await app.download_media(
        message.reply_to_message.document.file_id, file_name="enc2_2_data.py"
    )
    from downloads.enc2_2_data import list as l

    list0 = l
    signal = 1


# Send Same File again If error Occur


@app.on_message(
    filters.user(ebot) & (filters.regex("(Error)") | filters.regex("^.Errno 2."))
)
async def fix_error(app, message):
    await app.send_message(message.chat.id, list0[i - 1], disable_web_page_preview=True)


# Respond when bot send "Uploaded! ..."


@app.on_message(filters.user(ebot) & filters.regex("^Uploaded!"))
async def encode2_2_worker(app, message):
    global i, signal
    if signal == 0:
        return
    await app.send_message(message.chat.id, list0[i], disable_web_page_preview=True)
    if i == len(list0) - 1:
        await app.send_message(
            message.chat.id,
            "**😃😁Finally My Work Finished.\nNow no more encoding left**",
        )
        var_reset()
        return
    i += 1


# Disable/Stop AI Bot
@app.on_message(filters.user(sudo) & filters.command("enc2_2_stop", cmd))
async def encode_stop(app, message):
    if signal != 0:
        var_reset()
        await app.send_message(
            message.chat.id,
            "🔴Auto Encoding AI ****Stopped****",
            reply_to_message_id=message.message_id,
        )
    else:
        await app.send_message(
            message.chat.id,
            "😑AI Bot is not started yet😕",
            reply_to_message_id=message.message_id,
        )


# Send Values


@app.on_message(filters.user(sudo) & filters.command("enc2_2_value", cmd))
async def encode_values(app, message):
    await message.reply_text(
        f"i -> {i} (next execute ep no.)\nsignal -> {signal} (1 if AI bot is On else Off)"
    )