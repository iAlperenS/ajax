import os, requests, configparser, pyautogui, sys
from banner import *
from Logger import *
from system.ui.localizer import *
conf = configparser.ConfigParser()
conf.read("config.txt")
lang = get_lang()
local = localize()
def clear():
    os.system("cls")

def check_cord():
    screen_width, screen_height = pyautogui.size()
    eski_genislik = 1280
    eski_yukseklik = 720
    yeni_genislik = screen_width
    yeni_yukseklik = screen_height
    genislik_orani = yeni_genislik / eski_genislik
    yukseklik_orani = yeni_yukseklik / eski_yukseklik
    eski_x = 606; eski_x2 = 517
    eski_y = 319; eski_y2 = 303

    con1_x = int(eski_x * genislik_orani); con1_y = int(eski_y * yukseklik_orani)
    con2_x = int(eski_x2 * genislik_orani); con2_y = int(eski_y2 * yukseklik_orani)
    log(num="!", tabs="", text=f" {local[f'{lang}']['Main']['set_cord1']} {con1_x}, {con1_y}")
    log(num="!", tabs="", text=f" {local[f'{lang}']['Main']['set_cord2']} {con2_x}, {con2_y}")
    Log.write(f"{local[f'{lang}']['Main']['set_cord1']} {con1_x}, {con1_y}")
    Log.write(f"{local[f'{lang}']['Main']['set_cord2']} {con2_x}, {con2_y}")
def internet_check():
    try:
        log(num="!", tabs="", text=f" {local[f'{lang}']['Main']['check_internet']}")
        requests.get('https://github.com')
    except requests.exceptions.ConnectionError:
        print(f"{local[f'{lang}']['Result']['internet1']}")
        os._exit(0)
        sys.exit()

def version_check():
    try:
        log(num="!", tabs="", text=f" {local[f'{lang}']['Main']['check_version']}")
        ver = conf.get("Version", "v")
        ver = float(ver)
        v = requests.get("https://raw.githubusercontent.com/iAlperenS/ajax/main/version.txt")
        v = float(v.text.strip())
        if v > ver:
            print()
            log(c1=Fore.GREEN, num="!",tabs="", text=f" {local[f'{lang}']['Result']['version_1']}")
            Log.write(f"{local[f'{lang}']['Result']['version_1']}")
        else:
            Log.write(f"{local[f'{lang}']['Result']['version_2']}")
    except Exception as f:
        Log.write(f"{local[f'{lang}']['Result']['internet1']} (version)")
        print(f"{local[f'{lang}']['Result']['internet1']} {f}")

def check_api():
    api = requests.get("https://ocr.space/")
    if api.status_code == 200:
        log(num="!",tabs="", text=f" {local[f'{lang}']['Main']['check_api']}")

def check_webhook():
    return False
