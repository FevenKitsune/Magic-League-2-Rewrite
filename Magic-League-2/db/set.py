from discord import Guild
from db.db import config
from db.defaults import defaults


def set(configType: str, guildID: int, data: str) -> str:
    configCursor = config.cursor()
    payload = (str(guildID), configType, data)
    purge = (str(guildID), configType)
    
    configCursor.execute("DELETE FROM config WHERE id = ? AND name = ?", purge)
    configCursor.execute("INSERT INTO config (id, name, value) VALUES (?, ?, ?)", payload)

    config.commit()
    configCursor.close()
