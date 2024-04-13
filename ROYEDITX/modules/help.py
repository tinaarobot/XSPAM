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
    if event.sender_id in SUDO_USERS:
        try:
          await event.client.send_file(event.chat_id,
              "https://graph.org/file/cacbdddee77784d9ed2b7.jpg",
              caption=HELP_STRING,
              buttons=HELP_BUTTON
              )
        except Exception as e:
            await event.client.send_message(event.chat_id, f"✦ ᴀɴ ᴇxᴄᴇᴘᴛɪᴏɴ ᴏᴄᴄᴜʀᴇᴅ, ᴇʀʀᴏʀ ➥ {str(e)}")


extra_msg = f"""
**✦  ᴇxᴛʀᴀ ᴄᴏᴍᴍᴀɴᴅꜱ ♥︎**

❖ 𝗨𝘀𝗲𝗿𝗕𝗼𝘁 ➥ **ᴜꜱᴇʀʙᴏᴛ ᴄᴍᴅꜱ ⏤͟͟͞͞★**
  ● {hl}ping 
  ● {hl}reboot
  ● {hl}sudo <reply to user> ➠ Owner Cmd
  ● {hl}logs ➠ Owner Cmd

❖ 𝗘𝗰𝗵𝗼 ➥ **ᴛᴏ ᴀᴄᴛɪᴠᴇ ᴇᴄʜᴏ ᴏɴ ᴀɴʏ ᴜꜱᴇʀ ⏤͟͟͞͞★**
  ● {hl}echo <reply to user>
  ● {hl}rmecho <reply to user>

❖ 𝗟𝗲𝗮𝘃𝗲 ➥ **ᴛᴏ ʟᴇᴀᴠᴇ ɢʀᴏᴜᴘ/ᴄʜᴀɴɴᴇʟ ⏤͟͟͞͞★**
  ● {hl}leave <group/chat id>
  ● {hl}leave ➠ Type in the Group bot will auto leave that group
"""

                 
raid_msg = f"""
**✦ ʀᴀɪᴅ ᴄᴏᴍᴍᴀɴᴅꜱ ♥︎**

❖ 𝗥𝗮𝗶𝗱 ➥ **ᴀᴄᴛɪᴠᴀᴛᴇꜱ ʀᴀɪᴅ ᴏɴ ᴀɴʏ ɪɴᴅɪᴠɪᴅᴜᴀʟ ᴜꜱᴇʀ ꜰᴏʀ ɢɪᴠᴇɴ ʀᴀɴɢᴇ ⏤͟͟͞͞★**
  ● {hl}raid <count> <username>
  ● {hl}raid <count> <reply to user>

❖ 𝗥𝗲𝗽𝗹𝘆𝗥𝗮𝗶𝗱 ➥ **ᴀᴄᴛɪᴠᴀᴛᴇꜱ ʀᴇᴘʟʏ ʀᴀɪᴅ ᴏɴ ᴛʜᴇ ᴜꜱᴇʀ ⏤͟͟͞͞★**
  ● {hl}rraid <replying to user>
  ● {hl}rraid <username>

❖ 𝗗𝗥𝗲𝗽𝗹𝘆𝗥𝗮𝗶𝗱 ➥ **ᴅᴇᴀᴄᴛɪᴠᴀᴛᴇꜱ ʀᴇᴘʟʏ ʀᴀɪᴅ ᴏɴ ᴛʜᴇ ᴜꜱᴇʀ ⏤͟͟͞͞★**
  ● {hl}drraid <replying to user>
  ● {hl}drraid <username>

❖ 𝐌𝐑𝐚𝐢𝐝 ➥ **ʟᴏᴠᴇ ʀᴀɪᴅ ᴏɴ ᴛʜᴇ ᴜꜱᴇʀ⏤͟͟͞͞★ **
  ● {hl}mraid <count> <username>
  ● {hl}mraid <count> <reply to user>

❖ 𝐒𝐑𝐚𝐢𝐝 ➥ **ꜱʜᴀʏᴀʀɪ ʀᴀɪᴅ ᴏɴ ᴛʜᴇ ᴜꜱᴇʀ ⏤͟͟͞͞★**
  ● {hl}sraid <count> <username>
  ● {hl}sraid <count> <reply to user>

❖ 𝐂𝐑𝐚𝐢𝐝 ➥ **ᴀʙᴄᴅ ʀᴀɪᴅ ᴏɴ ᴛʜᴇ ᴜꜱᴇʀ ⏤͟͟͞͞★**
  ● {hl}craid <count> <username>
  ● {hl}craid <count> <reply to user>
"""

