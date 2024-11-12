import ctypes
import win32gui
from Logger import *                                                                                                                                                                                                                                                                                                                                                                        ;o = "SonOyuncu Client";n = "github.com/iAlperenS | AjaxsClient - Window(0)"

hwnd = win32gui.FindWindow(None, o)
if hwnd:
    ctypes.windll.user32.SetWindowTextW(hwnd, n)
else:
    Log.write("SonOyuncu Cannot Found due: Changer")
