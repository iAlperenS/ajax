import pyautogui, datetime, threading, requests, time, colorama, json       
from system.data import *
from Logger import *
from colorama import Fore
from hacks.WordSender import set_cord
colorama.init()

# github.com/iAlperenS

def kitap():
            klasor = "images\\"
            webhook_url="webhook urlniz"; lic="Ajax"
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

            trash_x, trash_y = set_cord(606, 220)
            def take_screenshot_and_send():
                    """now_utc = datetime.datetime.utcnow()

                    now_utc_plus_3 = now_utc + datetime.timedelta(hours=3)

                    unix_zamani_utc_plus_3 = int(now_utc_plus_3.timestamp())
                    update_t = f"<t:{unix_zamani_utc_plus_3}:R>"
                    screenshot = pyautogui.screenshot()

                    temp_file_path = f'record.png'
                    screenshot.save(temp_file_path)

                    # Webhook
                    payload = {
                        'content': f'Last Record At: {update_t}',
                    }

                    # Ekran 
                    files = {'file': open(temp_file_path, 'rb')}

                    # Webhook
                    response = requests.post(webhook_url, data=payload, files=files)

                    if response.status_code == 200:
                        pass
                        # print('Record gönderildi.')
                    else:
                        pass
                        # print('Record gönderilemedi.')
                    time.sleep(60)
                    """
            #c = threading.Thread(target=take_screenshot_and_send)
            #c.start()
            kitapc = 0;ipeksi = 0;keskinlik = 0;derin = 0;koruma = 0;verim = 0;yumruk = 0;sonsuz = 0;kırıl = 0
            deger = 'Auto Enchant Kitap'
            start_time = time.time()
            zaman = (time.strftime("%d-%m-%Y %H:%M:%S"))
            zaman2 = zaman
            print(Fore.RED)
            time.sleep(5)
            """
            print('''AutoEnchant 5 Saniye İçinde Başlatılıor''')
            print('5..')
            time.sleep(1)
            print('4..')
            time.sleep(1)
            print('3..')
            time.sleep(1)
            print('2..')
            time.sleep(1)
            print('1..')
            time.sleep(1)
            print('Başlatıldı')
            """
            resim_klasoru = 'Res'
            while 1:
                    try:
                        embed = {
                            "title": "Auto Enchant Kitap",
                            "description": f"**Total Kullanılan Kitap**: {kitapc}\n\n**Kitaplar**;\n\nKırlmazlık: {kırıl}\nV4: {verim}\nYumruk2: {yumruk}\nSonsuzluk: {sonsuz}\nP4: {koruma}\nDerin3: {derin}\nİpeksi: {ipeksi}\nKes4: {keskinlik}",
                            "color": 255, # 16711680 Kırmızı  # Embed rengi (Decimal format)
                            "fields": [
                                {
                                    "name": "Username",
                                    "value": f"Private",
                                    "inline": True
                                },
                                {
                                    "name": "Key",
                                    "value": f"{lic}",
                                    "inline": True
                                },
                                        {
                                    "name": "Özellik",
                                    "value": f"Auto Enchant Kitap",
                                    "inline": True
                                }
                            ],
                            "footer": {
                                "text": "Ajaxs Login System"
                            }
                        }

                        # Embedi içeren mesaj oluştur
                        message = {
                            "content": "Cliente Bağlanıldı",
                            "embeds": [embed]
                        }

                        # JSON formatına çevir
                        json_message = json.dumps(message)

                        # Discord'a POST isteği gönder
                        headers = {
                            'Content-Type': 'application/json'
                        }
                        #x = open("C:\Ajaxs_Ware\custom.txt", "r")
                        otokitap = 1
                        #response = requests.post(webhook_url, data=json_message, headers=headers)
                        if otokitap == 1:
                            try:
                                baslangic_x = 470
                                baslangic_y = 340
                                son_x = 814
                                son_y = 518
                                image_location = pyautogui.locateOnScreen(f'{klasor}ttLapis.png', region=(baslangic_x, baslangic_y, son_x - baslangic_x, son_y - baslangic_y))
                                if image_location is not None:
                                    # Görüntü bulunduğunda yapılacak işlemler
                                    print("Lapis Eklendi")
                                    Log.write("Added Lapis")
                                    
                                    # Bulunan koordinata fareyi hareket ettir
                                    hedef_x = image_location.left + image_location.width / 2
                                    hedef_y = image_location.top + image_location.height / 2
                                    pyautogui.moveTo(hedef_x, hedef_y)
                                    pyautogui.keyDown('shift')
                                    pyautogui.click()
                                    pyautogui.keyUp('shift')
                            except:
                                pass

                            try:
                                if pyautogui.locateOnScreen(f'{klasor}lapis5.png', grayscale=True):
                                    pyautogui.moveTo(f'{klasor}ttLapis.png')
                                    Data.lapis += 1
                                    pyautogui.keyDown('shift')
                                    pyautogui.click()
                                    pyautogui.keyUp('shift')
                            except:
                                pass

                            try:
                                if pyautogui.locateOnScreen(f'{klasor}kitap.png', grayscale=True):
                                    Data.kitap += 1
                                    Log.write("Kitap Eklendi")
                                    pyautogui.moveTo(f'{klasor}kitap.png')
                                    pyautogui.keyDown('shift')
                                    pyautogui.click()
                                    pyautogui.keyUp('shift')
                            except:
                                pass

                            try:
                                pyautogui.moveTo(con1_x, con1_y)
                            except:
                                pass
                            time.sleep(0.1)
                            try:
                                if pyautogui.locateOnScreen(f'{klasor}verim4.png'):
                                    pyautogui.click()
                                    Data.ver4 += 1
                                    pyautogui.moveTo(con2_x, con2_y)
                                    pyautogui.keyDown('shift')
                                    pyautogui.click()
                                    pyautogui.keyUp('shift')
                                    Data.kitap += 1

                                    Data.lapis += 3
                                    verim += 1
                            except:
                                pass
                            time.sleep(0.01)
                            try:
                                if pyautogui.locateOnScreen(f'{klasor}keskinlik4.png', grayscale=True):
                                    pyautogui.click()
                                    Data.kes4 += 1
                                    pyautogui.moveTo(con2_x, con2_y)
                                    pyautogui.keyDown('shift')
                                    pyautogui.click()
                                    pyautogui.keyUp('shift')
                                    Data.kitap += 1
                                    Data.good += 1
                                    Data.lapis += 3
                                    keskinlik += 1
                                    time.sleep(0.1)
                            except:
                                pass
                            time.sleep(0.01)
                            try:
                                if pyautogui.locateOnScreen(f'{klasor}kirilmazlik.png', grayscale=True):
                                    pyautogui.click(f'{klasor}kirilmazlik.png')
                                    Data.kir3 += 1
                                    pyautogui.moveTo(con2_x, con2_y)
                                    pyautogui.keyDown('shift')
                                    pyautogui.click()
                                    pyautogui.keyUp('shift')
                                    Data.kitap += 1
                                    Data.good += 1
                                    Data.lapis += 3
                                    kırıl += 1
                            except:
                                pass
                            time.sleep(0.01)
                            try:
                                if pyautogui.locateOnScreen(f'{klasor}derinkos.png', grayscale=True):
                                    pyautogui.click(f'{klasor}derinkos.png')
                                    Data.der3 += 1
                                    pyautogui.moveTo(con2_x, con2_y)
                                    pyautogui.keyDown('shift')
                                    pyautogui.click()
                                    pyautogui.keyUp('shift')
                                    Data.kitap += 1
                                    Data.good += 1
                                    Data.lapis += 3
                                    derin += 1
                                    time.sleep(0.1)
                            except:
                                pass
                            time.sleep(0.01)
                            try:
                                if pyautogui.locateOnScreen(f'{klasor}ipeksidok.png', grayscale=True):
                                    pyautogui.click(f'{klasor}ipeksidok.png')
                                    Data.ipe1 += 1
                                    pyautogui.moveTo(con2_x, con2_y)
                                    pyautogui.keyDown('shift')
                                    pyautogui.click()
                                    pyautogui.keyUp('shift')
                                    Data.kitap += 1
                                    Data.good += 1
                                    Data.lapis += 3
                                    ipeksi += 1
                            except:
                                pass
                            time.sleep(0.01)
                            try:
                                if pyautogui.locateOnScreen(f'{klasor}sonsuzluk.png', grayscale=True):
                                    pyautogui.click(f'{klasor}sonsuzluk.png')
                                    Data.son1 += 1
                                    pyautogui.moveTo(con2_x, con2_y)
                                    pyautogui.keyDown('shift')
                                    pyautogui.click()
                                    pyautogui.keyUp('shift')
                                    Data.kitap += 1
                                    Data.good += 1
                                    Data.lapis += 3
                                    sonsuz += 1
                            except:
                                pass
                            time.sleep(0.1)
                            try:
                                if pyautogui.locateOnScreen(f'{klasor}yumruk.png'):
                                    pyautogui.click()
                                    Data.yum2 += 1
                                    pyautogui.moveTo(con2_x, con2_y)
                                    pyautogui.keyDown('shift')
                                    pyautogui.click()
                                    pyautogui.keyUp('shift')
                                    Data.kitap += 1
                                    Data.good += 1
                                    Data.lapis += 3
                                    yumruk += 1
                            except:
                                pass
                            time.sleep(0.01)
                            try:
                                if pyautogui.locateOnScreen(f'{klasor}p4.png', grayscale=True):
                                    pyautogui.click(f'{klasor}p4.png')
                                    Data.pro4 += 1
                                    pyautogui.moveTo(con2_x, con2_y)
                                    pyautogui.keyDown('shift')
                                    pyautogui.click()
                                    pyautogui.keyUp('shift')
                                    Data.kitap += 1
                                    Data.good += 1
                                    Data.lapis += 3
                                    koruma += 1
                            except:
                                pass

                            try:
                                if pyautogui.locateOnScreen(f'{klasor}1lvl2.png', grayscale=True):
                                    pyautogui.moveTo(trash_x, trash_y)
                                    pyautogui.click()
                                    pyautogui.click()

                                    pyautogui.moveTo(con2_x, con2_y)
                                    pyautogui.typewrite('q')
                                    Data.kitap += 1
                            except:
                                pass

                            try:
                                if pyautogui.locateOnScreen(f'{klasor}lapis64.PNG', grayscale=True):
                                    pass
                            except:
                                pass
                            Log.write(text="AutoEnchant Loop done!")
                    except Exception as f:
                        Log.write(f"An error accoured: {f}")

def oto_kitap():
    p = threading.Thread(target=kitap)
    p.start()
