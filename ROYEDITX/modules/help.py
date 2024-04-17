from telethon import events, Button
from config import X1, SUDO_USERS, CMD_HNDLR as hl

HELP_STRING = f"**✦ ᴄʟɪᴄᴋ ᴏɴ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴꜱ ꜰᴏʀ xsᴘᴀᴍ ʜᴇʟᴘ ⏤͟͟͞͞★**"

HELP_BUTTON = [
    [
        Button.inline("ꜱᴘᴀᴍ", data="spam"),
        Button.inline("ʀᴀɪᴅ", data="raid")
    ],
    [
        Button.inline("ᴇxᴛʀᴀ", data="extra")
    ],
    [
        Button.url("ᴜᴘᴅᴀᴛᴇ", "https://t.me/roy_editx"),
        Button.url("sᴜᴘᴘᴏʀᴛ", "https://t.me/the_friendz")
    ]
]


@X1.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
async def help(event):
    try:
        await event.client.send_file(
            event.chat_id,
            "https://graph.org/file/cacbdddee77784d9ed2b7.jpg",
            caption=HELP_STRING,
            buttons=HELP_BUTTON
        )
    except Exception as e:
        await event.client.send_message(event.chat_id, f"✦ ᴀɴ ᴇxᴄᴇᴘᴛɪᴏɴ ᴏᴄᴄᴜʀᴇᴅ, ᴇʀʀᴏʀ ➥ {str(e)}")


extra_msg = """
**✦  ᴇxᴛʀᴀ ᴄᴏᴍᴍᴀɴᴅꜱ ♥︎**

❖ 𝗨𝘀𝗲𝗿𝗕𝗼𝘁 ➥ **ᴜꜱᴇʀʙᴏᴛ ᴄᴍᴅꜱ ⏤͟͟͞͞★**
  ● /ping 
  ● /reboot
  ● /sudo <reply to user> ➠ Owner Cmd
  ● /logs ➠ Owner Cmd

❖ 𝗘𝗰𝗵𝗼 ➥ **ᴛᴏ ᴀᴄᴛɪᴠᴇ ᴇᴄʜᴏ ᴏɴ ᴀɴʏ ᴜꜱᴇʀ ⏤͟͟͞͞★**
  ● /echo <reply to user>
  ● /rmecho <reply to user>

❖ 𝗟𝗲𝗮𝘃𝗲 ➥ **ᴛᴏ ʟᴇᴀᴠᴇ ɢʀᴏᴜᴘ/ᴄʜᴀɴɴᴇʟ ⏤͟͟͞͞★**
  ● /leave <group/chat id>
  ● /leave ➠ Type in the Group bot will auto leave that group
"""

raid_msg = """
**✦ ʀᴀɪᴅ ᴄᴏᴍᴍᴀɴᴅꜱ ♥︎**

❖ 𝗥𝗮𝗶𝗱 ➥ **ᴀᴄᴛɪᴠᴀᴛᴇꜱ ʀᴀɪᴅ ᴏɴ ᴀɴʏ ɪɴᴅɪᴠɪᴅᴜᴀʟ ᴜꜱᴇʀ ꜰᴏʀ ɢɪᴠᴇɴ ʀᴀɴɢᴇ ⏤͟͟͞͞★**
  ● /raid <count> <username>
  ● /raid <count> <reply to user>

❖ 𝗥𝗲𝗽𝗹𝘆𝗥𝗮𝗶𝗱 ➥ **ᴀᴄᴛɪᴠᴀᴛᴇꜱ ʀᴇᴘʟʏ ʀᴀɪᴅ ᴏɴ ᴛʜᴇ ᴜꜱᴇʀ ⏤͟͟͞͞★**
  ● /rraid <replying to user>
  ● /rraid <username>

❖ 𝗗𝗥𝗲𝗽𝗹𝘆𝗥𝗮𝗶𝗱 ➥ **ᴅᴇᴀᴄᴛɪᴠᴀᴛᴇꜱ ʀᴇᴘʟʏ ʀᴀɪᴅ ᴏɴ ᴛʜᴇ ᴜꜱᴇʀ ⏤͟͟͞͞★**
  ● /drraid <replying to user>
  ● /drraid <username>

❖ 𝐌𝐑𝐚𝐢𝐝 ➥ **ʟᴏᴠᴇ ʀᴀɪᴅ ᴏɴ ᴛʜᴇ ᴜꜱᴇʀ⏤͟͟͞͞★ **
  ● /mraid <count> <username>
  ● /mraid <count> <reply to user>

❖ 𝐒𝐑𝐚𝐢𝐝 ➥ **ꜱʜᴀʏᴀʀɪ ʀᴀɪᴅ ᴏɴ ᴛʜᴇ ᴜꜱᴇʀ ⏤͟͟͞͞★**
  ● /sraid <count> <username>
  ● /sraid <count> <reply to user>

❖ 𝐂𝐑𝐚𝐢𝐝 ➥ **ᴀʙᴄᴅ ʀᴀɪᴅ ᴏɴ ᴛʜᴇ ᴜꜱᴇʀ ⏤͟͟͞͞★**
  ● /craid <count> <username>
  ● /craid <count> <reply to user>
"""

spam_msg = """
**✦ ꜱᴘᴀᴍ ᴄᴏᴍᴍᴀɴᴅꜱ ♥︎**

❖ 𝗦𝗽𝗮𝗺 ➥ **ꜱᴘᴀᴍꜱ ᴀ ᴍᴇꜱꜱᴀɢᴇ ⏤͟͟͞͞★**
  ● /spam <count> <message to spam> 
  ● /spam <count> <replying any message>

❖ 𝗣𝗼𝗿𝗻𝗦𝗽𝗮𝗺 ➥ **ᴘᴏʀᴍᴏɢʀᴀᴘʜʏ ꜱᴘᴀᴍ ⏤͟͟͞͞★**
  ● /pspam <count>

❖ 𝗛𝗮𝗻𝗴 ➥ **ꜱᴘᴀᴍꜱ ʜᴀɴɢɪɴɢ ᴍᴇꜱꜱᴀɢᴇ ꜰᴏʀ ɢɪᴠᴇɴ ᴄᴏᴜɴᴛᴇʀ ⏤͟͟͞͞★**
  ● /hang <counter>
"""

@X1.on(events.CallbackQuery(pattern=r"help_back"))
async def helpback(event):
    await event.edit(
        HELP_STRING,
        buttons=[
            [
                Button.inline("ꜱᴘᴀᴍ", data="spam"),
                Button.inline("ʀᴀɪᴅ", data="raid")
            ],
            [
                Button.inline("ᴇxᴛʀᴀ", data="extra")
            ]
        ]
    )
    
@X1.on(events.CallbackQuery(pattern=r"spam"))
async def help_spam(event):
    await event.edit(
        spam_msg,
        buttons=[[Button.inline("ʙᴀᴄᴋ", data="help_back"),],],
    )

@X1.on(events.CallbackQuery(pattern=r"raid"))
async def help_raid(event):
    await event.edit(
        raid_msg,
        buttons=[[Button.inline("ʙᴀᴄᴋ", data="help_back"),],],
    )

@X1.on(events.CallbackQuery(pattern=r"extra"))
async def help_extra(event):
    await event.edit(
        extra_msg,
        buttons=[[Button.inline("ʙᴀᴄᴋ", data="help_back"),],],
    )

