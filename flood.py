import pyautogui
import time

time.sleep(10)

i = 1

def mesaj():
    pyautogui.write(str(i)+". Mesaj. ")
    pyautogui.press("enter")
    print(str(i)+" Mesaj gönderildi.")

while True:
    mesaj()
    i = i+1
    time.sleep(0)
    