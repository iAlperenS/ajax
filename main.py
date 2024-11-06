import colorama, os, time, sys
import configparser
from system.check import *
from hacks.Utils.Timers import *
from hacks.enchant_book import *
from Logger import *
from banner import Banner, Succes, Inputan, log, ColorMenu
from hacks.Dlljector.injectors import *
from banner import *
from system.ui.localizer import *
from colorama import Fore
try:
    colorama.init(); Config = configparser.ConfigParser(); Config.read("config.txt"); mco = Config.get("Menu", "Banner")
    banner = Banner(color=Fore.MAGENTA); local = localize()
    clear(); firstOption = Config.get("Start", "fp")
    firstOption = int(firstOption)
    if firstOption == "0" or firstOption == 0:
        log(num="1", text=f" {local['Lang']['Langs']['eng']}");log(num="2", text=f" {local['Lang']['Langs']['tr']}"); ll = Inputan(tabs="  ", text=f" {local['Lang']['1']} ")
        lang = Config.get("Start", "lang")
        if ll == 1 or ll == "1":
            lang = str(lang); lang = "English"; Config.set("Start", "lang", str(lang))
        elif ll == 2 or ll == "2":
            lang = str(lang); lang = "Turkce"; Config.set("Start", "lang", str(lang))
        lang = Config.get("Start", "lang")
        firstOption += 1; Config.set("Start", "fp", str(firstOption))
        with open("config.txt", "w") as configfile:
            Config.write(configfile)
        clear(); log(tabs="",num="~", text=f" {local['Description'][f'{lang}']}"); Inputan(c2=Fore.GREEN, text=f" {Fore.WHITE}{local['Enter'][f'{lang}']}")
    print(banner)
    try:
        count = Config.get("Counter", "count")
        count = int(count)
        count += 1
        Config.set("Counter", "count", str(count))
        # Checking shits
        internet_check(); version_check(); check_api(); check_cord()
        lang = str(lang)
        with open("config.txt", "w") as configfile:
            Config.write(configfile)
        lang = Config.get("Start", "lang")
        license = input(Fore.WHITE + f"[#] {local[f'{lang}']['Main']['license_key']} ")
    except:
        Inputan(num="!", text=" Please restart program!")
        sys.exit()
        os._exit(0)
    def refresh():
        os.system("cls")
        print(banner)
    def MainMenu():
        os.system("cls")
        print(banner)
        global zx
        print(); log(num=">", text=f" {local[f'{lang}']['Gui']['Settings']}");
        log(num="0", text=f" {local[f'{lang}']['Gui']['0']}");log(num="1", text=f" {local[f'{lang}']['Gui']['1']}");log(num="2", text=f" {local[f'{lang}']['Gui']['2']}");log(num="3", text=f" {local[f'{lang}']['Gui']['3']}");log(num="4", text=f" {local[f'{lang}']['Gui']['4']}");log(num="5", text=f" {local[f'{lang}']['Gui']['5']}")
        zx = Inputan(c1=Fore.WHITE, c2=Fore.GREEN, num=">", text=f" {Fore.WHITE}")

    if license:
        Log.write(f"Checking...")
        Log.write(f"Entered the client with license ({license})")
        Log.write(f"Internet connection already have!")
        Succes(text=f" {local[f'{lang}']['Main']['succes_license']}")
        time.sleep(1.2)
        def start():
            refresh()
            MainMenu()
            Log.write(f"Selected ({zx})")
            if zx == 0 or zx == "0":
                refresh()
                ColorMenu()
                x = Inputan(c1=Fore.WHITE, c2=Fore.GREEN, num=">", text=f" {Fore.WHITE}")
                if x == 5 or x == "5":
                    MainMenu()
                    start()
            elif zx == 1 or zx == "1":
                oto_kitap()
                Start_Timer()
                while 1:
                    EnchantMenu(color=Fore.LIGHTCYAN_EX)
                    time.sleep(3)
                    os.system("cls")
            elif zx == 2 or zx == "2":
                os.system("cls")
                craftrise_checker_menu()
            elif zx == 3 or zx == "3":
                clear()
                craftrise_gen_menu()
            elif zx == 4 or zx == "4":
                refresh()
                log(text=f" {local[f'{lang}']['Gui4']['press_cord']}");n()
            elif zx == 5 or zx == "5":
                refresh()
                Dll = Inputan(tabs="  ", text=f" {local[f'{lang}']['Gui5']['process_name']}: ")
                Pid = find_pid_by_title(f"{Dll}")
                DllFile = Inputan(tabs="  ", text=f" {local[f'{lang}']['Gui5']['dll_file']}: ")
                injector(pid=Pid, dll=DllFile)
                
        start()
    else:
        sys.exit()
except Exception as f:
    Log.write(f"An error occured: {f}")