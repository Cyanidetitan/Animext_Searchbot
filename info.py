import re
from os import environ

# Bot information
SESSION = environ.get('SESSION', 'Media_search')
USER_SESSION = environ.get('USER_SESSION', 'User_Bot')
API_ID = int(environ['API_ID'])
API_HASH = environ['API_HASH']
BOT_TOKEN = environ['BOT_TOKEN']

# Bot settings
MAX_RESULTS = int(environ.get('MAX_RESULTS', 10))
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', False))

# Admins, Channels & Users
ADMINS = [int(admin) if re.search('^\d+$', admin) else admin for admin in environ['ADMINS'].split()]
CHANNELS = [int(ch) if re.search('^.\d+$', ch) else ch for ch in environ['CHANNELS'].split()]
auth_users = [int(user) if re.search('^\d+$', user) else user for user in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []

# MongoDB information
DATABASE_URI = "mongodb+srv://animxt:1234@cluster0.10idlop.mongodb.net/?retryWrites=true&w=majority"
DATABASE_NAME = "Animxt Encodes"
COLLECTION_NAME = "Animxt"

# Messages
START_MSG = """
**Hello,

Please use /search to get started.

Search anime in inline mode.

Note: I can only give you the files of anime that were aired in @Latest_ongoing_airing_anime **

Here you can search files in inline mode. Just press following buttons and start searching.
"""

SHARE_BUTTON_TEXT = 'Checkout {username} for searching best quality encodes done by @animxt'
