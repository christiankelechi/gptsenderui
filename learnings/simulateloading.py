import tkinter as tk
from tkinter import ttk
import threading
import time

def type_text():
    text = "Hello, World! This is a sample text."
    for char in text:
        # text_output.insert(tk.END, char)
        # text_output.update()
        time.sleep(0.05)  # Adjust the typing speed here (in seconds)

def start_typing_thread():
    global typing_thread
    progress_bar.start()
    typing_thread = threading.Thread(target=type_text)
    typing_thread.start()

def stop_typing_thread():
    global typing_thread
    if typing_thread and typing_thread.is_alive():
        typing_thread.join()
    progress_bar.stop()

# Create the main tkinter window
root = tk.Tk()
root.title("Loading")


# Calculate the screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Calculate the position to center the window
x_position = (screen_width - 200) // 2  # 200 is the desired width of the window
y_position = (screen_height - 50) // 2  # 50 is the desired height of the window

# Set the window geometry to center it on the screen
root.geometry(f"200x50+{x_position}+{y_position}")

# Create a progress bar
progress_bar = ttk.Progressbar(root, length=200, mode="indeterminate")

# Create Start and Stop buttons
# start_button = tk.Button(root, text="Start Typing", command=start_typing_thread)
# stop_button = tk.Button(root, text="Stop Typing", command=stop_typing_thread)

# start_button.pack()
# stop_button.pack()
progress_bar.pack()
start_typing_thread()
root.mainloop()
