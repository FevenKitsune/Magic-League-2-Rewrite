from discord import Guild
from db.db import config
from db.defaults import defaults


def get(configType: str, guildID: int) -> str:
    configCursor = config.cursor()
    payload = (str(guildID), configType)

    data = str(list(configCursor.execute("SELECT value FROM config WHERE id = ? AND name = ? LIMIT 1", payload)))[3:-4]

    configCursor.close()
    if not data: data = defaults[configType]
    
    return data