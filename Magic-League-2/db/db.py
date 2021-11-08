from os import environ
from db.defaults import defaults
import sqlite3
import logging


databaseLocation = environ.get("bot-database")
if databaseLocation is None:
    databaseLocation = ":memory:"

config = sqlite3.connect(databaseLocation)

def init():
    configCursor = config.cursor()
    databaseLog = logging.getLogger("database")
    payload =  (str(defaults["defaultTable"]), )
    print(defaults["defaultTable"])
    databaseLog.info("Looking for default table...")
    configCursor.execute("""
        SELECT count(name) 
        FROM sqlite_master
        WHERE type='table'
        AND name=?
        """, payload)

    fetch = configCursor.fetchone()[0]

    if fetch == 1:
        databaseLog.info("Default table found.")
    else:
        databaseLog.warning("Default table was not found. Creating table.")
        configCursor.execute("""CREATE TABLE IF NOT EXISTS ? (guild_id INTEGER PRIMARY KEY, config_name TEXT, config_value TEXT);""", payload)

    config.commit()
    configCursor.close()