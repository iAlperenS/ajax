import threading
import time
from system.data import *

def TimerWithOut():
    while 1:
        time.sleep(1)
        Data.timer += 1

def Start_Timer():
    tm = threading.Thread(target=TimerWithOut)
    tm.start()