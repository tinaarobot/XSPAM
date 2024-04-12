import logging

from telethon import TelegramClient

from os import getenv
from ROYEDITX.data import AVISHA


logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s', level=logging.WARNING)


API_ID = 18136872
API_HASH = "312d861b78efcd1b02183b2ab52a83a4"
CMD_HNDLR = getenv("CMD_HNDLR", default=".")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", None)
HEROKU_API_KEY = getenv("HEROKU_API_KEY", None)

BOT_TOKEN = getenv("BOT_TOKEN", default=None)

SUDO_USERS = list(map(lambda x: int(x), getenv("SUDO_USERS", default="6922271843").split()))
for x in AVISHA:
    SUDO_USERS.append(x)
OWNER_ID = int(getenv("OWNER_ID", default="6922271843"))
SUDO_USERS.append(OWNER_ID)


# ------------- CLIENTS -------------

X1 = TelegramClient('X1', API_ID, API_HASH).start(bot_token=BOT_TOKEN)
