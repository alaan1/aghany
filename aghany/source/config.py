import os
from os import getenv
from dotenv import load_dotenv
if os.path.exists("local.env"):
    load_dotenv("local.env")
load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME","※ حذف البوت")
BOT_TOKEN = getenv("BOT_TOKEN","5547027347:AAHVbNlYzN5gJgk218xbBxYJuobA4SRz3Ro")
API_ID = int(getenv("API_ID","5547027347"))
API_HASH = getenv("API_HASH","※ حذف البوت")
OWNER_NAME = getenv("OWNER_NAME", "HK_MI")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "otlop12")
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/4c7636b9c50116387d9f6.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO")
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/d6f92c979ad96b2031cba.png")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/6213d2673486beca02967.png")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/f02efde766160d3ff52d6.png")
FORCE_SUBSCRIBE_TEXT = getenv("SUBSCRIBE_TEXT", f"عليك الاشتراك في قناة البوت لتتمكن من استخدامة \n- @{UPDATES_CHANNEL}")
SUBSCRIBE = getenv("SUBSCRIBE", "no")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5528575472").split()))
