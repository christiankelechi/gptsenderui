import tkinter as tk
from tkinter import ttk
import threading
import time

class LoadingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Loading")
        
        # Calculate the screen width and height
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        
        # Calculate the position to center the window
        x_position = (screen_width - 200) // 2  # 200 is the desired width of the window
        y_position = (screen_height - 50) // 2  # 50 is the desired height of the window
        
        # Set the window geometry to center it on the screen
        self.root.geometry(f"200x50+{x_position}+{y_position}")
        
        # Create a progress bar
        self.progress_bar = ttk.Progressbar(self.root, length=200, mode="indeterminate")
        
        # Create Start and Stop buttons
        # self.start_button = tk.Button(self.root, text="Start Typing", command=self.start_typing_thread)
        # self.stop_button = tk.Button(self.root, text="Stop Typing", command=self.stop_typing_thread)
        
        # self.start_button.pack()
        # self.stop_button.pack()
        self.progress_bar.pack()
        
        self.typing_thread = None

    def type_text(self):
        text = "Hello, World! This is a sample text."
        for char in text:
            # text_output.insert(tk.END, char)
            # text_output.update()
            time.sleep(0.05)  # Adjust the typing speed here (in seconds)
    
    def start_loading_thread(self):
        self.progress_bar.start()
        self.loading_thread = threading.Thread(target=self.type_text)
        self.loading_thread.start()
    
    def stop_loading_thread(self):
        if self.loading_thread and self.loading_thread.is_alive():
            self.loading_thread.join()
        self.progress_bar.stop()

if __name__ == "__main__":
    root = tk.Tk()
    app = LoadingApp(root)
    
    app.start_loading_thread()
    # root.destroy()
    root.mainloop()
    # root.destroy()
