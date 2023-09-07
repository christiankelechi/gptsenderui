import tkinter as tk
from tkinter import messagebox
import requests
import time

# Define the URL of your Django backend endpoint
BACKEND_URL = "http://your_backend_url/check-app-version/"

def check_app_version():
    try:
        response = requests.get(BACKEND_URL)
        data = response.json()
        message = data.get("message", "Failed to retrieve app version.")
        show_notification(message)
    except Exception as e:
        show_notification("Error: " + str(e))

def show_notification(message):
    notification_window = tk.Tk()
    notification_window.title("Notification")
    notification_window.geometry("300x100+900+500")  # Adjust the position as needed

    label = tk.Label(notification_window, text=message, padx=10, pady=10)
    label.pack()

    notification_window.after(60000, notification_window.destroy)  # Close notification after 5 seconds
    notification_window.mainloop()

# Create the main application window
root = tk.Tk()
root.title("App Version Checker")

# Create a button to check the app version
check_button = tk.Button(root, text="Check App Version", command=check_app_version)
check_button.pack(pady=20)

# Run the Tkinter main loop
root.mainloop()
