import customtkinter as ctk
import tkinter.messagebox as tkmb
from baseurlfile import base_url
import requests
import homeview
# Selecting GUI theme - dark, light , system (for system default)

  
# Selecting color theme - blue, green, dark-blue
# ctk.set_default_color_theme("blue")
  
app = ctk.CTk()
# ctk.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
with open("themevalue.txt","r") as readtheme:
    themeString=str(readtheme.read())
    ctk.set_appearance_mode(themeString)
ctk.set_default_color_theme("blue")
# app.geometry("1000x500")

# Get screen width and height
screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()

# Calculate the position for centering the window
x_position = (screen_width - 1000) // 2  # 1000 is the width of the window
y_position = (screen_height - 500) // 2  # 500 is the height of the window

app.geometry(f"1000x500+{x_position}+{y_position}")
app.title("Gpt Sender")

def open_home_dialog():
    # homeView=hvm.HomeViewWindow(self)
    # homeView.show()
    pass
def login():
    import loginview
    loginview.app.mainloop()
def send_signup_request():
    email = user_email_entry.get()
    password = user_pass.get()
    confirm_password_field=user_confirm_password.get()

    if password==confirm_password_field:


    
        data = {
            'email': email,
            'username': None,
            'first_name': None,
            'last_name': None,
            'password': user_pass,
            
        }
        from baseurlfile import base_url
        response = requests.post(f'{base_url}api/auth/register/', json=data)
        content = response.content.decode('utf-8')
        print(content)
        if response.status_code >= 200 and response.status_code <=204:
            response_data = response.json()
            registered_username = response_data['user']['email']
            request_id=response_data['user']['id']
            print(response_data)
            show_success_message(registered_username)
            with open('current_user_token.txt', 'w') as file:
                file.write(str(response.json().get('access')))
            with open('request_id.txt', 'w') as file:
                file.write(str(response_data['user']['id']))
            # with open('current_user_token.txt', 'r') as file:
            #     access_token=str(file.read())
            # with open('request_id.txt', 'r') as file:
            #     request_id=file.read()
            
            # headers = {
            #     'Authorization': f'Bearer {access_token}',
            #     'Content-Type': 'application/json',
            #     'User-ID': request_id  # Include the request ID in the headers
            # }
            import assignkey
            assignkey.assignOpenApiKey()

            print("successful")
            import loginview
            tkmb.showinfo(title="Login Successful",message="You have Registered Successfully")
            signin_window=loginview.app.mainloop
            

        else:
            show_error_message()

# def navigateToLoginPage(self):
#     from login import LoginMainForm
#     self.hide()
#     home_dialog = LoginMainForm(self)  # Instantiate the HomeDialog with the parent as self
#     home_dialog.show()  # Open the HomeDialog modally

def show_success_message(self, email):
    message = f"Your account has been created successfully.\nEmail: {email}"
    (self, "Registration Successful", message)
    tkmb.showinfo(title="Login Successful",message="You have Registered Successfully")
def show_error_message():
    tkmb.showinfo(title="Login Successful",message="You have Registered Successfully")

def show_password_error_message():
    tkmb.showinfo(title="Login Successful",message="You have Registered Successfully")
    
    
#     username = "Enter Username"
#     password = "Enter Password"
#     new_window = ctk.CTkToplevel(app)
  
#     new_window.title("Gpt sender")
  
#     new_window.geometry("350x150")
  
#     if user_entry.get() == username and user_pass.get() == password:
#         tkmb.showinfo(title="Login Successful",message="You have logged in Successfully")
#         ctk.CTkLabel(new_window,text="GeeksforGeeks is best for learning ANYTHING !!").pack()
#     elif user_entry.get() == username and user_pass.get() != password:
#         tkmb.showwarning(title='Wrong password',message='Please check your password')
#     elif user_entry.get() != username and user_pass.get() == password:
#         tkmb.showwarning(title='Wrong username',message='Please check your username')
#     else:
#         tkmb.showerror(title="Login Failed",message="Invalid Username and password")
  
  
  
label = ctk.CTkLabel(app,text="Gpt Sender")
  
label.pack(pady=20)
  
frame = ctk.CTkFrame(master=app)
frame.pack(pady=20,padx=40,fill='both',expand=True)
  
label = ctk.CTkLabel(master=frame,text='Register View')
label.pack(pady=12,padx=10)
  
user_email_entry= ctk.CTkEntry(master=frame,placeholder_text="Email",width=350)
user_email_entry.pack(pady=12,padx=10)
  
user_pass= ctk.CTkEntry(master=frame,placeholder_text="Password",show="*",width=350)
user_pass.pack(pady=12,padx=10)

user_confirm_password= ctk.CTkEntry(master=frame,placeholder_text="confirm password",width=350)
user_confirm_password.pack(pady=12,padx=10)
  

  
button = ctk.CTkButton(master=frame,text='Signup',command=send_signup_request)
button.pack(pady=12,padx=10)



button = ctk.CTkButton(master=frame,text='Already have account?',command=login)
button.pack(pady=12,padx=10)

  
checkbox = ctk.CTkCheckBox(master=frame,text='Remember Me')
checkbox.pack(pady=12,padx=10)


app.mainloop()
