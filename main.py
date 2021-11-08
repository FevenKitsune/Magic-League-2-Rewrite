##
# MAGICLEAGUE2 ALPHA
# APPENDED June 3rd, 2020: MagicLeague2 is licensed under CC0 1.0 Universal (CC0 1.0) Public Domain Dedication
# APPENDED June 3rd, 2020: Updated to latest source code, contains bug fixes implemeneted May 5th, 2020
# APPENDED April 20th, 2021: Bugfix, fixed bug where bot will continuously loop trying to remove a role.
###

###
# ///// NOTES /////
#
# SIGN/RELEASE TAGS:
# %playermention% - Mention signed/released player
# %teammention% - Mention signing/releasing team
# %playername% - Name of signed/released player
# %teamname% - Name of signing/releasing team
###

import discord
from discord.ext import commands
import sqlite3
import logging
import shlex
import json
from os import environ
from fuzzywuzzy import process
from db import db
from db.defaults import defaults
from core.prefix import get_prefix

print("Loading...")
logging.basicConfig(level=logging.INFO)
versionNumber = "FINAL RELEASE (Patched 4/20/2021)"

db.init()
client = commands.Bot(description=defaults["description"], command_prefix=get_prefix)


@client.event
async def on_ready():
    startup = logging.getLogger("startup")
    startup.info("===MagicLeague 2 is now starting up!===")
    startup.info('USERNAME: {0.user}'.format(client))
    startup.info('ID: {0.user.id}'.format(client))
    startup.info("SERVERS: " + str(sum(1 for x in client.guilds)))

if __name__ == "__main__":
    client.run(environ.get("bot-key"))
