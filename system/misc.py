from PIL import ImageGrab

def pixel(left, top, right, bottom, re, ge, be):
                                                # Belirtilen koordinatlar arasındaki ekran görüntüsünü al
    screenshot = ImageGrab.grab(bbox=(left, top, right, bottom))
    width, height = screenshot.size
                        # Fonksiyonu çağır ve metni göster
                        # Ekran görüntüsündeki her pikseli kontrol et
    for x in range(width):
        for y in range(height):
            r, g, b = screenshot.getpixel((x, y))
                        # Beyaz rengi kontrol et (#FFFFFF)
            if r == re and g == ge and b == be:
                        # Koordinatları global ekrana göre ayarla
                return (left + x, top + y)
    return None