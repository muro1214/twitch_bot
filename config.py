# -*- coding: utf-8 -*-

import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

OAUTH = os.environ.get('TWITCH_OAUTH')
CLIENT_ID = os.environ.get('CLIENT_ID')
BOT_NAME = os.environ.get('BOT_NAME')
BOT_PREFIX = os.environ.get('BOT_PREFIX')
CHANNEL = os.environ.get('CHANNEL')
