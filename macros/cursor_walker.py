import pyautogui as p
import random as r

intensity = 1
x, y = 0, 0

while(True):
  x += r.randint(-intensity, intensity)
  y += r.randint(-intensity, intensity)
  print(x, y)
  p.moveRel(x, y)