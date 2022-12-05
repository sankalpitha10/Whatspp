import random
import pyautogui as pg
import time

animal=('Donkey, Monkey, Cat')
time.sleep(8)

for i in range(5):
    a=random.choice(animal)
    pg.write('You are a '+a)
    pg.press('enter')
    