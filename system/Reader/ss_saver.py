from PIL import ImageGrab

def scs(left, top, right, bottom, name):
    screenshot = ImageGrab.grab(bbox=(left, top, right, bottom))
    screenshot.save(fr"images\{name}.png")