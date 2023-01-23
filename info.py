import re
from os import environ

# Bot information
SESSION = 'Animxt_Encodes_bot'
USER_SESSION = 'BQAmv_AtfnxRFrYCx3Cw9jPiZfDUk9N7RsDlleadZOXq9kCxYZVg6reyjRXIrmABSzGRY-yeal1DdiP6bDBttupOECgoq8ALg3pLUwbGV0dxHpfVJ-eXa1Pv_sDxl7ko4STUI5T9gQbQy04iUP5cqxvslIol5-Fd8kRkU3vP338U5p8lCzcAYYe-XlvrIxlc3Rw292t_nsarmpdCVQKZKCc4HLgEuimy8VY4jdPdvIpJTpwph6s9ozP-72gJhgWjAsFIbSbTxHeAcoo0s40NHwjXjKLkwicRLn2lnEs6Yuc0uRy9TuYDPqBncx-4FhnJU5DOgmi0ouU43VqQZA76bQuuAAAAAUAx8BsA'
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
DATABASE_NAME = "Animxt Encodes"
COLLECTION_NAME = 'Animxt'

# Messages
START_MSG = """
**Hello,

Please use /search to get started.

Search anime in inline mode.

Note: I can only give you the files of anime that were aired in @Latest_ongoing_airing_anime **

Here you can search files in inline mode. Just press following buttons and start searching.
"""

SHARE_BUTTON_TEXT = 'Checkout {username} for searching best quality encodes done by @animxt'
