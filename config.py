# -*- coding: utf-8 -*-

import os
from pathlib import Path
from dotenv import load_dotenv

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

OAUTH = os.getenv('TWITCH_OAUTH')
CLIENT_ID = os.getenv('CLIENT_ID')
BOT_NAME = os.getenv('BOT_NAME')
BOT_PREFIX = os.getenv('BOT_PREFIX')
CHANNEL = os.getenv('CHANNEL')

print(OAUTH)
