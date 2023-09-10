import customtkinter as ctk
import tkinter.messagebox as tkmb
from baseurlfile import base_url
import requests
import homeview
RESET_URL = "http://localhost:8000/api/password_reset/"
CHANGE_URL = "http://localhost:8000/api/password_reset/confirm/"
# Create the main app window
app = ctk.CTk()
with open('themevalue.txt','r') as themefile:
    theme=themefile.read()
ctk.set_appearance_mode(str(theme))
# Set the initial theme to 'dark'
# def forget_password():
#     pass

def already_have_account():
    import loginview
    loginview.app 

def dont_have_account():
    import registerview
    registerview.app

def reset_password():
    import json
    username = user_entry.get()
    with open('current_user_token.txt', 'r') as file:
        access_token = file.read()

    with open('request_id.txt', 'r') as file:
        request_id = file.read()
    # with ope
    # access_token=""
    with open("emailgenerationdetails.json","r") as generationFile:
        data_loaded=json.load(generationFile)
    
    headers = {
    'Authorization': f'Bearer {access_token}',
    'Content-Type': 'application/json',
    'User-ID':request_id  # Include the request ID in the headers
    }
    data = {
        "email": username
        }
    response = requests.post(RESET_URL, json=data,headers=headers)
    print(response)
    if response.status_code == 200:
        tkmb.showinfo("Success", "Password reset email sent.")
    else:
        tkmb.showerror("Error", "Password reset failed.")

def change_password():
    new_password = user_pass.get()
    confirm_password = user_pass.get()
    
    if new_password != confirm_password:
        tkmb.showerror("Error", "Passwords do not match.")
        return
    
    token = input("Enter the password reset token sent to your email: ")
    
    data = {
        "token": token,
        "password": new_password,
    }
    
    response = requests.post(CHANGE_URL, data=data)
    
    if response.status_code == 200:
        tkmb.showinfo("Success", "Password changed successfully.")
    else:
        tkmb.showerror("Error", "Password change failed.")

# Define a function to change the theme
def change_theme(theme):
    # global current_theme
    # current_theme = theme
    pass
    

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
        content = response.content.decode('utf-8')
        print(content)
        tkmb.showinfo(title='Error message',message=str(content))

# Create a function to change the theme to 'light'
def set_light_theme():
    change_theme("light")

# Create a function to change the theme to 'dark'
def set_dark_theme():
    change_theme("dark")

# Create a function to change the theme to 'system'
def set_system_theme():
    change_theme("system")
label = ctk.CTkLabel(app, text="Gpt Sender", font=("Helvetica", 24))
label.pack(pady=20)

frame = ctk.CTkFrame(master=app)
frame.pack(pady=20, padx=40, fill='both', expand=True)

label = ctk.CTkLabel(master=frame, text='Login', font=("Helvetica", 18))
label.pack(pady=12, padx=10)

user_entry = ctk.CTkEntry(master=frame, placeholder_text="Username", width=350)
user_entry.pack(pady=12, padx=10)

user_pass = ctk.CTkEntry(master=frame, placeholder_text="Password", show="*", width=350)
user_pass.pack(pady=12, padx=10)

button = ctk.CTkButton(master=frame, text='Login', command=login, bg_color='green', fg_color='black', font=("Helvetica", 14))
button.pack(pady=12, padx=10)

checkbox = ctk.CTkCheckBox(master=frame, text='Remember Me')
checkbox.pack(pady=12, padx=10)

# Add "Forgot Password" and "Already have an account?" buttons
forgot_password_button = ctk.CTkButton(master=frame, text='Forgot Password', command=reset_password, font=("Helvetica", 12))
forgot_password_button.pack(pady=6, padx=10)

change_password_button = ctk.CTkButton(master=frame, text='Change Password?', command=change_password, font=("Helvetica", 12))
change_password_button.pack(pady=6, padx=10)

already_have_account_button = ctk.CTkButton(master=frame, text='Don\'t have an account yet?', command=dont_have_account, font=("Helvetica", 12))
already_have_account_button.pack(pady=6, padx=10)
# Add a UI scale label
ui_scale_label = ctk.CTkLabel(master=frame, text='UI Scale', font=("Helvetica", 14))
ui_scale_label.pack(pady=6, padx=10)
app.mainloop()