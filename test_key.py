from pynput.keyboard import Key, Controller
import time

keyboard = Controller()

print("Click on the game window.")
print("Starting in 5 seconds...")

time.sleep(5)

print("Pressing RIGHT...")

keyboard.press(Key.right)
time.sleep(3)
keyboard.release(Key.right)

print("Done.")
