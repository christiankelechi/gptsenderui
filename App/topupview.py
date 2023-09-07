import tkinter
import customtkinter


class App(customtkinter.CTk):
    
    def topUpEndPoint(self):
            currency = self.currency_value.get()
            amount = self.amount_value.get()
            if amount=='':
                import tkinter.messagebox as tkmb
                tkmb.showinfo(title="Error Alert",message="Make sure to fill in the gap")
            else:
                amount=float(amount)
                import requests
                
                with open('request_id.txt', 'r') as file:
                    request_id = file.read()
                with open('current_user_token.txt', 'r') as file:
                    access_token = file.read()
                # with ope
                # access_token=""
                # check_token_response=requests.get("http://localhost:8000/api/checktoken/",headers=headers)
                # headers = {
                #     'Authorization': f'Bearer {check_token_response.json().get("access")}',
                #     'Content-Type': 'application/json',
                #     'User-ID':request_id  # Include the request ID in the headers
                #     }
                
                
                # if check_token_response.status_code==200:

                    
                    data = {
                        'currency': currency,
                        'amount': amount,
                    }
                    
                    headers = {
                    'Authorization': f'Bearer {access_token}',
                    'Content-Type': 'application/json',
                    'User-ID':request_id  # Include the request ID in the headers
                    }
                    from baseurlfile import base_url
                    top_up_response = requests.post(f'{base_url}api/usdtopup/', json=data,headers=headers)
                    response_json=top_up_response.json()
                    # request_email=response_json['user']['email']
                    print(response_json)
                    file=open(f"current_user_token.txt","r")
                    # top_up_response = requests.post(f'{base_url}/api/topupbtc/', json=data)

            

                if top_up_response.status_code == 200:
                    response_data = top_up_response.json()
                    print(response_data)
                    # print(response_data['total_amount'])
                    # from PyQt6.QtWidgets import QVBoxLayout
                    successful_msg = response_data.get('click_link_address')
                    import sys
                    import webbrowser
                    
                    successful_msg = successful_msg
                    import customtkinter as ctk
                    import tkinter.messagebox as tkmb
                    import webbrowser

                    

                    
                    webbrowser.open(successful_msg)

                else:
                    import tkinter.messagebox as tkmb
                    tkmb.showinfo(title="Error Alert",message="Fill in the blank space")


    def navigateToWallet(self):
        import wallet
        walletObj=wallet.App()
        walletObj.mainloop()
    def __init__(self):
        super().__init__()
        # customtkinter.set_appearance_mode("System")
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
        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame, command=self.sidebar_button_event,text='Home')
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)
        self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame, command=self.navigateToWallet,text='Wallet')
        self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)
        self.sidebar_button_3 = customtkinter.CTkButton(self.sidebar_frame, command=self.sidebar_button_event,text='Mails')
        self.sidebar_button_3.grid(row=3, column=0, padx=20, pady=10)
        self.sidebar_button_4 = customtkinter.CTkButton(self.sidebar_frame, command=self.sidebar_button_event,text='Send Mails')
        self.sidebar_button_4.grid(row=4, column=0, padx=20, pady=10)

        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"],command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["80%", "90%", "100%", "110%", "120%"],
                                                               command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))

        # Create a card frame for wallet information
        card_frame = customtkinter.CTkFrame(self, corner_radius=10, fg_color=["skyblue", "skyblue"])
        card_frame.grid(row=0, column=1, rowspan=2, padx=20, pady=20, sticky="nsew")

        wallet_label = customtkinter.CTkLabel(card_frame, text="Amount:($)", text_color='white', font=("serif", 22))
        wallet_label.grid(row=0, column=0, padx=(20, 10), pady=(20, 5), sticky="w")

        fund_label = customtkinter.CTkLabel(card_frame, text="Currency", text_color='white', font=("serif", 22))
        fund_label.grid(row=1, column=0, padx=(20, 10), pady=5, sticky="w")

        # unit_label = customtkinter.CTkLabel(card_frame, text="Available Unit:", font=("serif", 22), text_color='white')
        # unit_label.grid(row=2, column=0, padx=(20, 10), pady=5, sticky="w")

        self.amount_value = customtkinter.CTkEntry(card_frame,placeholder_text='eg 20,40 etc', width=200, text_color=['black','white'], font=("serif", 22))
        self.amount_value.grid(row=0, column=1, padx=10, pady=(20, 5), sticky="w")

        self.currency_value = customtkinter.CTkComboBox(card_frame, values=['USD'], width=200, text_color=['black','white'], font=("serif", 22))
        self.currency_value.grid(row=1, column=1, padx=10, pady=5, sticky="w")

        # unit_value = customtkinter.CTkLabel(card_frame, text="0", width=200, text_color='white', font=("serif", 22))
        # unit_value.grid(row=2, column=1, padx=10, pady=5, sticky="w")

        fund_button = customtkinter.CTkButton(card_frame, text="Fund Wallet", width=200, text_color='white', font=("serif", 22),command=self.topUpEndPoint)
        fund_button.grid(row=3, column=1, padx=(20, 10), pady=(20, 20), sticky="w")

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    def sidebar_button_event(self):
        print("sidebar_button click")

if __name__ == "__main__":
    app = App()
    app.mainloop()
