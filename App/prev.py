import tkinter as tk
import customtkinter
import customtkinter as ctk
from tkhtmlview import HTMLLabel

class HTMLPreviewApp(tk.Tk):
    def __init__(self):
        super().__init__()

        # Set up the tkinter window
        self.title("HTML Preview")
        self.geometry("800x600")

        # Create a Text widget for user input
        self.html_input = tk.Text(self, wrap=tk.WORD, height=10, width=50)
        self.html_input.pack(pady=(10, 0), padx=10, fill=tk.BOTH, expand=True)

        # Create a button to preview HTML
        self.preview_button = tk.Button(self, text="Preview", command=self.preview_html)
        self.preview_button.pack(pady=(5, 10))

        # Create a frame to hold the HTML preview
        self.preview_frame = tk.Frame(self)
        self.preview_frame.pack(fill=tk.BOTH, expand=True)

    def preview_html(self):
        # Get the HTML code from the Text widget
        html_code = self.html_input.get("1.0", tk.END)

        # Clear the previous HTML preview
        for widget in self.preview_frame.winfo_children():
            widget.destroy()

        # Create an HTMLLabel to display the HTML content
        html_label = HTMLLabel(self.preview_frame, html=html_code)
        html_label.pack(fill=tk.BOTH, expand=True)

if __name__ == "__main__":
    app = HTMLPreviewApp()
    app.mainloop()
