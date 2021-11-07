from os import environ
import sqlite3


databaseLocation = environ.get("bot-database")
if databaseLocation is None:
    databaseLocation = ":memory:"

config = sqlite3.connect(databaseLocation)
config.text_factory = str
