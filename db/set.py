from discord import Guild
from db.db import config
from db.defaults import defaults


def setConfig(configType: str, guildID: int, data: str) -> str:
    configCursor = config.cursor()
    payload = (guildID, configType, data)
    purge = (guildID, configType)
    
    configCursor.execute("DELETE FROM config WHERE guild_id = ? AND config_name = ?", purge)
    configCursor.execute("INSERT INTO config (guild_id, config_name, config_value) VALUES (?, ?, ?)", payload)

    config.commit()
    configCursor.close()
