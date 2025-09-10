import ctypes
import time
from playsound import playsound

def DetectClick(button, watchtime=5):
    if button in (1, '1', 'l', 'L', 'left', 'Left', 'LEFT'):
        bnum = 0x01
    elif button in (2, '2', 'r', 'R', 'right', 'Right', 'RIGHT'):
        bnum = 0x02
    else:
        raise ValueError("Unknown button")

    start = time.time()
    while time.time() - start < watchtime:
        if ctypes.windll.user32.GetKeyState(bnum) < 0:  # pressed
            return True
        time.sleep(0.001)
    return False

while True:
    if DetectClick(1):
        playsound('C:\\Users\\samda\\Desktop\\sound\\scout_specialcompleted03.wav')
        # wait for release to avoid multiple plays
        while ctypes.windll.user32.GetKeyState(0x01) < 0:
            time.sleep(0.01)