from telethon import __version__, events, Button

from config import X1


START_BUTTON = [
    [
        Button.url("ᴀᴅᴅ ᴍᴇ ʙᴀʙʏ", "https://t.me/avishaxbot?startgroup=true")
    ],
    [
        Button.url("sᴜᴘᴘᴏʀᴛ", "https://t.me/the_friendz"),
        Button.url("ʀᴇᴘᴏ", "https://github.com/LOCO-PILOT/ROYMUSIC")
    ],
    [
        Button.inline("ʜᴇʟᴘ ᴄᴏᴍᴍᴀɴᴅs", data="help_back")
    ]
]


@X1.on(events.NewMessage(pattern="/start"))
async def start(event):              
    if event.is_private:
        Altbot = await event.client.get_me()
        bot_name = Altbot.first_name
        bot_id = Altbot.id
        TEXT = f"**❖ ʜᴇʏ [{event.sender.first_name}](tg://user?id={event.sender.id}),\n\n● ɪ ᴀᴍ [{bot_name}](tg://user?id={bot_id})**\n━━━━━━━━━━━━━━━━━━━\n\n"
        TEXT += f"● **ᴍʏ ᴅᴇᴠᴇʟᴏᴘᴇʀ ➥ [ʀᴏʏ ᴇᴅɪᴛx](https://t.me/ROY_EDITX)**\n\n"
        TEXT += f"● **xʙᴏᴛꜱ ᴠᴇʀsɪᴏɴ ➥** `M3.3`\n"
        TEXT += f"● **ᴘʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ ➥** `3.11.3`\n"
        TEXT += f"● **ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ ➥** `{__version__}`\n━━━━━━━━━━━━━━━━━"
        await event.client.send_file(
                    event.chat_id,
                    "https://graph.org/file/9d0cc6a4aaa021b546323.jpg",
                    caption=TEXT, 
                    buttons=START_BUTTON
      )
