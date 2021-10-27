# This File is for custom use
from pyrogram import filters

from userge import userge

app = userge

ebot = 1887520139
sudo = [866874030, 885190545]
cmd = "/"

i0 = "{i}"  # for skiping f-string 🥲
start = 1  # if ep.no. is 101 so if we need to start from 1 so this.Many show/anime not divude into season so for dividing
startSignal = 0  # Signal for Start Variable
i = 1
l = 0
signal = 0
q = ""


# Var Reset Function
def var_reset():
    global signal, l, i, q, start
    signal = 0
    l = 0
    i = 1
    start = 1
    q = ""


# Help


@app.on_message(filters.command("enc_help", cmd))
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
        f'**Currently Sudo Can Use**\n{sudoD} are in sudo\n\n{cmd}enc_help - You get this message\n{cmd}enc [y/n (y means start from1 if ep. no. not start from 1)] [starting ep. no.] [last(ending) ep. no.] [link instead of ep. no. use {i0}] | [ rename file name with {i0}\n{cmd}enc_stop - Currently Not Working\n{cmd}enc_value - See all variable current value\n\n**Explaination**:\nIn {cmd}enc \nstarting ep. no. for if some ep. encoded already\n{i0} use because episode link is animeS1E1...En& rename will be animeS1E1...En\n\n"n" is last episode\nHere {i0} will replace with i & i increment until i is greater then l.\n\ne.g. i=21 & l=26 so this will enocode episode 21 to 26',
    )


# Enable/Start Auto Encoding Ai


@app.on_message(filters.command("enc", cmd) & filters.user(sudo))
async def encode_start(app, message):
    q0 = ""
    global q, l, signal, i, startSignal
    code = message.text
    code = str(code[5:])
    code = code.split(" ")
    print(code)
    if code[0] == "y":
        startSignal = 1
    else:
        startSignal = 0
    i = int(code[1])
    l = int(code[2])
    a = 3
    while a < len(code):
        q0 += code[a]
        if a < len(code) - 1:
            q0 += " "
        a += 1
    q = "/ddl " + q0
    signal = 1
    await app.send_message(message.chat.id, "🤖Auto Encoding AI **Started**")


# After Start this will work


@app.on_message(filters.user(ebot) & filters.regex("^Uploaded!"))
async def encode_worker(app, message):
    global i, signal, l, q, start
    if signal == 1:
        if i <= l:
            if startSignal == 0:
                s = q.replace("{start}", "{i}")
            else:
                s = q.replace("{start}", str(start))
            s = s.replace("{i}", str(i))
            await app.send_message(message.chat.id, s, disable_web_page_preview=True)
            if i == l:
                await app.send_message(
                    message.chat.id,
                    "**😃😁Finally My Work Finished.\nNow no more encoding left**",
                )
            int(i)
            i += 1
            start += 1
        else:
            var_reset()
    else:
        return


# Disable/Stop AI Bot


@app.on_message(filters.user(sudo) & filters.command("enc_stop", cmd))
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


#########


@app.on_message(filters.user(sudo) & filters.command("enc_value", cmd))
async def encode_values(app, message):
    await message.reply_text(
        f"i -> {i} (next execute ep no.)\nstart -> {start}\nl -> {l} (last execute ep no.)\nq (query) -> {q}\nsignal -> {signal} (1 if AI bot is On else 0"
    )
