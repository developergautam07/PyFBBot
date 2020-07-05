from pynput.keyboard import Key, Controller
import time

bot_keyboard = Controller()     # Creating a Keyboard Controller for bot
time.sleep(5)

# Uncomment all the line for finite times and replace True with count
#count = 3  

while True:  

	# Selecting posts
    bot_keyboard.press('j')
    bot_keyboard.release('j')

    # Commenting on posts
    bot_keyboard.press('c')
    bot_keyboard.release('c')

    bot_keyboard.type(':)')

    bot_keyboard.press(Key.enter)
    bot_keyboard.release(Key.enter)

    bot_keyboard.press(Key.tab)
    bot_keyboard.release(Key.tab)

    #count -= 1
    time.sleep(1)

