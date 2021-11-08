import discord
from db.defaults import defaults
from db.get import getConfig
from db.set import setConfig

async def get_prefix(bot, message):
    """Checks if the bot has a configuration tag for the prefix. Otherwise, gets the default."""
    if isinstance(message.channel, discord.DMChannel):
        return defaults["prefix"]
    prefix = getConfig("prefix", message.guild.id)
    print(f"PREFIX: {prefix}")
    return prefix