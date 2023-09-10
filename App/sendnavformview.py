import tkinter
import customtkinter
import requests
import tkinter.messagebox as tkmb

class App(customtkinter.CTk):
    def navigateToWallet(self):
        import wallet
        walletObj=wallet.App()
        walletObj.mainloop()
    
    def navigateToHome(self):
        import homeview
        homeObj=homeview.App()
        homeObj.mainloop()

    def navigateToSendNav(self):
        import sendnavformview
        sendNavObj=sendnavformview.App()
        sendNavObj.mainloop()

    def __init__(self):
        super().__init__()
        # customtkinter.set_appearance_mode("System")
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
        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame, command=self.navigateToHome,text='Home')
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)
        self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame, command=self.navigateToWallet,text='Wallet')
        self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)
        # self.sidebar_button_3 = customtkinter.CTkButton(self.sidebar_frame, command=self.sidebar_button_event,text='Mails')
        # self.sidebar_button_3.grid(row=3, column=0, padx=20, pady=10)
        self.sidebar_button_4 = customtkinter.CTkButton(self.sidebar_frame, command=self.navigateToSendNav,text='Send Mails')
        self.sidebar_button_4.grid(row=3, column=0, padx=20, pady=10)

        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"],command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["80%", "90%", "100%", "110%", "120%"],
                                                               command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))

        # Create a card frame for wallet information
        card_frame = customtkinter.CTkFrame(self, corner_radius=10, fg_color=["skyblue", "skyblue"])
        card_frame.grid(row=0, column=1, rowspan=2, padx=20, pady=20, sticky="nsew")

        self.email_host = customtkinter.CTkLabel(card_frame, text="Email_Host", text_color=['white','black'], font=("serif", 22))
        self.email_host.grid(row=0, column=0, padx=(20, 10), pady=(20, 5), sticky="w")

        self.email_host_user = customtkinter.CTkLabel(card_frame, text="Email_Host_User", text_color=['white','black'], font=("serif", 22))
        self.email_host_user.grid(row=1, column=0, padx=(20, 10), pady=5, sticky="w")

        self.host_password_label = customtkinter.CTkLabel(card_frame, text="Email_Host_Password", text_color=['white','black'], font=("serif", 22))
        self.host_password_label.grid(row=2, column=0, padx=(20, 40), pady=5, sticky="w")

        self.email_port_label = customtkinter.CTkLabel(card_frame, text="Email_Port", text_color=['white','black'], font=("serif", 22))
        self.email_port_label.grid(row=3, column=0, padx=(20, 40), pady=5, sticky="w")

        self.email_ssl_label = customtkinter.CTkLabel(card_frame, text="SSL/TLS", text_color=['white','black'], font=("serif", 22))
        self.email_ssl_label.grid(row=4, column=0, padx=(20, 40), pady=5, sticky="w")

        # self.email_tls_label = customtkinter.CTkLabel(card_frame, text="Use_TLS", text_color=['white','black'], font=("serif", 22))
        # self.email_tls_label.grid(row=5, column=0, padx=(20, 40), pady=5, sticky="w")
        # unit_label = customtkinter.CTkLabel(card_frame, text="Available Unit:", font=("serif", 22), text_color='white')
        # unit_label.grid(row=2, column=0, padx=(20, 10), pady=5, sticky="w")

        

        # fund_value = customtkinter.CTkComboBox(card_frame, values=['USD'], width=200, text_color='black', font=("serif", 22))
        # fund_value.grid(row=1, column=1, padx=10, pady=5, sticky="w")

        # unit_value = customtkinter.CTkLabel(card_frame, text="0", width=200, text_color='white', font=("serif", 22))
        # unit_value.grid(row=2, column=1, padx=10, pady=5, sticky="w")

        self.savebutton = customtkinter.CTkButton(card_frame, text="Save", width=200, text_color='white', font=("serif", 22),command=self.navigatetoMainSendView)
        self.savebutton.grid(row=6, column=0, padx=(20, 10), pady=(20, 20), sticky="w")
        tokenpath = 'current_user_token.txt'
        
        with open(tokenpath, 'r') as file:
            access_token = str(file.read())
        
        with open('current_user_token.txt', 'r') as file:
            access_token = file.read()

        with open('request_id.txt', 'r') as file:
            request_id = file.read()
        # with ope
        # access_token=""
        
    
        headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json',
        'User-ID':request_id  # Include the request ID in the headers
        }
    
        from baseurlfile import base_url
        smtp_response=requests.get(f'{base_url}api/smtpcredentials/',headers=headers)
        if smtp_response.status_code==200:
            # 'email_host','email_host_user','email_host_password','email_port'
            email_host=smtp_response.json().get('email_host')
            email_host_user=smtp_response.json().get('email_host_user')
            email_host_password=smtp_response.json().get('email_host_password')
            email_port=smtp_response.json().get('email_port')

            if email_host==None  or email_host_user==None or email_host_password==None or email_port==None:
                self.emailhostfield = customtkinter.CTkEntry(card_frame,placeholder_text='eg mail.supressedman.com', width=400, text_color=['black','white'], font=("serif", 22))
                self.emailhostfield.insert(0,"None")
                self.emailhostfield.grid(row=0, column=1, padx=10, pady=(20, 5), sticky="w")

                self.emailhostuserfield = customtkinter.CTkEntry(card_frame,placeholder_text='eg support@supressedman.com', width=400, text_color=['black','white'], font=("serif", 22))
                self.emailhostuserfield.insert(0,"None")
                self.emailhostuserfield.grid(row=1, column=1, padx=10, pady=(20, 5), sticky="w")

                self.emailpasswordfield = customtkinter.CTkEntry(card_frame,placeholder_text='eg Sup1234!', width=400, text_color=['black','white'], font=("serif", 22))
                self.emailpasswordfield.insert(0,"None")
                self.emailpasswordfield.grid(row=2, column=1, padx=10, pady=(20, 5), sticky="w")

                self.emailportfield = customtkinter.CTkEntry(card_frame,placeholder_text='eg 420', width=400, text_color=['black','white'], font=("serif", 22))
                self.emailportfield.insert(0,"None")
                self.emailportfield.grid(row=3, column=1, padx=10, pady=(20, 5), sticky="w")

                self.sslfield = customtkinter.CTkComboBox(card_frame,values=['SSL','TLS'],width=400, text_color=['black','white'], font=("serif", 22))
                self.sslfield.grid(row=4, column=1, padx=10, pady=(20, 5), sticky="w")

                # self.tlsfield = customtkinter.CTkComboBox(card_frame,values=['SSL','TLS'], width=400, text_color=['black','white'], font=("serif", 22))
                # self.tlsfield.grid(row=5, column=1, padx=10, pady=(20, 5), sticky="w")
            else:
                
                self.emailhostfield = customtkinter.CTkEntry(card_frame,placeholder_text='eg mail.supressedman.com', width=400, text_color=['black','white'], font=("serif", 22))
                self.emailhostfield.insert(0,email_host)
                self.emailhostfield.grid(row=0, column=1, padx=10, pady=(20, 5), sticky="w")

                self.emailhostuserfield = customtkinter.CTkEntry(card_frame,placeholder_text='eg support@supressedman.com', width=400, text_color=['black','white'], font=("serif", 22))
                self.emailhostuserfield.insert(0,email_host_user)
                self.emailhostuserfield.grid(row=1, column=1, padx=10, pady=(20, 5), sticky="w")

                self.emailpasswordfield = customtkinter.CTkEntry(card_frame,placeholder_text='eg Sup1234!', width=400, text_color=['black','white'], font=("serif", 22),show="*")
                self.emailpasswordfield.insert(0,email_host_password)
                self.emailpasswordfield.grid(row=2, column=1, padx=10, pady=(20, 5), sticky="w")

                self.emailportfield = customtkinter.CTkEntry(card_frame,placeholder_text='eg 420', width=400, text_color=['black','white'], font=("serif", 22))
                self.emailportfield.insert(0,email_port)
                self.emailportfield.grid(row=3, column=1, padx=10, pady=(20, 5), sticky="w")

                self.sslfield = customtkinter.CTkComboBox(card_frame,values=['SSL','TLS'],width=400, text_color=['black','white'], font=("serif", 22))
                self.sslfield.grid(row=4, column=1, padx=10, pady=(20, 5), sticky="w")

                # self.tlsfield = customtkinter.CTkComboBox(card_frame,values=['False','True'], width=400, text_color=['black','white'], font=("serif", 22))
                # self.tlsfield.grid(row=5, column=1, padx=10, pady=(20, 5), sticky="w")
            # self.send_mail_ui.email_host_edit.setText(email_host)
            # self.send_mail_ui.email_host_user_edit.setText(email_host_user)
            # self.send_mail_ui.email_port_edit.setText(email_port)
            # self.send_mail_ui.emal_host_password_edit.setText(email_host_password)
        
    def navigatetoMainSendView(self):
        # 'email_host','email_host_user','email_host_password','email_port'
        
        with open('current_user_token.txt', 'r') as file:
            access_token = file.read()

        with open('request_id.txt', 'r') as file:
            request_id = file.read()
        # with ope
        # access_token=""
        data = {
            'email_host': self.emailhostfield.get(),
            'email_host_user': self.emailhostuserfield.get(),
            'email_host_password':self.emailpasswordfield.get(),
            'email_port':self.emailportfield.get(),
            'email_usessl_or_tls':self.sslfield.get()
            # 'swapped_emails':None
        }
        if (self.emailhostfield.get()=='') or (self.emailhostuserfield.get()=='') or (self.emailpasswordfield.get()=='') or (self.emailportfield.get()=='') or (self.sslfield.get()==''):
            # from PyQt6.QtWidgets import QMessageBox
            tkmb.showinfo(title='Credential alert',message="You need to fill in the form")
        else:
            headers = {
            'Authorization': f'Bearer {access_token}',
            'Content-Type': 'application/json',
            'User-ID':request_id  # Include the request ID in the headers
            }

            
            from baseurlfile import base_url
            response = requests.post(f'{base_url}api/smtpcredentials/', json=data,headers=headers)
            if response.status_code==200:
                
                tkmb.showinfo(title='Credential alert',message=str(response.json().get('user_credentials_outcome')))
                import mainsendview
                mainSendObj=mainsendview.App()
                mainSendObj.mainloop()
            else:
                pass
                
            
    def change_appearance_mode_event(self, new_appearance_mode: str):
        with open('themevalue.txt','w') as themefile:
            themefile.write(str(new_appearance_mode))
        customtkinter.set_appearance_mode(new_appearance_mode)
        

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    def sidebar_button_event(self):
        print("sidebar_button click")

if __name__ == "__main__":
    app = App()
    app.mainloop()
