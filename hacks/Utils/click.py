import win32, win32api, win32gui, win32con, pyautogui as p, time
#
#
#
#
# ----------------------
#    Win32 Click Bg
# ----------------------
#
#
#
#
def click(cps, ft: False):
    while 1:
        if ft == True:
            p.click()
            d = 1 / cps
            time.sleep(d)
        else:
            return "Waiting.."

def clickw32(x, y, wind):
    hWnd = win32gui.FindWindow(None, wind)
    lParam = win32api.MAKELONG(x, y)

    hWnd1= win32gui.FindWindowEx(hWnd, None, None, None)
    win32api.PostMessage(hWnd1, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, lParam)
    win32api.PostMessage(hWnd1, win32con.WM_LBUTTONUP, None, lParam)
def clickshiftw32(x, y, wind):
    hWnd = win32gui.FindWindow(None, wind)
    lParam = win32api.MAKELONG(x, y)

    hWnd1= win32gui.FindWindowEx(hWnd, None, None, None)
    win32gui.SendMessage(hWnd1, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON | win32con.MK_SHIFT, lParam)
    win32gui.SendMessage(hWnd1, win32con.WM_LBUTTONUP, None, lParam)