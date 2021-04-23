import pyautogui
import time
import random
import subprocess

subprocess.call("echo you have been hacked!  > texts.txt", shell=True)
time.sleep(2)

file = open('texts.txt' , 'r').read()
file = file.splitlines()

for _ in range(50):
	pyautogui.typewrite(random.choice(file))
	pyautogui.press('enter')
