import tkinter
import customtkinter
import customtkinter as ctk
import asyncio
import requests

class App(customtkinter.CTk):
    async def makeAllWalletRequest(self):
    
        await asyncio.sleep(1)
        file_path = 'current_user_token.txt'
        
        with open(file_path, 'r') as file:
            access_token = str(file.read())
        file.close()
        with open('current_user_token.txt', 'r') as file:
            access_token = file.read()
        file.close()
        with open('request_id.txt', 'r') as file:
            request_id = file.read()
        file.close()
        # access_token=""
        
    
        headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json',
        'User-ID':request_id  # Include the request ID in the headers
        }
        import json
        from baseurlfile import base_url
        wallet_balance_response = requests.get(f'{base_url}api/usdtopup/',headers=headers)
        if wallet_balance_response.status_code==200:
            with open("cachefiles/wallet.json",'w') as walletWrite:
                # wallet_amount=walletWrite.write())

                wallet_amount=int(wallet_balance_response.json().get('amount'))
                wallet_id=str(wallet_balance_response.json().get('wallet_address'))
                unitofmails=float(wallet_amount/0.01)
                # walletWrite.write((unitofmails))
                wallet_data={'wallet_amount':wallet_amount,'wallet_id':wallet_id,'unit_of_mails':unitofmails}
                json.dump(wallet_data,walletWrite)
            # pass
            # await  self.ui.availablefund_label.setText()
            # await self.ui.wallet_address_label.setText()
            # unit_of_mails=
            # await self.ui.availableunit_label.setText)
        else:
            pass
    def openHomeView(self):
        
        import homeview
        homeObj=homeview.App()
        homeObj.mainloop()
    # def openTopUpView(self):
    #     import topupview
    #     topupObj=topupview.App()
    #     topupObj.mainloop()
    def __init__(self):
        super().__init__()
        with open("themevalue.txt","r") as readtheme:
            themeString=str(readtheme.read())
        ctk.set_appearance_mode(themeString)  # Modes: "System" (standard), "Dark", "Light"
        ctk.set_default_color_theme("blue")
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
        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame, command=self.openHomeView,text='Home')
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)
        self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame, command=self.sidebar_button_event,text='Wallet')
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
        card_frame.grid(row=0, column=1, rowspan=1, padx=20, pady=20, sticky="nsew")

        wallet_label = customtkinter.CTkLabel(card_frame, text="Wallet ID:", text_color='white', font=("serif", 22))
        wallet_label.grid(row=0, column=0, padx=(20, 10), pady=(20, 5), sticky="w")

        fund_label = customtkinter.CTkLabel(card_frame, text="Available Fund:", text_color='white', font=("serif", 22))
        fund_label.grid(row=1, column=0, padx=(20, 10), pady=5, sticky="w")

        unit_label = customtkinter.CTkLabel(card_frame, text="Available Unit:", font=("serif", 22), text_color='white')
        unit_label.grid(row=2, column=0, padx=(20, 10), pady=5, sticky="w")

        import json
        with open("cachefiles/wallet.json",'r') as walletFile:
            data=json.load(walletFile)
            # [{"wallet_amount": 3887, "wallet_id": "3809998921", "unit_of_mails": 388700.0}]
            walletid=data['wallet_id']
            wallet_amount=data['wallet_amount']
            units_of_mails=data['unit_of_mails']
          
        walletFile.close()

        self.wallet_value = customtkinter.CTkLabel(card_frame, text=str(walletid), width=200, text_color='white', font=("serif", 22))
        self.wallet_value.grid(row=0, column=1, padx=10, pady=(20, 5), sticky="w")

        self.fund_value = customtkinter.CTkLabel(card_frame, text=str(wallet_amount), width=200, text_color='white', font=("serif", 22))
        self.fund_value.grid(row=1, column=1, padx=10, pady=5, sticky="w")

        self.unit_value = customtkinter.CTkLabel(card_frame, text=str(units_of_mails), width=200, text_color='white', font=("serif", 22))
        self.unit_value.grid(row=2, column=1, padx=10, pady=5, sticky="w")

        fund_button = customtkinter.CTkButton(self, text="Fund Wallet", width=200, text_color='white', font=("serif", 22),command=self.navigateToFundView)
        fund_button.grid(row=3, column=1, padx=(20, 10), pady=(20, 20), sticky="w")

        loop = asyncio.get_event_loop()
        loop.run_until_complete(self.makeAllWalletRequest())
        # self.wallet_address_label.setText(str(walletid))
        # self.availablefund_label.setText(str(wallet_amount))
        # self.availableunit_label.setText(f'{units_of_mails}mails unit')
        
        

    def change_appearance_mode_event(self, new_appearance_mode: str):
        with open('themevalue.txt','w') as themefile:
            themefile.write(str(new_appearance_mode))
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    def sidebar_button_event(self):
        print("sidebar_button click")

    def navigateToFundView(self):
        import topupview
        fundviewObj=topupview.App()
        fundviewObj.mainloop()

if __name__ == "__main__":
    app = App()
    app.mainloop()
