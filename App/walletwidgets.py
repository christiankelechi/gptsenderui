import customtkinter
import asyncio
import requests
class WalletFrame(customtkinter.CTkFrame):
    # def navigateToTopup(self):
    #     self.withdraw()
    #     import topupview
    #     topUpObj=topupview.App()
    #     topUpObj.mainloop()

    # def generate_email_template(self):
    #     # async def run_tasks():
    #     import asyncio
    #     loop = asyncio.get_event_loop()
    #     loop.run_until_complete(self.makeRequestToOpenAi())
    
    # def navigateToSendNav(self):
    #     import sendnavformview
    #     sendNavObj=sendnavformview.App()
    #     sendNavObj.mainloop()

    # def open_input_dialog_event(self):
    #     dialog = customtkinter.CTkInputDialog(text="Type in a number:", title="CTkInputDialog")
    #     print("CTkInputDialog:", dialog.get_input())

    # def change_appearance_mode_event(self, new_appearance_mode: str):
    #     with open('themevalue.txt','w') as themefile:
    #         themefile.write(str(new_appearance_mode))
    #     customtkinter.set_appearance_mode(new_appearance_mode)

    # def change_scaling_event(self, new_scaling: str):
    #     new_scaling_float = int(new_scaling.replace("%", "")) / 100
    #     customtkinter.set_widget_scaling(new_scaling_float)

    # def sidebar_button_event(self):
    #     print("sidebar_button click")
    def __init__(self, parent):
        super().__init__(parent)
        self.card_frame = customtkinter.CTkFrame(self, corner_radius=10, fg_color=["#243028", "#243028"])
        self.card_frame.grid(row=0, column=1, rowspan=1, padx=20, pady=20, sticky="nsew")
        
        wallet_label = customtkinter.CTkLabel(self.card_frame, text="Wallet ID:", text_color='white', font=("serif", 22))
        wallet_label.grid(row=0, column=0, padx=(20, 10), pady=(20, 5), sticky="w")

        fund_label = customtkinter.CTkLabel(self.card_frame, text="Available Fund:($)", text_color='white', font=("serif", 22))
        fund_label.grid(row=1, column=0, padx=(20, 10), pady=5, sticky="w")

        unit_label = customtkinter.CTkLabel(self.card_frame, text="Available Unit:", font=("serif", 22), text_color='white')
        unit_label.grid(row=2, column=0, padx=(20, 10), pady=5, sticky="w")
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self.makeAllWalletRequest())
        import json
        with open("cachefiles/wallet.json",'r') as walletFile:
            data=json.load(walletFile)
            # [{"wallet_amount": 3887, "wallet_id": "3809998921", "unit_of_mails": 388700.0}]
            walletid=data['wallet_id']
            wallet_amount=data['wallet_amount']
            units_of_mails=data['unit_of_mails']
          
        walletFile.close()

        self.wallet_value = customtkinter.CTkLabel(self.card_frame, text=str(walletid), width=200, text_color='white', font=("serif", 22))
        self.wallet_value.grid(row=0, column=1, padx=10, pady=(20, 5), sticky="w")

        self.fund_value = customtkinter.CTkLabel(self.card_frame, text=str(wallet_amount), width=200, text_color='white', font=("serif", 22))
        self.fund_value.grid(row=1, column=1, padx=10, pady=5, sticky="w")

        self.unit_value = customtkinter.CTkLabel(self.card_frame, text=str(units_of_mails), width=200, text_color='white', font=("serif", 22))
        self.unit_value.grid(row=2, column=1, padx=10, pady=5, sticky="w")

        fund_button = customtkinter.CTkButton(self.card_frame, text="Fund Wallet", width=200, text_color='white', font=("serif", 22),command=self.navigateToTopup)
        fund_button.grid(row=3, column=1, padx=(20, 10), pady=(20, 20), sticky="w")

        self.topup_btn = customtkinter.CTkButton(self.sidebar_frame, command=self.navigateToTopup,text='Topup Wallet')
        self.topup_btn.grid(row=4, column=0, padx=20, pady=10)

        self.card_frame.grid_forget()

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
    def navigateToTopup(self):
        # import topupview
        # topUpObj=topupview.App()
        # topUpObj.mainloop()
        self.grid()