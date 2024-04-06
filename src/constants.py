import os

# Various files and directories
STORAGE_DIR = os.path.join(os.getcwd(), 'store')
TEMP_DIR = os.path.join(os.getcwd(), 'temp')
LOGGING_FILE = os.path.join(STORAGE_DIR, 'logging', 'base.log')
DB_FILE = os.path.join(STORAGE_DIR, 'database.json')
AUTH_FILE = os.path.join(STORAGE_DIR, 'auth.json')

TIMEOUT = 45.0

# Misc symbols
GREEN_CHECK = "\U00002705"
RED_X = "\U0000274c"

# Progress bar constants
EMPTY_SQUARE = "□"
FULL_SQUARE = "■"
BAR_SIZE = 40
PROGRESS_UPDATE_MULTIPLE = 50

# Turns out discord has a max number of embed fields...
DISCORD_MAX_EMBED_FIELDS = 25
