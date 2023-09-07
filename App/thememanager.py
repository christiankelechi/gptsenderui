import customtkinter as ctk

# Initialize the current theme to 'dark'
current_theme = "dark"

def set_theme(theme):
    global current_theme
    current_theme = theme
    ctk.set_appearance_mode(theme)

def get_current_theme():
    return current_theme
