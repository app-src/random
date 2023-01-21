from pynput.keyboard import Key,Controller
from pynput import keyboard
import time

time.sleep(15)
word = """चूहा निकला बिल से
हैप्पी न्यू ईयर दिल से 👉👈"""
for i in range(500):
    keyboard.Controller().type(word)
    keyboard.Controller().press(Key.enter)
    keyboard.Controller().release(Key.enter)
