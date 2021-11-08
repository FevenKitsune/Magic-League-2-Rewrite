from discord import Guild
from db.db import config
from db.defaults import defaults


def getConfig(configType: str, guildID: int) -> str:
    configCursor = config.cursor()
    payload = (guildID, configType)
    configCursor.execute("SELECT config_value FROM config WHERE guild_id = ? AND config_name = ? LIMIT 1", payload)
    data = configCursor.fetchone()
    configCursor.close()
    if not data:
        data = defaults[configType]

    return str(data[0])
