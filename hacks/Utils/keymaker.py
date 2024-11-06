import keyboard
import threading
def keyz(newkey, execable):
    while True:
        key = keyboard.read_key()
        if key == 'enter':
            pass
        if key == newkey:
            exec(execable)

def setkey(newkey, execable):
    kb = threading.Thread(target=keyz, args=(newkey, execable))
    kb.start()