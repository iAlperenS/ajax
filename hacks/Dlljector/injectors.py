import colorama; from colorama import *
import psutil, datetime, os
from banner import *
from Logger import Log
from pyinjector import inject
colorama.init()

dict_pids = {
    p.info["pid"]: p.info["name"]
    for p in psutil.process_iter(attrs=["pid", "name"])
}

def find_pid_by_title(title):
    for proc in psutil.process_iter(['pid', 'name']):
        if title.lower() in proc.info['name'].lower():
            log(tabs="  ", text=f" Finded: {title} : {proc.info['pid']}")
            return proc.info['pid']
    log(tabs="  ", text=f" I cannot find a {title}'s pid")
    Log.write(dict_pids)
    log(tabs="  ", text=" All pids was writed at logs!")
    return None

def injector(pids="Dll", dll="None"):
    log(tabs="  ", text=f" Injecting [{Fore.LIGHTBLUE_EX}{pids}{Fore.RESET}]")
    inject(pids, dll)
