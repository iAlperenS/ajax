import colorama, datetime, requests, configparser
from system.data import *
from colorama import *
colorama.init()
config = configparser.ConfigParser()
config.read("config.txt")
version = config.get("Version", "v")
res = Fore.RESET
def log(tabs="          ", c1=Fore.RED, c2=Fore.WHITE, num=">", text="test"):
    print(f"{tabs}" + c1 + "[" + c2 + str(num) + c1 + "]" + c2 + text)
def Inputan(tabs="      ", c1=Fore.RED, c2=Fore.WHITE, num=">", text="test"):
    return input(f"{tabs}" + c1 + "[" + c2 + str(num) + c1 + "]" + c2 + text)
def Succes(c1=Fore.LIGHTBLACK_EX, c2=Fore.GREEN, text="123"):
    print(c1 + "[" + c2 + "+" + c1 + "]" + c2 + text)
def ColorMenu():
    print(); log(num=">", text=" Colors <#>");log(num="0", text=" Red");log(num="1", text=" Blue");log(num="2", text=" Green");log(num="3", text=" Magenta");log(num="4", text=" Cyan");log(num="5", text=" Exit")
def n():
    print()
def craftrise_gen_menu(color=Fore.RED, c2=Fore.WHITE):
    print(Banner())

def craftrise_checker_menu(color=Fore.LIGHTRED_EX, c2=Fore.WHITE):
    reset = Fore.RESET; green = Fore.GREEN;yellow=Fore.YELLOW; space = " "
    lapis_text = f"║  {c2}%1               ({Fore.BLUE}{Data.lapis}{reset}) [{Fore.GREEN}{Data.lapis} {Fore.LIGHTBLUE_EX}/{reset}]"
    kitap_text = f"║  {c2}%10              ({Fore.YELLOW}{Data.kitap}{reset}) [{Fore.GREEN}{Data.kitap}{Fore.LIGHTBLUE_EX}/{reset}]"
    captcha_text = f"║  {c2}%50              ({Fore.LIGHTRED_EX}{Data.capthca}{Fore.RESET})"
    xp_text = f"║  {c2}%99              ({Fore.LIGHTGREEN_EX}0.1{Fore.RESET})"
    lapis_text = f"{lapis_text:<75}{color}║"
    kitap_text = f"{kitap_text:<75}{color}║"
    captcha_text = f"{captcha_text:<60}{color}║"
    xp_text = f"{xp_text:<60}{color}║"
    print(Banner())
    log(text=f" {Fore.LIGHTCYAN_EX}2024 CraftRise Checker")
    try:
        Data.hit = Data.good / Data.bad
    except:
        Data.hit = 0
    print(f''' {reset}         
    {color}╔════════════════════════════════════════════╗     {color}╔════════════════════════════════════════════╗ 
    ║                 {c2}   %  ({green}{2}{reset}){space * (14 - len(str(2)))}{color}     ║     ║                 {c2}   DATA  ({green}0{reset}){space * (14 - len(str(0)))}{color}  ║ 
    {color}╠════════════════════════════════════════════╣     {color}╠════════════════════════════════════════════╣ 
    {lapis_text}     ║  {c2}Hit                ({Fore.LIGHTGREEN_EX}{Data.hit}{Fore.RESET}){space * (21 - len(str(Data.hit)))}{color}║
    {kitap_text}     ║  {c2}Good               ({Fore.LIGHTGREEN_EX}{Data.good}{Fore.RESET}){space * (21 - len(str(Data.good)))}{color}║
    {captcha_text}     ║  {c2}Bad                ({Fore.LIGHTGREEN_EX}{Data.bad}{Fore.RESET}){space * (21 - len(str(Data.bad)))}{color}║
    {xp_text}     ║  {c2}Other              ({Fore.LIGHTGREEN_EX}{Data.other}{Fore.RESET}){space * (21 - len(str(Data.other)))}{color}║
    {color}╠════════════════════════════════════════════╣     ╠════════════════════════════════════════════╣
    ║{c2}                 Account  ({green}{0}{reset}){color}               ║    
    {color}╠════════════════════════════════════════════╣
    ║  {c2}Coins              ({Fore.LIGHTGREEN_EX}{Data.coin}{Fore.RESET}){space * (21 - len(str(Data.sc_rc)))}{color}║    
    {color}║  {c2}VIPS               ({Fore.LIGHTGREEN_EX}{Data.vip}{Fore.RESET}){space * (21 - len(str(Data.sc_rc)))}{color}║                
    {color}║  {c2}RC+                ({Fore.LIGHTGREEN_EX}{Data.sc_rc}{Fore.RESET}){space * (21 - len(str(Data.sc_rc)))}{color}║     
    {color}╠════════════════════════════════════════════╣  
    Estimated reamining time: {Data.timer}{Fore.LIGHTBLUE_EX}s''')
