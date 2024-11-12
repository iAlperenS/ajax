import requests, os
from pynput import keyboard
from os import system
import threading
from PIL import ImageGrab
import pyautogui, time, colorama
from colorama import Fore, Style
colorama.init()
zaman = 0                                                                                                                                                                                                                                                                                                               ;system("title github.com/iAlperenS v1.2")

def set_cord(eski_x, eski_y):
    screen_width, screen_height = pyautogui.size()
    eski_genislik = 1280
    eski_yukseklik = 720
    yeni_genislik = screen_width
    yeni_yukseklik = screen_height
    genislik_orani = yeni_genislik / eski_genislik
    yukseklik_orani = yeni_yukseklik / eski_yukseklik

    con1_x = int(eski_x * genislik_orani); con1_y = int(eski_y * yukseklik_orani)
    return (con1_x, con1_y)

def bestie():
    class Webhook:
            @staticmethod
            def send(url, text):
                payload = {
                    'content': f'{text}',
                }

                # Webhook'a POST isteği gönderin
                response = requests.post(url=url, data=payload)

    def scs(left, top, right, bottom, name):
        screenshot = ImageGrab.grab(bbox=(left, top, right, bottom))

        # Ekran görüntüsünü kaydet
        screenshot.save(fr"{name}.png")

    def ocr_space_file(filename, overlay=False, api_key='K85456255888957', language='eng', engine='2'):
        """ OCR.space API request with local file.
            Python3.5 - not tested on 2.7
        :param filename: Your file path & name.
        :param overlay: Is OCR.space overlay required in your response.
                        Defaults to False.
        :param api_key: OCR.space API key.
                        Defaults to 'helloworld'.
        :param language: Language code to be used in OCR.
                        List of available language codes can be found on https://ocr.space/OCRAPI
                        Defaults to 'en'.
        :return: Result in JSON format.
        """

        payload = {'isOverlayRequired': overlay,
                'apikey': api_key,
                'language': language,
                'OCREngine': engine
                }
        with open(filename, 'rb') as f:
            r = requests.post('https://api.ocr.space/parse/image',
                            files={filename: f},
                            data=payload,
                            )
        return r.json()

    def ocr_space_url(url, overlay=False, api_key='helloworld', language='eng'):
        """ OCR.space API request with remote file.
            Python3.5 - not tested on 2.7
        :param url: Image url.
        :param overlay: Is OCR.space overlay required in your response.
                        Defaults to False.
        :param api_key: OCR.space API key.
                        Defaults to 'helloworld'.
        :param language: Language code to be used in OCR.
                        List of available language codes can be found on https://ocr.space/OCRAPI
                        Defaults to 'en'.
        :return: Result in JSON format.
        """

        payload = {'url': url,
                'isOverlayRequired': overlay,
                'apikey': api_key,
                'language': language,
                }
        r = requests.post('https://api.ocr.space/parse/image',
                        data=payload,
                        )
        return r.content.decode()

    def log(text, text2):
        print(Fore.MAGENTA + "[" + Fore.LIGHTGREEN_EX + "LOG" + Fore.MAGENTA + "]" + Fore.MAGENTA + "[" + Fore.LIGHTGREEN_EX + str(text2) + Fore.MAGENTA + "]"  +Fore.LIGHTWHITE_EX + text)

    def on_press(key, newkey):
        global zaman
        wlx, wty = set_cord(1043, 282); clx, cty = set_cord(0, 169)
        wrx, wby = set_cord(1287, 302); crx, cby = set_cord(265, 188)
        try:
            if key.char == newkey:
                log(f" Using OCR ({x})", zaman)
                log(" Taking cords (1)", zaman)
                time.sleep(1.5)
                scs(0, cty, crx, cby, "scren") #left, top, right, bottom
                scs(wlx, wty, wrx, wby, "world")
                zaman += 1
                log(f" Taked cords (2)", zaman)
                test_file = ocr_space_file(filename=r'scren.png', language='eng', engine=x)
                world = ocr_space_file(filename=r'world.png', language='eng', engine=x)
                print("Cords: ", test_file['ParsedResults'][0]['ParsedText'])
                print("World: ", world['ParsedResults'][0]['ParsedText'])
                Webhook.send("https://discord.com/api/webhooks/1283849508270374912/O3tpwYKxt7oKpKxB3tR_pIDVTa-mVxLj-k8jwVoLQzbyPcJR_l6a3__ixhog0AZ6fE0U", f"{world['ParsedResults'][0]['ParsedText']}\n{test_file['ParsedResults'][0]['ParsedText']}")
        except AttributeError:
            pass

    def red(text):
        os.system(""); faded = ""
        for line in text.splitlines():
            green = 255
            for character in line:
                green -= 5
                
                if green < 0:
                    green = 0            
                faded += (f"\033[38;2;255;{green};0m{character}\033[0m")
            faded += "\n"
        return faded

    def blue(text):
        os.system(""); faded = ""
        for line in text.splitlines():
            green = 0
            for character in line:
                green += 6
                if green > 255:
                    green = 255
                faded += (f"\033[38;2;0;{green};255m{character}\033[0m")
            faded += "\n"
        return faded

    banner = f"""
        ███████╗ █████╗ ███████╗████████╗ ██████╗ ██████╗ ██████╗ ██████╗ ██╗
        ██╔════╝██╔══██╗██╔════╝╚══██╔══╝██╔════╝██╔═══██╗██╔══██╗██╔══██╗██║
        █████╗  ███████║███████╗   ██║   ██║     ██║   ██║██████╔╝██║  ██║██║
        ██╔══╝  ██╔══██║╚════██║   ██║   ██║     ██║   ██║██╔══██╗██║  ██║██║
        ██║     ██║  ██║███████║   ██║   ╚██████╗╚██████╔╝██║  ██║██████╔╝██║
        ╚═╝     ╚═╝  ╚═╝╚══════╝   ╚═╝    ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚═════╝ ╚═╝                                                                   
    """
    print(red(banner))
    print(blue('        github.com/iAlperenS    discord: xalperen    v1.2'))
    print(f"                 {Fore.MAGENTA}[{Fore.LIGHTBLUE_EX}1{Fore.MAGENTA}] {Fore.LIGHTWHITE_EX} Ocr (1) Default and Faster")
    print(f"                 {Fore.MAGENTA}[{Fore.LIGHTBLUE_EX}2{Fore.MAGENTA}] {Fore.LIGHTWHITE_EX} Ocr (2) Better for numbers and #$:")
    # print(f"                 {Fore.MAGENTA}[{Fore.LIGHTBLUE_EX}3{Fore.MAGENTA}] {Fore.LIGHTWHITE_EX} Webhook & Keybinds")
    print(" ")
    global x
    x = input(f"                        {Fore.MAGENTA}[{Fore.LIGHTBLUE_EX}?{Fore.MAGENTA}] {Fore.LIGHTWHITE_EX} Enter the option >: ")
    print(" ")
    print(" ")

    def on_press_wrapper(key):
        on_press(key, "x")

    with keyboard.Listener(on_press=on_press_wrapper) as listener:
        listener.join()

def AutoWord():
    job = threading.Thread(target=bestie)
    job.start()
