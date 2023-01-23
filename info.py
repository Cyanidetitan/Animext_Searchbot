import re
from os import environ

# Bot information
SESSION = 'Animxt_Encodes_bot'
USER_SESSION = 'User_bot'
API_ID = 8858279
API_HASH = 'ef28c3f458143cbcb4271a98a2e9d596'
BOT_TOKEN = '5725647066:AAFgLg8cI8cTsZjyjD66sqxwNPzDLRU0GGs'

# Bot settings
MAX_RESULTS = 20
CACHE_TIME = 300
USE_CAPTION_FILTER = True

# Admins, Channels & Users
ADMINS = [5371981851]
CHANNELS = [-1001693312957]

AUTH_USERS = []

# MongoDB information
DATABASE_URI = "mongodb+srv://animxt:1234@cluster0.10idlop.mongodb.net/?retryWrites=true&w=majority"
DATABASE_NAME = 'Telegram'
COLLECTION_NAME = 'channel_files'

# Messages
START_MSG = """
**Hello,

Please use /search to get started.

Search anime in inline mode.

Note: I can only give you the files of anime that were aired in @Latest_ongoing_airing_anime **

Here you can search files in inline mode. Just press following buttons and start searching.
"""

SHARE_BUTTON_TEXT = 'Checkout {username} for searching best quality encodes done by @animxt'
