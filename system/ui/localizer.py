import json
from system.data import Data
import configparser
Config = configparser.ConfigParser()

def get_lang():
    Config.read("config.txt")
    lang = Config.get("Start", "lang")
    return lang

def localize():
    with open(mode="r", file=Data.localFile, encoding="utf-8") as l:
        jj = l.read()
    localize = json.loads(jj)
    return localize