from pynput.keyboard import Key, Controller

keyboard = Controller()

current_key = None


def control_game(gesture):

    global current_key


    if gesture == "ACCELERATE":

        if current_key != "right":

            if current_key == "left":
                keyboard.release(Key.left)

            keyboard.press(Key.right)
            current_key = "right"


    elif gesture == "BRAKE":

        if current_key != "left":

            if current_key == "right":
                keyboard.release(Key.right)

            keyboard.press(Key.left)
            current_key = "left"


    else:

        if current_key == "right":
            keyboard.release(Key.right)

        elif current_key == "left":
            keyboard.release(Key.left)

        current_key = None