def EnchantMenu(color=Fore.LIGHTRED_EX, c2=Fore.WHITE):
    reset = Fore.RESET; green = Fore.GREEN;yellow=Fore.YELLOW; num = 2; space = " "
    k3, v4, y2, s1, p4, g3, k4, i1, d3 = Data.kir3, Data.ver4, Data.yum2, Data.son1, Data.pro4, Data.gan3, Data.kes4, Data.ipe1, Data.der3 
    checked, good, ratelimit, xprate = 0,0,0,0
    lapis_rate = Data.lapis / 64; lapis_rate = int(lapis_rate)
    kitap_rate = Data.kitap / 64; kitap_rate = int(kitap_rate)
    try: 
        verim = Data.good / Data.kitap
        try:
            verim = f"{str(verim)[0]}{str(verim)[1]}{str(verim)[2]}{str(verim)[3]}{str(verim)[4]}"
        except IndexError:
            try:
                verim = f"{str(verim)[0]}{str(verim)[1]}{str(verim)[2]}{str(verim)[3]}"
            except:
                try:
                    verim = f"{str(verim)[0]}{str(verim)[1]}{str(verim)[2]}"
                except:
                    verim = f"{str(verim[0])}"
    except:
        verim = 0

    try:
        book_rate = Data.kitap / Data.lapis
        try:
            book_rate = f"{str(book_rate)[0]}{str(book_rate)[1]}{str(book_rate)[2]}{str(book_rate)[3]}{str(book_rate)[4]}"
        except IndexError:
            try:
                book_rate = f"{str(book_rate)[0]}{str(book_rate)[1]}{str(book_rate)[2]}{str(book_rate)[3]}"
            except:
                try:
                    book_rate = f"{str(book_rate)[0]}{str(book_rate)[1]}{str(book_rate)[2]}"
                except:
                    book_rate = f"{str(book_rate[0])}"
    except:
        book_rate = 0

    try:
        lapis_r = Data.lapis / 3
    except:
        lapis_r = 0
    lapis_text = f"║  {c2}Lapis              ({Fore.BLUE}{Data.lapis}{reset}) [{Fore.GREEN}{lapis_rate} {Fore.LIGHTBLUE_EX}stack{reset}]"
    kitap_text = f"║  {c2}Kitap              ({Fore.YELLOW}{Data.kitap}{reset}) [{Fore.GREEN}{kitap_rate}{Fore.LIGHTBLUE_EX} stack{reset}]"
    captcha_text = f"║  {c2}Checked Captcha    ({Fore.LIGHTRED_EX}{Data.capthca}{Fore.RESET})"
    xp_text = f"║  {c2}XP Rate            ({Fore.LIGHTGREEN_EX}%{Data.xp_rate}{Fore.RESET})"
    lapis_text = f"{lapis_text:<75}{color}║"
    kitap_text = f"{kitap_text:<75}{color}║"
    captcha_text = f"{captcha_text:<60}{color}║"
    xp_text = f"{xp_text:<60}{color}║"
    print(Banner())
    log(text=" Start AutoEnchant with press 'r' and pause with 'p'")
    print(f''' {reset}         
    {color}╔════════════════════════════════════════════╗     {color}╔════════════════════════════════════════════╗ 
    ║                 {c2}   MAIN  ({green}{num}{reset}){space * (14 - len(str(num)))}{color}  ║     ║                 {c2}   USER  ({green}0{reset}){space * (14 - len(str(num)))}{color}  ║ 
    {color}╠════════════════════════════════════════════╣     {color}╠════════════════════════════════════════════╣ 
    {lapis_text}     ║  {c2}Verim              ({Fore.LIGHTGREEN_EX}{verim}{Fore.RESET}){space * (21 - len(str(verim)))}{color}║
    {kitap_text}     ║  {c2}Book Rate          ({Fore.LIGHTGREEN_EX}{book_rate}{Fore.RESET}){space * (21 - len(str(book_rate)))}{color}║
    {captcha_text}     ║  {c2}Lapis Rate         ({Fore.LIGHTGREEN_EX}{lapis_r}{Fore.RESET}){space * (21 - len(str(lapis_r)))}{color}║
    {xp_text}     ║  {c2}30s                ({Fore.LIGHTGREEN_EX}{v4}{Fore.RESET}){space * (21 - len(str(v4)))}{color}║
    {color}╠════════════════════════════════════════════╣     {color}╠════════════════════════════════════════════╣ 
    ║{c2}                    BOOKS  ({green}{0}{reset}){color}              ║     ║{c2}                    GEARS    {color}               ║ 
    {color}╠════════════════════════════════════════════╣     {color}╠════════════════════════════════════════════╣
    ║  {c2}V4                 ({Fore.LIGHTGREEN_EX}{v4}{Fore.RESET}){space * (21 - len(str(v4)))}{color}║     ║  {c2}Kask               ({Fore.LIGHTGREEN_EX}{v4}{Fore.RESET}){space * (21 - len(str(v4)))}{color}║
    {color}║  {c2}K3                 ({Fore.LIGHTGREEN_EX}{k3}{Fore.RESET}){space * (21 - len(str(k3)))}{color}║     ║  {c2}Cp                 ({Fore.LIGHTGREEN_EX}{v4}{Fore.RESET}){space * (21 - len(str(v4)))}{color}║                
    {color}║  {c2}Y2                 ({Fore.LIGHTGREEN_EX}{y2}{Fore.RESET}){space * (21 - len(str(y2)))}{color}║     ║  {c2}Pant               ({Fore.LIGHTGREEN_EX}{v4}{Fore.RESET}){space * (21 - len(str(v4)))}{color}║
    {color}║  {c2}S1                 ({Fore.LIGHTGREEN_EX}{s1}{Fore.RESET}){space * (21 - len(str(s1)))}{color}║     ║  {c2}Bot                ({Fore.LIGHTGREEN_EX}{v4}{Fore.RESET}){space * (21 - len(str(v4)))}{color}║
    {color}║  {c2}K4                 ({Fore.LIGHTGREEN_EX}{k4}{Fore.RESET}){space * (21 - len(str(k4)))}{color}║     ║  {c2}Yay                ({Fore.LIGHTGREEN_EX}{v4}{Fore.RESET}){space * (21 - len(str(v4)))}{color}║
    {color}║  {c2}I1                 ({Fore.LIGHTGREEN_EX}{i1}{Fore.RESET}){space * (21 - len(str(i1)))}{color}║     ║  {c2}Kılıç              ({Fore.LIGHTGREEN_EX}{v4}{Fore.RESET}){space * (21 - len(str(v4)))}{color}║
    {color}║  {c2}P4                 ({Fore.LIGHTGREEN_EX}{p4}{Fore.RESET}){space * (21 - len(str(p4)))}{color}║     ║  {c2}Kazma              ({Fore.LIGHTGREEN_EX}{v4}{Fore.RESET}){space * (21 - len(str(v4)))}{color}║
    {color}║  {c2}G3                 ({Fore.LIGHTGREEN_EX}{g3}{Fore.RESET}){space * (21 - len(str(g3)))}{color}║     ║  {c2}Kürek              ({Fore.LIGHTGREEN_EX}{v4}{Fore.RESET}){space * (21 - len(str(v4)))}{color}║
    {color}║  {c2}D3                 ({Fore.LIGHTGREEN_EX}{d3}{Fore.RESET}){space * (21 - len(str(g3)))}{color}║     ║  {c2}Balta              ({Fore.LIGHTGREEN_EX}{v4}{Fore.RESET}){space * (21 - len(str(v4)))}{color}║
    {color}╠════════════════════════════════════════════╣     ╠════════════════════════════════════════════╣
    Estimated reamining time: {Data.timer}{Fore.LIGHTBLUE_EX}s''')

