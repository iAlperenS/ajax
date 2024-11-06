import datetime, os
import configparser
from configparser import *

Config = configparser.ConfigParser()
class Log():
    @staticmethod
    def write(text):
        Config.read("config.txt")
        count = Config.get("Counter", "count")
        count = int(count)
        count += 1
        now = datetime.datetime.now()
        d = now.strftime("%Y-%m-%d")
        newpath = rf'logs\{d}' 
        if not os.path.exists(newpath):
            os.makedirs(newpath)
        with open(file=f"logs\\{d}\\log-{count}.txt", mode="a") as conf:
            now = datetime.datetime.now()
            d = now.strftime("%Y-%m-%d")
            h = datetime.datetime.now().hour  # s
            m = datetime.datetime.now().minute  # d
            s = datetime.datetime.now().second
            conf.write(f"[{d} {h}:{m}:{s}] [LOG] {text}\n")
    @staticmethod
    def writeout(text):
        now = datetime.datetime.now()
        d = now.strftime("%Y-%m-%d")
        h = datetime.datetime.now().hour  # s
        m = datetime.datetime.now().minute  # d
        s = datetime.datetime.now().second
        newpath = rf'output\{d}' 
        if not os.path.exists(newpath):
            os.makedirs(newpath)
        with open(file=f"output\\{d}\\{d}-{h}-{m}-{s}.txt", mode="a") as conf:
            now = datetime.datetime.now()
            conf.write(f"[{d} {h}:{m}:{s}] [Account] {text}\n")