spam_msg = f"""
**✦ ꜱᴘᴀᴍ ᴄᴏᴍᴍᴀɴᴅꜱ ♥︎**

❖ 𝗦𝗽𝗮𝗺 ➥ **ꜱᴘᴀᴍꜱ ᴀ ᴍᴇꜱꜱᴀɢᴇ ⏤͟͟͞͞★**
  ● {hl}spam <count> <message to spam> 
  ● {hl}spam <count> <replying any message>

❖ 𝗣𝗼𝗿𝗻𝗦𝗽𝗮𝗺 ➥ **ᴘᴏʀᴍᴏɢʀᴀᴘʜʏ ꜱᴘᴀᴍ ⏤͟͟͞͞★**
  ● {hl}pspam <count>

❖ 𝗛𝗮𝗻𝗴 ➥ **ꜱᴘᴀᴍꜱ ʜᴀɴɢɪɴɢ ᴍᴇꜱꜱᴀɢᴇ ꜰᴏʀ ɢɪᴠᴇɴ ᴄᴏᴜɴᴛᴇʀ ⏤͟͟͞͞★**
  ● {hl}hang <counter>
"""                     
           
           
@X1.on(events.CallbackQuery(pattern=r"help_back"))
async def helpback(event):
    if event.query.user_id in SUDO_USERS:    
        await event.edit(
            HELP_STRING,
            buttons=[
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
          )
    else:
        await event.answer("✦ ᴍᴀᴋᴇ ʏᴏᴜʀ ᴏᴡɴ xsᴘᴀᴍ ʙᴏᴛ, ʙʏ ~ @roy_editx", cache_time=0, alert=False)


@X1.on(events.CallbackQuery(pattern=r"spam"))
async def help_spam(event):
    if event.query.user_id in SUDO_USERS:    
        await event.edit(spam_msg,
              buttons=[[Button.inline("< Back", data="help_back"),],],
              ) 
    else:
        await event.answer("✦ ᴍᴀᴋᴇ ʏᴏᴜʀ ᴏᴡɴ xsᴘᴀᴍ ʙᴏᴛ, ʙʏ ~ @roy_editx", cache_time=0, alert=False)


@X1.on(events.CallbackQuery(pattern=r"raid"))
async def help_raid(event):
    if event.query.user_id in SUDO_USERS:
        await event.edit(raid_msg,
            buttons=[[Button.inline("< Back", data="help_back"),],],
          )
    else:
        await event.answer("✦ ᴍᴀᴋᴇ ʏᴏᴜʀ ᴏᴡɴ xsᴘᴀᴍ ʙᴏᴛ, ʙʏ ~ @roy_editx", cache_time=0, alert=False)


@X1.on(events.CallbackQuery(pattern=r"extra"))
async def help_extra(event):
    if event.query.user_id in SUDO_USERS:
        await event.edit(extra_msg,
            buttons=[[Button.inline("< Back", data="help_back"),],],
            )
    else:
        await event.answer("✦ ᴍᴀᴋᴇ ʏᴏᴜʀ ᴏᴡɴ xsᴘᴀᴍ ʙᴏᴛ, ʙʏ ~ @roy_editx", cache_time=0, alert=False)