def Banner(color=Fore.BLUE, c2=Fore.WHITE):
    return f"""{color} 
                                                 █████{c2}╗     {color} ██{c2}╗ {color}█████{c2}╗ {color}██{c2}╗  {color}██{c2}╗
                                                {color}██{c2}╔══{color}██{c2}╗     {color}██{c2}║{color}██{c2}╔══{color}██{c2}╗╚{color}██{c2}╗{color}██{c2}╔╝
                                                {color}███████{c2}║     {color}██{c2}║{color}███████{c2}║ ╚{color}███{c2}╔╝ 
                                                {color}██{c2}╔══{color}██{c2}║{color}██   ██{c2}║{color}██{c2}╔══{color}██{c2}║ {color}██{c2}╔{color}██{c2}╗ 
                                                {color}██{c2}║  {color}██{c2}║╚{color}█████{c2}╔╝{color}██{c2}║  {color}██{c2}║{color}██{c2}╔╝{color} ██{c2}╗
                                                {c2}╚═╝  ╚═╝ ╚════╝ ╚═╝  ╚═╝╚═╝  ╚═╝                             
                                                {Fore.LIGHTBLUE_EX}discord{c2}: {Fore.GREEN}xalperen    {Fore.LIGHTBLUE_EX}v{Fore.GREEN}{version}
            """