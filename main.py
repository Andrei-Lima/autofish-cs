## 
## Sorry for anyone who's using this
## Try setting lowering the gamma so it detects better
## this was also my first time using python so, again, sorry LOL
## 

import pyautogui
import keyboard
import time
from datetime import datetime

fish_amount = 0

with open("fish.txt", "r") as file:
  content = file.readline()
  fish_amount = int(content);

xx = 200
yy = 200
box = 10

color = [0, 0, 0]

txt = ""
yes = True

while yes:
  now = datetime.now()
  current_time = now.strftime("%H:%M:%S")

  xx, yy = pyautogui.position()
  y2 = yy+40

  for x in range(xx-box, xx+box):
    for y in range(y2-box, y2+box):
      if pyautogui.pixelMatchesColor(x, y, color):
        txt = "Fish Found! at "+str(current_time)+"\n"
        print(txt)
        
        with open("fish.txt", "w") as file:
          fish_amount += 1
          file.write(str(fish_amount))
          
        pyautogui.dragTo(xx, yy, 0.80)

  if keyboard.is_pressed('Q'):
    yes = False
    print("q")