import tkinter as tk
from tkinter import ttk
import time
from PIL import Image, ImageTk
# import homeview
import customtkinter as ctk

class GPTSenderApp(tk.Tk):
    def __init__(self):
        super().__init__()
        with open('themevalue.txt','w') as themefile:
            themefile.write("Dark")
        self.title("GPT Sender")
        with open("themevalue.txt","r") as readtheme:
            themeString=str(readtheme.read())
        ctk.set_appearance_mode(themeString)  # Modes: "System" (standard), "Dark", "Light"
        ctk.set_default_color_theme("blue")
        
        # Set the window icon
        icon = Image.open("gptsenderui/images/gptsenderlogo.png")
        icon = ImageTk.PhotoImage(icon)
        self.iconphoto(True, icon)

        self.center_window()
        self.configure(bg="dark blue")  # Set the window background color

        # Create a frame to center the progress bar with a blue background
        self.frame = tk.Frame(self,bg='dark blue')
        self.frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        # Load the logo image and resize it
        logo_image = Image.open("gptsenderui/images/gptsenderlogo.png")
        logo_image.thumbnail((200, 200), Image.AFFINE)  # Resize the logo to fit within 200x200 pixels
        logo_image = ImageTk.PhotoImage(logo_image)

        # Create a label for the app title with the resized logo and remove the border
        self.title_label = tk.Label(self.frame, image=logo_image, bg='dark blue', borderwidth=0, highlightthickness=0)
        self.title_label.image = logo_image  # Reference to prevent image garbage collection
        self.title_label.pack(pady=20)

        # Create a progress bar with a blue background
        self.progress_var = tk.DoubleVar()
        self.progress_bar = ttk.Progressbar(self.frame, variable=self.progress_var, length=300, mode="determinate", style="blue.Horizontal.TProgressbar")
        self.progress_bar.pack()

        # Style the progress bar to have a blue background
        style = ttk.Style()
        style.configure("blue.Horizontal.TProgressbar")

        # Start the loading asynchronously using the 'after' method
        self.after(100, self.simulate_loading)
        
    def center_window(self):
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x_position = (screen_width - 1000) // 2  # 1000 is the width of the window
        y_position = (screen_height - 500) // 2  # 500 is the height of the window
        self.geometry(f"1000x500+{x_position}+{y_position}")

    def simulate_loading(self):
        for i in range(101):
            self.progress_var.set(i)  # Update the progress bar value
            self.update_idletasks()
            time.sleep(0.1)
        
        # Destroy the loading screen
        self.destroy()
        
        import homeview

        # Create the home view
        home_frame = homeview.App()

        # Use the 'after' method to show the home view after a brief delay
        self.after(100, lambda: home_frame.deiconify())

        # Create the login view
        import loginview

        # Show the login view on top of the home view
        login_frame = loginview.app
        login_frame._set_appearance_mode("Light")
        login_frame.withdraw()

if __name__ == "__main__":
    app = GPTSenderApp()
    app.mainloop()
