import customtkinter as ctk
import tkinter.messagebox as tkmb
from baseurlfile import base_url
import requests
import homeview

# Create the main app window
app = ctk.CTk()

# Set the initial theme to 'dark'



# Define a function to change the theme
def change_theme(theme):
    global current_theme
    current_theme = theme
    with open('themevalue.txt','w') as themefile:
        themefile.write(str(current_theme))
    ctk.set_appearance_mode(theme)

# Get screen width and height
screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()

# Calculate the position for centering the window
x_position = (screen_width - 1000) // 2  # 1000 is the width of the window
y_position = (screen_height - 500) // 2  # 500 is the height of the window

app.geometry(f"1000x500+{x_position}+{y_position}")
app.title("Gpt Sender")

def open_home_dialog(self):
    # homeView=hvm.HomeViewWindow(self)
    # homeView.show()
    pass
  
def login():
    email = user_entry.get()
    password = user_pass.get()

    url = f'{base_url}api/auth/login/'
    data = {
        'email': email,
        'password': password
    }
    response = requests.post(url, json=data)

    if response.status_code == 200:
        response_json = response.json()
        print(response_json)
        request_email = response_json['user']['email']

        token = response.json().get('access')
        with open(f"current_user_token.txt", "w+") as file:
            file.write(token)

        data = {
            'token': token,
        }
        request_id = response_json['user']['id']
        headers = {
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json',
            'User-ID': request_id
        }
        with open('request_id.txt', 'w') as file:
            file.write(str(request_id))

        tkmb.showinfo(title="Login Successful", message="You have logged in Successfully")
        home_obj = homeview.App()
        home_obj.mainloop()
    else:
        # QtWidgets.QMessageBox.warning(self, "Login Failed", "Invalid email or password. Please try again.")
        pass

# Create a function to change the theme to 'light'
def set_light_theme():
    change_theme("light")

# Create a function to change the theme to 'dark'
def set_dark_theme():
    change_theme("dark")

# Create a function to change the theme to 'system'
def set_system_theme():
    change_theme("system")

label = ctk.CTkLabel(app, text="Gpt Sender")
label.pack(pady=20)

frame = ctk.CTkFrame(master=app)
frame.pack(pady=20, padx=40, fill='both', expand=True)

label = ctk.CTkLabel(master=frame, text='Login View')
label.pack(pady=12, padx=10)

user_entry = ctk.CTkEntry(master=frame, placeholder_text="Username", width=350)
user_entry.pack(pady=12, padx=10)

user_pass = ctk.CTkEntry(master=frame, placeholder_text="Password", show="*", width=350)
user_pass.pack(pady=12, padx=10)

button = ctk.CTkButton(master=frame, text='Login', command=login)
button.pack(pady=12, padx=10)

checkbox = ctk.CTkCheckBox(master=frame, text='Remember Me')
checkbox.pack(pady=12, padx=10)

# Add theme buttons
light_theme_button = ctk.CTkButton(master=frame, text='Light Theme', command=set_light_theme)
light_theme_button.pack(pady=6, padx=10)

dark_theme_button = ctk.CTkButton(master=frame, text='Dark Theme', command=set_dark_theme)
dark_theme_button.pack(pady=6, padx=10)

system_theme_button = ctk.CTkButton(master=frame, text='System Theme', command=set_system_theme)
system_theme_button.pack(pady=6, padx=10)

app.mainloop()
