from telethon import __version__, events, Button

from config import X1


START_BUTTON = [
    [
        Button.inline("ʜᴇʟᴘ ᴄᴏᴍᴍᴀɴᴅs", data="help_back")
    ],
    [
        Button.url("sᴜᴘᴘᴏʀᴛ", "https://t.me/AlonesHeaven"),
        Button.url("ʀᴇᴘᴏ", "https://github.com/TeamAloneOp/AloneXSpam/fork")
    ]
]


@X1.on(events.NewMessage(pattern="/start"))
async def start(event):              
    if event.is_private:
        ROYEDITX = await event.client.get_me()
        bot_name = ROYEDITX.first_name
        bot_id = ROYEDITX.id
        TEXT = f"**ʜᴇʏ [{event.sender.first_name}](tg://user?id={event.sender.id}),\n\nɪ ᴀᴍ [{bot_name}](tg://user?id={bot_id})**\n━━━━━━━━━━━━━━━━━━━\n\n"
        TEXT += f"» **ᴍʏ ᴅᴇᴠᴇʟᴏᴘᴇʀ : [𝐀ʟᴏɴᴇ](https://t.me/ALONE_WAS_BOT)**\n\n"
        TEXT += f"» **xʙᴏᴛꜱ ᴠᴇʀsɪᴏɴ :** `M3.3`\n"
        TEXT += f"» **ᴘʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `3.11.3`\n"
        TEXT += f"» **ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `{__version__}`\n━━━━━━━━━━━━━━━━━"
        await event.client.send_file(
                    event.chat_id,
                    "https://telegra.ph//file/9e8ce3092848a1bc5d9d6.jpg",
                    caption=TEXT, 
                    buttons=START_BUTTON
      )
