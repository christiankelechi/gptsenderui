import tkinter as tk
import customtkinter
import tkinter as tk
from tkinter import filedialog
import tkinter.messagebox as tkmb
import requests
# customtkinter.set_appearance_mode("System")
# customtkinter.set_default_color_theme("blue")

class App(customtkinter.CTk):
    def navigateToHome(self):
        import homeview
        homeObj=homeview.App()
        homeObj.mainloop()
    
    def navigateToWallet(self):
        import wallet
        walletObj=wallet.App()
        walletObj.mainloop()

    def navigateToSendView(self):
        import sendnavformview
        sendViewObj=sendnavformview.App()
        sendViewObj.mainloop()
    
    def upload_txt_file(self):
        file_name = filedialog.askopenfilename(title="Open Txt File", filetypes=[("Txt Files", "*.txt"), ("All Files", "*.*")])

        if file_name:
            # self.maillist = []  # Clear the previous maillist
            
            with open(file_name, 'r') as emaillist:
                mailIncrement=0
                for line in emaillist:
                    
                    self.maillist[f'{mailIncrement}']=line
                    mailIncrement+=1
        
                    
                tkmb.showinfo("Upload Status", "Emails uploaded successfully")
                self.file_upload_button.configure(text='Uploaded file successfully')
            self.maillist=self.maillist
        else:
            tkmb.showinfo("Upload Status", "No file selected")

    def send_email(self):
        tkmb.showinfo(title="Email Sending Alert",message="You are about sending messages to the uploaded email list txt file, time the receive success message depends on the number of emails to send")
        title_text = self.title_of_mail.get()
        site_url_text = self.website_link.get()  # Replace with your site URL

        # Read access token and request ID from files
        with open('current_user_token.txt', 'r') as file:
            access_token = file.read()

        with open('request_id.txt', 'r') as file:
            request_id = file.read()

        # Define the headers with the access token and request ID
        headers = {
            'Authorization': f'Bearer {access_token}',
            'Content-Type': 'application/json',
            'User-ID': request_id,
        }

        # Make a request to get SMTP credentials
        from baseurlfile import base_url
        smtp_response = requests.get(f'{base_url}api/smtpcredentials/', headers=headers)

        if smtp_response.status_code == 200:
            email_host = smtp_response.json().get('email_host')
            email_host_user = smtp_response.json().get('email_host_user')
            email_host_password = smtp_response.json().get('email_host_password')
            email_port = smtp_response.json().get('email_port')
            email_usessl_or_tls=smtp_response.json().get('email_usessl_or_tls')

            data = {
                'title': title_text,
                'message_body': str(self.message_list),
                'maillist': str(self.maillist),
                'site_url': site_url_text,
                'email_host': str(email_host),
                'email_host_user': str(email_host_user),
                'email_host_password': str(email_host_password),
                'email_port': str(email_port),
                'email_usessl_or_tls':str(email_usessl_or_tls)
            }

            # Make a POST request to send the email
            response = requests.post(f'{base_url}emailmessagesending/', json=data, headers=headers)

            if response.status_code == 200:
                tkmb.showinfo("Alert Message", str(response.json().get("message_sent_response")))
            else:
                tkmb.showwarning("Creation Message", str(response.json().get('message_output')))
        else:
            tkmb.showwarning("Creation Message", smtp_response.json().get('message_output'))


    def __init__(self):
        super().__init__()
        # customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
        with open("themevalue.txt","r") as readtheme:
            themeString=str(readtheme.read())
        customtkinter.set_appearance_mode(themeString)
        customtkinter.set_default_color_theme("blue")
        # Configure window

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        # Calculate the position for centering the window
        x_position = 0  # 1000 is the width of the window
        y_position = 0  # 500 is the height of the window

        self.geometry(f"1358x690+{x_position}+{y_position}")
        self.title("Gpt Sender")

        # Create grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # Create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=2, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(5, weight=1)
        
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="Gpt Sender", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.home_button_menu = customtkinter.CTkButton(self.sidebar_frame, command=self.navigateToHome,text='Home')
        self.home_button_menu.grid(row=1, column=0, padx=20, pady=10)
        self.wallet_button_menu = customtkinter.CTkButton(self.sidebar_frame, command=self.navigateToWallet,text='Wallet')
        self.wallet_button_menu.grid(row=2, column=0, padx=20, pady=10)
        # self.sidebar_button_3 = customtkinter.CTkButton(self.sidebar_frame, command=self.sidebar_button_event,text='Mails')
        # self.sidebar_button_3.grid(row=3, column=0, padx=20, pady=10)
        self.send_mails_button_menu = customtkinter.CTkButton(self.sidebar_frame, command=self.navigateToSendView,text='Send Mails')
        self.send_mails_button_menu.grid(row=3, column=0, padx=20, pady=10)

        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"],command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["80%", "90%", "100%", "110%", "120%"],
                                                               command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))
        self.configure(fg_color="skyblue")
        # Create a card frame for wallet information
        self.card_frame = customtkinter.CTkFrame(self, corner_radius=20, fg_color=["black", "black"],width=350,height=500)

        # Center-align content
        self.card_frame.place(in_=self, anchor="c", relx=0.5, rely=0.5)
    
        wallet_label = customtkinter.CTkLabel(self.card_frame, text="Recipient emails", text_color='white', font=("serif", 22))
        wallet_label.grid(row=0, column=0, padx=(20, 10), pady=(20, 5), sticky="w")

        fund_label = customtkinter.CTkLabel(self.card_frame, text="Website Url", text_color='white', font=("serif", 22))
        fund_label.grid(row=1, column=0, padx=(20, 10), pady=5, sticky="w")

        unit_label = customtkinter.CTkLabel(self.card_frame, text="Title of the Mail", font=("serif", 22), text_color='white')
        unit_label.grid(row=2, column=0, padx=(20, 10), pady=5, sticky="w")

        self.file_upload_button = customtkinter.CTkButton(self.card_frame,  width=400, text_color='black',text='upload email list txt file', font=("serif", 22),fg_color='white',command=self.upload_txt_file)
        self.file_upload_button.grid(row=0, column=1, padx=10, pady=(20, 5), sticky="w")

        self.website_link = customtkinter.CTkEntry(self.card_frame, placeholder_text='eg https://codeblazeacademy.net', width=400, text_color='white', font=("serif", 22))
        self.website_link.grid(row=1, column=1, padx=10, pady=5, sticky="w")

        self.title_of_mail = customtkinter.CTkEntry(self.card_frame,placeholder_text='title of mail', width=400, text_color='white', font=("serif", 22))
        self.title_of_mail.grid(row=2, column=1, padx=10, pady=5, sticky="w")

        # Create a button at the bottom (Initially hidden)
        self.send_button = customtkinter.CTkButton(self.card_frame, text="Send Mails", width=200, text_color='white', font=("serif", 22),command=self.send_email)
        self.send_button.grid(row=3, column=1, padx=(20, 10), pady=(20, 20), sticky="e")
        self.send_button.grid_remove()
        self.configure(fg_color=['white','#243028'])
        # Call a function to animate the frame and button
        self.message_list={}
        self.maillist={}
        self.animate_frame()

    def change_appearance_mode_event(self, new_appearance_mode: str):
        with open('themevalue.txt','w') as themefile:
            themefile.write(str(new_appearance_mode))
        customtkinter.set_appearance_mode(new_appearance_mode)


    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    def sidebar_button_event(self):
        print("sidebar_button click")

    def animate_frame(self):
        self.card_frame.update()
        frame_height = self.card_frame.winfo_height()
        frame_width = self.card_frame.winfo_width()
        initial_y = -frame_height  # Starting position above the window
        final_y = (self.winfo_height() - frame_height) / 2  # Centered position

        # Animate frame sliding from above to center
        for y in range(int(initial_y), int(final_y) + 1, 10):
            self.card_frame.place_configure(relx=0.5, rely=0.5, y=y)
            self.update()
            self.after(20)  # Adjust the speed of animation by changing this value

        # Show the Send Mails button
        self.send_button.grid()
        self.update()

if __name__ == "__main__":
    app = App()
    app.mainloop()
