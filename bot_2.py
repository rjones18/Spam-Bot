import pyautogui
import time
import random

time.sleep(2)

file = open('spam_texts.txt' , 'r').read()
file = file.splitlines()

for _ in range(50):
	pyautogui.typewrite(random.choice(file))
	pyautogui.press('enter')
	