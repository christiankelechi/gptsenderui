import tkinter
import customtkinter
import customtkinter as ctk
import asyncio
import requests

import tkinter as tk
import customtkinter  # Make sure you import your customtkinter module
import tkinter as tk
from tkinter import ttk
import threading
import time

class LoadingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Loading")
        
        # Calculate the screen width and height
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        
        # Calculate the position to center the window
        x_position = (screen_width - 200) // 2  # 200 is the desired width of the window
        y_position = (screen_height - 50) // 2  # 50 is the desired height of the window
        
        # Set the window geometry to center it on the screen
        self.root.geometry(f"200x50+{x_position}+{y_position}")
        
        # Create a progress bar
        self.progress_bar = ttk.Progressbar(self.root, length=200, mode="indeterminate")
        
        # Create Start and Stop buttons
        # self.start_button = tk.Button(self.root, text="Start Typing", command=self.start_typing_thread)
        # self.stop_button = tk.Button(self.root, text="Stop Typing", command=self.stop_typing_thread)
        
        # self.start_button.pack()
        # self.stop_button.pack()
        self.progress_bar.pack()
        
        self.typing_thread = None

    def type_text(self):
        text = "Hello, World! This is a sample text."
        for char in text:
            # text_output.insert(tk.END, char)
            # text_output.update()
            time.sleep(0.05)  # Adjust the typing speed here (in seconds)
    
    def start_loading_thread(self):
        self.progress_bar.start()
        self.loading_thread = threading.Thread(target=self.type_text)
        self.loading_thread.start()
    
    def stop_loading_thread(self):
        if self.loading_thread and self.loading_thread.is_alive():
            self.loading_thread.join()
        self.progress_bar.stop()

# if __name__ == "__main__":
#     root = tk.Tk()
#     app = LoadingApp(root)
    
#     app.start_loading_thread()
#     # root.destroy()
#     root.mainloop()
    # root.destroy()

class HomeFrame(customtkinter.CTkFrame):
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
        
        self.columnconfigure(0, weight=1)  # Make sure the column expands with the window

        # Create and place the widgets in the frame
        prompt_list = ['follow_up', 'software sales', 'promote your business', 'register prompt', 'share prompt']
        
        self.prompt_combo = customtkinter.CTkComboBox(self, values=prompt_list, width=100, height=50)
        self.prompt_combo.grid(row=6, column=0, padx=(20, 5), pady=(20, 5), sticky="nsew")

        self.generatemailbutton = customtkinter.CTkButton(self, fg_color="transparent", border_width=1,
                                                          text_color=("gray10", "#DCE4EE"), text="generate", width=90,
                                                          command=self.generate_email_template)
        self.generatemailbutton.grid(row=6, column=1, sticky="nsew", pady=(10, 10), padx=(10, 10))

        self.textbox = customtkinter.CTkTextbox(self, width=100, height=300)
        self.textbox.grid(row=1, column=0, padx=(0, 40), pady=(0, 40), sticky="nsew")

        self.checkbox_slider_frame = customtkinter.CTkFrame(self)
        self.checkbox_slider_frame.grid(row=2, column=0, padx=(20, 20), pady=(20, 0), sticky="nsew")

        self.checkbox_1 = customtkinter.CTkLabel(master=self.checkbox_slider_frame, text='No of mails')
        self.checkbox_1.grid(row=0, column=0, pady=(20, 0), padx=20, sticky="n")

        self.numberofmessages = customtkinter.CTkEntry(master=self.checkbox_slider_frame, width=200,
                                                       placeholder_text='eg 20')
        self.numberofmessages.grid(row=0, column=1, pady=(20, 0), padx=20, sticky="n")

        self.companies_email_label = customtkinter.CTkLabel(master=self.checkbox_slider_frame, text='Companies Email')
        self.companies_email_label.grid(row=1, column=0, pady=(20, 0), padx=20, sticky="n")

        self.companies_email = customtkinter.CTkEntry(master=self.checkbox_slider_frame, width=200,
                                                      placeholder_text='kezechristian@gmail.com')
        self.companies_email.grid(row=1, column=1, pady=(20, 0), padx=20, sticky="n")

        self.companies_site_label = customtkinter.CTkLabel(master=self.checkbox_slider_frame, text='Companies Site')
        self.companies_site_label.grid(row=2, column=0, pady=(20, 0), padx=20, sticky="n")

        self.companies_site = customtkinter.CTkEntry(master=self.checkbox_slider_frame, width=200,
                                                      placeholder_text='www.codeblazeacademy.net')
        self.companies_site.grid(row=2, column=1, pady=(20, 0), padx=20, sticky="n")

        # Make sure rows expand with the frame
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)

    def loadprogress_thread(self):
        # if __name__ == "__main__":
        self.root_app = tk.Tk()
        self.app_root = LoadingApp(self.root)
        
        self.app_root.start_loading_thread()
        # root.destroy()
        self.root_app.mainloop()

        
    def stoploadprogress_thread(self):
        self.root_app.destroy()

    def makeRequestToOpenAi(self):
        tkmb.showinfo(title="Message prompt alert",message="You are about to generate unique emails according to your preference, generation will not take more than 1minute from range of 1-1000 messages")

        # self.start_loading_animation() 
        self.prompt=self.prompt_combo.get()
        self.number_of_messages=self.numberofmessages.get()
        self.email_keywords_list=['follow_up'+f'replace the generated chat gpt content response with {self.companies_email.get()} for the companies emails and also {self.companies_site.get()} for the companies website any where necessary','top_up'+f'replace the generated chat gpt content response with {self.companies_email.get()} for the companies emails and also {self.companies_site.get()} for the companies website any where necessary','advert'+f'replace the generated chat gpt content response with {self.companies_email.get()} for the companies emails and also {self.companies_site.get()} for the companies website any where necessary','register'+f'replace the generated chat gpt content response with {self.companies_email.get()} for the companies emails and also {self.companies_site.get()} for the companies website any where necessary']
        file_path = 'current_user_token.txt'
        with open("emailgenerationdetails.json","w") as generationFile:
            data={'number_of_messages':str(self.number_of_messages),'prompt':self.prompt}
            import json
            json.dump(data,generationFile)

        with open(file_path, 'r') as file:
            access_token = str(file.read())
        
        with open('current_user_token.txt', 'r') as file:
            access_token = file.read()

        with open('request_id.txt', 'r') as file:
            request_id = file.read()
        # with ope
        # access_token=""
        with open("emailgenerationdetails.json","r") as generationFile:
            data_loaded=json.load(generationFile)
        data = {
            'number_of_mail': str(data_loaded['number_of_messages']),
            'prompt': str(data_loaded['prompt']),
            'access_token':str(access_token),
            'site_url':str(self.companies_site.get()),
            'email_address':str(self.companies_email.get())
            # 'generated_emails':None,
            # 'swapped_emails':None
        }
        
        headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json',
        'User-ID':request_id  # Include the request ID in the headers
        }

        
        if (self.companies_site.get()=='') or (self.companies_email.get()==''):
            # from PyQt6.QtWidgets import QMessageBox
           
          
            tkmb.showwarning(title="Form Error",message="Try to fill in all fields ")
           
            
        else:
            
            import requests
            from baseurlfile import base_url
            response = requests.post(f'{base_url}email-generator/', json=data,headers=headers)
            
            # current_number_of_messages.append(self.number_of_messages)
            data_loaded['response']=response
            increment_send=0
            if int(self.number_of_messages)>0:

                import os
                
                import requests

                # Load the .env file
                
                file_path = 'current_user_token.txt'
                
                with open(file_path, 'r') as file:
                    access_token = str(file.read())
                # Make the API request and retrieve the OpenAI key
                url = f'{base_url}api/openaiusers/'
                headers = {
                    'Authorization': f'Bearer {str(access_token)}',
                    'Content-Type': 'application/json'
                }

                response = requests.get(url, headers=headers)
            
                data = response.json()
                openai_key = data.get('open_ai_key')
                content = response.content.decode('utf-8')
                print(content)
                
                import openai
                openai_key=str(openai_key)
                print(str(openai_key))
                from allprompts import business_promotion_prompt,follow_up_prompt,software_sales_prompt,register_prompt,share_promt
                business_promotion_prompt=business_promotion_prompt
                follow_up_prompt=follow_up_prompt
                software_sales_prompt=software_sales_prompt
                register_prompt=register_prompt
                share_promt=share_promt
                
                # self.register_up_promt=['action message to tell user to register with a particular link']

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
                file_path = 'current_user_token.txt'
                with open("emailgenerationdetails.json","w") as generationFile:
                    data={'number_of_messages':str(self.number_of_messages),'prompt':self.prompt}
                    import json
                    json.dump(data,generationFile)

                with open(file_path, 'r') as file:
                    access_token = str(file.read())
                
                with open('current_user_token.txt', 'r') as file:
                    access_token = file.read()

                with open('request_id.txt', 'r') as file:
                    request_id = file.read()
                # with ope
                # access_token=""
                with open("emailgenerationdetails.json","r") as generationFile:
                    data_loaded=json.load(generationFile)
                data = {
                    'number_of_mail': str(data_loaded['number_of_messages']),
                    'prompt': str(data_loaded['prompt']),
                    'access_token':str(access_token),
                    'site_url':str(self.companies_site.get()),
                    'email_address':str(self.companies_email.get())
                    # 'generated_emails':None,
                    # 'swapped_emails':None
                }
                
                headers = {
                'Authorization': f'Bearer {access_token}',
                'Content-Type': 'application/json',
                'User-ID':request_id  # Include the request ID in the headers
                }

                
                if (self.companies_site.get()=='') or (self.companies_email.get()==''):
                    # from PyQt6.QtWidgets import QMessageBox
                
                
                    tkmb.showwarning(title="Form Error",message="Try to fill in all fields ")
                
                
                else:
                    import json
                    from baseurlfile import base_url
                    wallet_balance_response = requests.get(f'{base_url}api/usdtopup/',headers=headers)

                    if wallet_balance_response.json().get('amount')<10:
                        tkmb.showwarning(title='Wallet balance alert',message="Top up at least 10USD to make use of the application")
                    
                    else:
                        
                        if str(self.prompt)=='follow_up'.lower():
                            responses_dict = {}
                            email_swapped_json={}
                            follow_up_prompt=random.choice(follow_up_prompt)
                            follow_up_prompt=follow_up_prompt+f'replace the generated chat gpt content response with {self.companies_email.get()} for the companies emails and also {self.companies_site.get()} for the companies website any where necessary'
                            swapped_list=[]
                            import os
                            import openai
                            import json
                            def create_response(n):
                                
                                api_url = "https://api.openai.com/v1/engines/text-davinci-003/completions"

    
                                
                                params = {
                                    "prompt": str(follow_up_prompt),
                                    "temperature": 1,
                                    "max_tokens": 45,
                                    "top_p": 1,
                                    "n": n,
                                    "frequency_penalty": 2.0,
                                    "presence_penalty": 2.0,
                                }

                                # Headers with API key
                                headers = {
                                    "Content-Type": "application/json",
                                    "Authorization": f"Bearer {openai_key}",
                                }

                                # Make the API request
                                response = requests.post(api_url, json=params, headers=headers)
                                return [choice['text'] for choice in response.json()['choices']]

                            def main():
                            
            # time.sleep(1)
                                total_iterations = int(self.number_of_messages)  # Change this number to the desired maximum generation
                                increment = 100

                                
                                import appdirs
                                from pathlib import Path

                                # Get the appropriate directory for application-specific data
                                app_data_dir = appdirs.user_data_dir()

                                file_name = "emails.json"
                                file_path = Path(app_data_dir) / file_name
                        

                                total_iterations = int(self.number_of_messages) # 
                                increment = 100
                                
                                
                                responses_dict = {}
                                for n in range(1, total_iterations + 1, increment):
                                    current_increment = min(increment, total_iterations - n + 1)
                                    response_list = create_response(current_increment)
                                    for i, response in enumerate(response_list):
                                        responses_dict[str(n + i)] = response
                                with open(file_path, 'w') as file:
                                    json.dump(responses_dict, file)
                            responses_dict=responses_dict
                                
                            
                            main()
                            import appdirs
                            from pathlib import Path

                            # Get the appropriate directory for application-specific data
                            app_data_dir = appdirs.user_data_dir()

                            file_name = "emails.json"
                            file_path = Path(app_data_dir) / file_name
                        
                            with open(file_path,'r') as readmailfile:
                                data_loaded=json.load(readmailfile)
                            
                            import json

                            def swap_characters(text):
                                # Create a translation table to swap characters
                                translation_table = str.maketrans('aeiou', 'zcpmk')
                                return text.translate(translation_table)

                            def process_json(data):
                                processed_data = {}

                                for key, value in data.items():
                                    if isinstance(value, str):
                                        value = value.lower()  # Convert value to lowercase
                                        swapped_value = swap_characters(value)
                                        processed_data[key] = swapped_value
                                    else:
                                        processed_data[key] = value

                                return processed_data

                            def main():
                                
                                processed_json = process_json(data_loaded)
                            
                            # Create the file path
                                import appdirs
                                from pathlib import Path

                                # Get the appropriate directory for application-specific data
                                app_data_dir = appdirs.user_data_dir()

                                file_name = "swappedemails.json"
                                file_path = Path(app_data_dir) / file_name
                                
                                # Write the formatted data to the file
                                with open(file_path, 'w') as file:
                                    json.dump(processed_json, file, indent=4)
                                
                            
                            main()

                            
                            context={'unique_email_text':data_loaded}
                            self.textbox.insert('0.00',str(context['unique_email_text']))
                        if str(self.prompt)=='software sales'.lower():
                            responses_dict = {}
                            email_swapped_json={}
                            software_sales_prompt=random.choice(software_sales_prompt)
                            software_sales_prompt=software_sales_prompt+f'replace the generated chat gpt content response with {self.companies_email.get()} for the companies emails and also {self.companies_site.get()} for the companies website any where necessary'
                            swapped_list=[]
                            import os
                            import openai
                            import json
                            def create_response(n):
                                api_url = "https://api.openai.com/v1/engines/text-davinci-003/completions"

        # Define your prompt
                                
                                params = {
                                    "prompt": str(software_sales_prompt),
                                    "temperature": 1,
                                    "max_tokens": 45,
                                    "top_p": 1,
                                    "n": n,
                                    "frequency_penalty": 2.0,
                                    "presence_penalty": 2.0,
                                }

                                # Headers with API key
                                headers = {
                                    "Content-Type": "application/json",
                                    "Authorization": f"Bearer {openai_key}",
                                }

                                # Make the API request
                                response = requests.post(api_url, json=params, headers=headers)
                                return [choice['text'] for choice in response.json()['choices']]

                            def main():
                            
            # time.sleep(1)
                                total_iterations = int(self.number_of_messages)  # Change this number to the desired maximum generation
                                increment = 100

                                
                                import appdirs
                                from pathlib import Path

                                # Get the appropriate directory for application-specific data
                                app_data_dir = appdirs.user_data_dir()

                                file_name = "emails.json"
                                file_path = Path(app_data_dir) / file_name
                                

                                total_iterations = int(self.number_of_messages) # 
                                increment = 100
                                
                                
                                responses_dict = {}
                                for n in range(1, total_iterations + 1, increment):
                                    current_increment = min(increment, total_iterations - n + 1)
                                    response_list = create_response(current_increment)
                                    for i, response in enumerate(response_list):
                                        responses_dict[str(n + i)] = response
                                with open(file_path, 'w') as file:
                                    json.dump(responses_dict, file)
                            responses_dict=responses_dict
                                
                            
                            main()
                            import appdirs
                            from pathlib import Path

                            # Get the appropriate directory for application-specific data
                            app_data_dir = appdirs.user_data_dir()

                            file_name = "emails.json"
                            file_path = Path(app_data_dir) / file_name
                            
                            with open(file_path,'r') as readmailfile:
                                data_loaded=json.load(readmailfile)
                            
                            import json

                            def swap_characters(text):
                                # Create a translation table to swap characters
                                translation_table = str.maketrans('aeiou', 'zcpmk')
                                return text.translate(translation_table)

                            def process_json(data):
                                processed_data = {}

                                for key, value in data.items():
                                    if isinstance(value, str):
                                        value = value.lower()  # Convert value to lowercase
                                        swapped_value = swap_characters(value)
                                        processed_data[key] = swapped_value
                                    else:
                                        processed_data[key] = value

                                return processed_data

                            def main():
                                
                                processed_json = process_json(data_loaded)
                                import appdirs
                                from pathlib import Path

                                # Get the appropriate directory for application-specific data
                                app_data_dir = appdirs.user_data_dir()

                                file_name = "swappedemails.json"
                                file_path = Path(app_data_dir) / file_name
                                
                            # Create the file path
                                # file_path = downloads_dir / "swappedemails.json"
                                
                                # Write the formatted data to the file
                                with open(file_path, 'w') as file:
                                    json.dump(processed_json, file, indent=4)
                                
                            
                            main()

                            
                            context={'unique_email_text':data_loaded}
                            self.textbox.insert('0.00',str(context['unique_email_text']))
                        
                        if str(self.prompt)=='promote your business'.lower():
                            responses_dict = {}
                            email_swapped_json={}
                            business_promotion_prompt=random.choice(business_promotion_prompt)
                            business_promotion_prompt=business_promotion_prompt+f'replace the generated chat gpt content response with {self.companies_email.get()} for the companies emails and also {self.companies_site.get()} for the companies website any where necessary'
                            swapped_list=[]
                            import os
                            import openai
                            import json
                            def create_response(n):
                                api_url = "https://api.openai.com/v1/engines/text-davinci-003/completions"

        # Define your prompt
                                
                                params = {
                                    "prompt": str(business_promotion_prompt),
                                    "temperature": 1,
                                    "max_tokens": 45,
                                    "top_p": 1,
                                    "n": n,
                                    "frequency_penalty": 2.0,
                                    "presence_penalty": 2.0,
                                }

                                # Headers with API key
                                headers = {
                                    "Content-Type": "application/json",
                                    "Authorization": f"Bearer {openai_key}",
                                }

                                # Make the API request
                                response = requests.post(api_url, json=params, headers=headers)
                                return [choice['text'] for choice in response.json()['choices']]

                            def main():
                            
            # time.sleep(1)
                                total_iterations = int(self.number_of_messages)  # Change this number to the desired maximum generation
                                increment = 100

                                
                                import appdirs
                                from pathlib import Path

                                # Get the appropriate directory for application-specific data
                                app_data_dir = appdirs.user_data_dir()

                                file_name = "emails.json"
                                file_path = Path(app_data_dir) / file_name
                                

                                total_iterations = int(self.number_of_messages) # 
                                increment = 100
                                
                                
                                responses_dict = {}
                                for n in range(1, total_iterations + 1, increment):
                                    current_increment = min(increment, total_iterations - n + 1)
                                    response_list = create_response(current_increment)
                                    for i, response in enumerate(response_list):
                                        responses_dict[str(n + i)] = response
                                with open(file_path, 'w') as file:
                                    json.dump(responses_dict, file)
                            responses_dict=responses_dict
                                
                            
                            main()
                            import appdirs
                            from pathlib import Path

                            # Get the appropriate directory for application-specific data
                            app_data_dir = appdirs.user_data_dir()

                            file_name = "emails.json"
                            file_path = Path(app_data_dir) / file_name
                                
                            with open(file_path,'r') as readmailfile:
                                data_loaded=json.load(readmailfile)
                            
                            import json

                            def swap_characters(text):
                                # Create a translation table to swap characters
                                translation_table = str.maketrans('aeiou', 'zcpmk')
                                return text.translate(translation_table)

                            def process_json(data):
                                processed_data = {}

                                for key, value in data.items():
                                    if isinstance(value, str):
                                        value = value.lower()  # Convert value to lowercase
                                        swapped_value = swap_characters(value)
                                        processed_data[key] = swapped_value
                                    else:
                                        processed_data[key] = value

                                return processed_data

                            def main():
                                
                                processed_json = process_json(data_loaded)
                            
                            # Create the file path
                                headers = {
                                'Authorization': f'Bearer {access_token}',
                                'Content-Type': 'application/json',
                                'User-ID':request_id  # Include the request ID in the headers
                                }
                                import json
                                from baseurlfile import base_url
                                wallet_balance_response = requests.get(f'{base_url}api/usdtopup/',headers=headers)
                                import appdirs
                                from pathlib import Path

                                # Get the appropriate directory for application-specific data
                                app_data_dir = appdirs.user_data_dir()

                                file_name = "swappedemails.json"
                                file_path = Path(app_data_dir) / file_name
                        
                                # file_path = downloads_dir / "swappedemails.json"
                                # current_user=UsdModel.objects.get(user=user)
                                
                                # Write the formatted data to the file
                                with open(file_path, 'w') as file:
                                    json.dump(processed_json, file, indent=4)
                                
                            
                            main()

                            
                            context={'unique_email_text':data_loaded}
                            self.textbox.insert('0.00',str(context['unique_email_text']))
                        
                        if str(self.prompt)=='register prompt'.lower():
                            responses_dict = {}
                            email_swapped_json={}
                            register_prompt=random.choice(register_prompt)
                            register_prompt=register_prompt+f'replace the generated chat gpt content response with {self.companies_email.get()} for the companies emails and also {self.companies_site.get()} for the companies website any where necessary'
                            swapped_list=[]
                            import os
                            import openai
                            import json
                            def create_response(n):
                                api_url = "https://api.openai.com/v1/engines/text-davinci-003/completions"

        # Define your prompt
                                
                                params = {
                                    "prompt": str(register_prompt),
                                    "temperature": 1,
                                    "max_tokens": 45,
                                    "top_p": 1,
                                    "n": n,
                                    "frequency_penalty": 2.0,
                                    "presence_penalty": 2.0,
                                }

                                # Headers with API key
                                headers = {
                                    "Content-Type": "application/json",
                                    "Authorization": f"Bearer {openai_key}",
                                }

                                # Make the API request
                                response = requests.post(api_url, json=params, headers=headers)
                                return [choice['text'] for choice in response.json()['choices']]

                            def main():
                            
            # time.sleep(1)
                                total_iterations = int(self.number_of_messages)  # Change this number to the desired maximum generation
                                increment = 100

                                
                                import appdirs
                                from pathlib import Path

                                # Get the appropriate directory for application-specific data
                                app_data_dir = appdirs.user_data_dir()

                                file_name = "emails.json"
                                file_path = Path(app_data_dir) / file_name
                        
                                

                                total_iterations = int(self.number_of_messages) # 
                                increment = 100
                                
                                
                                responses_dict = {}
                                for n in range(1, total_iterations + 1, increment):
                                    current_increment = min(increment, total_iterations - n + 1)
                                    response_list = create_response(current_increment)
                                    for i, response in enumerate(response_list):
                                        responses_dict[str(n + i)] = response
                                with open(file_path, 'w') as file:
                                    json.dump(responses_dict, file)
                            responses_dict=responses_dict
                                
                            
                            main()
                            import appdirs
                            from pathlib import Path

                            # Get the appropriate directory for application-specific data
                            app_data_dir = appdirs.user_data_dir()

                            file_name = "emails.json"
                            file_path = Path(app_data_dir) / file_name
                        
                            with open(file_path,'r') as readmailfile:
                                data_loaded=json.load(readmailfile)
                            
                            import json

                            def swap_characters(text):
                                # Create a translation table to swap characters
                                translation_table = str.maketrans('aeiou', 'zcpmk')
                                return text.translate(translation_table)

                            def process_json(data):
                                processed_data = {}

                                for key, value in data.items():
                                    if isinstance(value, str):
                                        value = value.lower()  # Convert value to lowercase
                                        swapped_value = swap_characters(value)
                                        processed_data[key] = swapped_value
                                    else:
                                        processed_data[key] = value

                                return processed_data

                            def main():
                                
                                processed_json = process_json(data_loaded)
                                import appdirs
                                from pathlib import Path

                                # Get the appropriate directory for application-specific data
                                app_data_dir = appdirs.user_data_dir()

                                file_name = "swappedemails.json"
                                file_path = Path(app_data_dir) / file_name
                                
                            # Create the file path
                                # file_path = downloads_dir / "swappedemails.json"
                                
                                # Write the formatted data to the file
                                with open(file_path, 'w') as file:
                                    json.dump(processed_json, file, indent=4)
                                
                            
                            main()

                            
                            context={'unique_email_text':data_loaded}
                            self.textbox.insert('0.00',str(context['unique_email_text']))
                        
                        if str(self.prompt)=='share prompt'.lower():
                            responses_dict = {}
                            email_swapped_json={}
                            share_promt=random.choice(share_promt)
                            share_promt=share_promt+f'replace the generated chat gpt content response with {self.companies_email.get()} for the companies emails and also {self.companies_site.get()} for the companies website any where necessary'
                            swapped_list=[]
                            import os
                            import openai
                            import json
                            def create_response(n):
                                api_url = "https://api.openai.com/v1/engines/text-davinci-003/completions"

        # Define your prompt
                                
                                params = {
                                    "prompt": str(share_promt),
                                    "temperature": 1,
                                    "max_tokens": 45,
                                    "top_p": 1,
                                    "n": n,
                                    "frequency_penalty": 2.0,
                                    "presence_penalty": 2.0,
                                }

                                # Headers with API key
                                headers = {
                                    "Content-Type": "application/json",
                                    "Authorization": f"Bearer {openai_key}",
                                }

                                # Make the API request
                                response = requests.post(api_url, json=params, headers=headers)
                                return [choice['text'] for choice in response.json()['choices']]

                            def main():
                            
            # time.sleep(1)
                                total_iterations = int(self.number_of_messages)  # Change this number to the desired maximum generation
                                increment = 100

                                
                                import appdirs
                                from pathlib import Path

                                # Get the appropriate directory for application-specific data
                                app_data_dir = appdirs.user_data_dir()

                                file_name = "emails.json"
                                file_path = Path(app_data_dir) / file_name
                        
                                total_iterations = int(self.number_of_messages) # 
                                increment = 100
                                
                                responses_dict = {}
                                for n in range(1, total_iterations + 1, increment):
                                    current_increment = min(increment, total_iterations - n + 1)
                                    response_list = create_response(current_increment)
                                    for i, response in enumerate(response_list):
                                        responses_dict[str(n + i)] = response
                                with open(file_path, 'w') as file:
                                    json.dump(responses_dict, file)
                            responses_dict=responses_dict
                                
                            
                            main()
                            import appdirs
                            from pathlib import Path

                            # Get the appropriate directory for application-specific data
                            app_data_dir = appdirs.user_data_dir()

                            file_name = "emails.json"
                            file_path = Path(app_data_dir) / file_name
                        
                            with open(file_path,'r') as readmailfile:
                                data_loaded=json.load(readmailfile)
                            
                            import json

                            def swap_characters(text):
                                # Create a translation table to swap characters
                                translation_table = str.maketrans('aeiou', 'zcpmk')
                                return text.translate(translation_table)

                            def process_json(data):
                                processed_data = {}

                                for key, value in data.items():
                                    if isinstance(value, str):
                                        value = value.lower()  # Convert value to lowercase
                                        swapped_value = swap_characters(value)
                                        processed_data[key] = swapped_value
                                    else:
                                        processed_data[key] = value

                                return processed_data

                            def main():
                                
                                processed_json = process_json(data_loaded)
                            
                            # Create the file path
                                import appdirs
                                from pathlib import Path

                                # Get the appropriate directory for application-specific data
                                app_data_dir = appdirs.user_data_dir()

                                file_name = "swappedemails.json"
                                file_path = Path(app_data_dir) / file_name
                        
                                
                                # Write the formatted data to the file
                                with open(file_path, 'w') as file:
                                    json.dump(processed_json, file, indent=4)
                                
                            
                            main()

                            
                            context={'unique_email_text':data_loaded}
                            self.textbox.insert('0.00',str(context['unique_email_text']))
                        
                        
                
            
                
                

        
       
            
            if response.status_code==200:
                
                # data_loaded=str(response.json().get('unique_email_text'))
                # self.email_terminal.setText(str(data_loaded))
                self.track_state=0
              
                # from PyQt6.QtGui import QMovie
                # self.tract_loading=0
               
            elif response.status_code==302:
                
                
            
                tkmb.showwarning(title="Warning ",message="Request not successfull, verify if you have signed up or entered the number of emails")
                # self.loading_label.setVisible(False)
                # self.tract_loading=0
                
            else:

                
                tkmb.showwarning(title="Warning ",message="Request not successfull, verify if you have signed up or entered the number of emails you want to enterhave enough balance in your wallet")
                

    
        
    # def generate_email_template(self):
    #     # async def run_tasks():
    #     # import asyncio
    #     # loop = asyncio.get_event_loop()
    #     import threading
    #     global generateemail_thread
    #     generateemail_thread=threading.Thread(target=self.makeRequestToOpenAi)
    #     # loop.run_until_complete(self.makeRequestToOpenAi())
    #     generateemail_thread.start()

    def startload_thread(self):
        import threading
        global start_thread
        # progress_bar.sart()
        start_thread = threading.Thread(target=self.loadprogress_thread)
        start_thread.start()
        

    # def start_load_thread(self):
    #     import simulateloading as sl

    #     # if __name__ == "__main__":
    #     self.root = tk.Tk()
    #     self.app = sl.LoadingApp(self.root)

    #     self.app.start_loading_thread()
    #     self.root.mainloop()
    #     import threading
    #     global load_thread
    # #   progress_bar.start()
    #     load_thread = threading.Thread(target=self.loadthreadview)
    #     load_thread.start()
    def stopload_thread(self):
        import threading
        global stop_thread
        # progress_bar.sart()
        stop_thread = threading.Thread(target=self.stoploadprogress_thread)
        stop_thread.start()
        
    def generate_email_template(self):
        # self.startload_thread()
        # async def run_tasks():
        # import asyncio
        # loop = asyncio.get_event_loop()
        # self.startload_thread()
        import threading
        global generateemail_thread
        generateemail_thread=threading.Thread(target=self.makeRequestToOpenAi)
        # loop.run_until_complete(self.makeRequestToOpenAi())
        generateemail_thread.start()

        # self.stopload_thread()
        # self.stopload_thread()
import tkinter
import tkinter.messagebox
import customtkinter
import tkinter.messagebox as tkmb
import thememanager
import random
import webbrowser
from plyer import notification  
  # Themes: "blue" (standard), "green", "dark-blue"
from pathlib import Path
app_running=True
    
def check_app_version():
    with open("cachefiles/version.txt","r") as versionfile:
        current_version=float(str(versionfile.read()))
    version_data = {
    'current_version':current_version
    # 'generated_emails':None,
    # 'swapped_emails':None
    }

    # headers = {
    # 'Authorization': f'Bearer {access_token}',
    # 'Content-Type': 'application/json',
    # 'User-ID':request_id  # Include the request ID in the headers
    # }

    from baseurlfile import base_url
    # while app_running==True:

    try:
        import requests
        response = requests.post(f"{base_url}api/check_version/",json=version_data)
        data = response.json()
        message = data.get("app_update_response")
        # pip install plyer  
        
        
        notification_title = 'Software Update Needed'  
        # notification_message = 'Thank you for reading. Have a Good Day.'  
        
        notification.notify(  
            title = notification_title,  
            message = message,  
            app_icon = None,  
            timeout = 10000,  
            toast = True  
            )  
        # webbrowser.open("www.codeblazeacademy.net")
    except Exception as e:
        pass
        # self.show_notification("Error: " + str(e))
    import time
    # time.sleep(60)
class App(customtkinter.CTk):
    

        
    

    def show_notification(self,message):
        import tkinter as tk
        notification_window = tk.Tk()
        notification_window.title("Notification")
        notification_window.geometry("300x100+900+500")  # Adjust the position as needed

        label = tk.Label(notification_window, text=message, padx=10, pady=10)
        label.pack()

        notification_window.after(60000, notification_window.destroy)  # Close notification after 5 seconds
        # notification_window.mainloop()

    # Create the main application window
    # root = tk.Tk()
    # root.title("App Version Checker")

    # Create a button to check the app version
    
    

        # Run the Tkinter main loop


class App(customtkinter.CTk):
    def navigateToHome(self):
        import homeview
        homeObj=homeview.App()
        homeObj.mainloop()
    
    # def navigateToWallet(self):
    #     import wallet
    #     walletObj=wallet.App()
    #     walletObj.mainloop()

    def navigateToSendMail(self):
        # import sendnavformview
        # sendMailsViewObj=sendnavformview.App()
        # sendMailsViewObj.mainloop()
        self.card_frame.grid_remove()
        self.topupframe.grid_remove()
        self.mainsend_frame.place_forget()
        self.sendnavform_frame.grid()


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
        self.home_button_menu = customtkinter.CTkButton(self.sidebar_frame, command=self.navigateToHome,text='Home')
        self.home_button_menu.grid(row=1, column=0, padx=20, pady=10)
        self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame, command=self.navigateToWallet,text='Wallet')
        self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)
        # self.sidebar_button_3 = customtkinter.CTkButton(self.sidebar_frame, command=self.sidebar_button_event,text='Mails')
        # self.sidebar_button_3.grid(row=3, column=0, padx=20, pady=10)
        self.sidebar_button_4 = customtkinter.CTkButton(self.sidebar_frame, command=self.navigateToSendMail,text='Send Mails')
        self.sidebar_button_4.grid(row=3, column=0, padx=20, pady=10)

        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"],command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["80%", "90%", "100%", "110%", "120%"],command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))
        # home view
        self.home_frame = HomeFrame(self)
        
        self.home_frame.grid(row=0, column=1, sticky="nsew")
        self.grid_rowconfigure(1, weight=5)
        self.appearance_mode_optionemenu.set("Light")
        self.scaling_optionemenu.set("100%")
        # self.home_frame.grid_remove()

        # MAINSEND WIDGETS
        self.mainsend_frame = customtkinter.CTkFrame(self, corner_radius=20, fg_color=["black", "black"],width=350,height=600)

        # Center-align content
        self.mainsend_frame.place(in_=self, anchor="c", relx=0.5, rely=0.5)
    
        wallet_label = customtkinter.CTkLabel(self.mainsend_frame, text="Recipient emails", text_color='white', font=("serif", 22))
        wallet_label.grid(row=0, column=0, padx=(20, 10), pady=(20, 5), sticky="w")

        fund_label = customtkinter.CTkLabel(self.mainsend_frame, text="Website Url", text_color='white', font=("serif", 22))
        fund_label.grid(row=1, column=0, padx=(20, 10), pady=5, sticky="w")

        unit_label = customtkinter.CTkLabel(self.mainsend_frame, text="Title of the Mail", font=("serif", 22), text_color='white')
        unit_label.grid(row=2, column=0, padx=(20, 10), pady=5, sticky="w")

        self.file_upload_button = customtkinter.CTkButton(self.mainsend_frame,  width=400, text_color='black',text='upload email list txt file', font=("serif", 22),fg_color='white',command=self.upload_txt_file)
        self.file_upload_button.grid(row=0, column=1, padx=10, pady=(20, 5), sticky="w")

        self.website_link = customtkinter.CTkEntry(self.mainsend_frame, placeholder_text='eg https://codeblazeacademy.net', width=400, text_color='black', font=("serif", 22))
        self.website_link.grid(row=1, column=1, padx=10, pady=5, sticky="w")

        self.title_of_mail = customtkinter.CTkEntry(self.mainsend_frame,placeholder_text='title of mail', width=400, text_color='black', font=("serif", 22))
        self.title_of_mail.grid(row=2, column=1, padx=10, pady=5, sticky="w")

        # Create a button at the bottom (Initially hidden)
        self.send_button = customtkinter.CTkButton(self.mainsend_frame, text="Send Mails", width=200, text_color='black', font=("serif", 22),command=self.sendmail_thread)
        self.send_button.grid(row=6, column=0, padx=(20, 10), pady=(20, 20), sticky="e")
        self.send_button.grid_remove()
        # self.preview_mail_template = customtkinter.CTkButton(self.card_frame, text="Select Email Template", width=200, text_color='white', font=("serif", 22),command=self.sendmail_thread)
        # self.preview_mail_template.grid(row=4, column=1, padx=(20, 10), pady=(20, 20), sticky="e")
        # self.preview_mail_template.grid_remove()
        # self.configure(fg_color=['white','#243028'])
        # # Call a function to animate the frame and button
        # self.template_combobox = customtkinter.CTkComboBox(self.card_frame, width=300, font=("serif", 18),values=['1'])
        # self.template_combobox.grid(row=4, column=1, padx=(20, 10), pady=(20, 20), sticky="e")

        # # Populate the combobox with template names from the template folder
        # template_folder = "email-templates/1/"
        # template_files = os.listdir(template_folder)
        # self.template_combobox._values=template_files

        # # Create a text widget for displaying the selected template
        # self.template_text_widget = customtkinter.CTkTextbox(self.card_frame, width=300, height=10, font=("serif", 16))
        # self.template_text_widget.grid(row=5, column=1, padx=(20, 10), pady=(0, 20), sticky="e")

        # # Create a button to load the selected template
        # self.load_template_button = customtkinter.CTkButton(self.card_frame, text="Load Template", width=20, text_color='white', font=("serif", 18), command=self.load_template)
        # self.load_template_button.grid(row=6, column=1, padx=(20, 10), pady=(10, 20), sticky="e")

        # # Hide the Send Mails button initially
        # self.send_button.grid_remove()
        # self.preview_mail_template.grid_remove()
        self.message_list={}
        self.maillist={}

        # self.animate_frame()
        self.mainsend_frame.place_forget()
        

        # self.mainsend_frame.grid_remove()
        # Create a card frame for wallet information
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
        
        # topup view

        self.topupframe = customtkinter.CTkFrame(self, corner_radius=10, fg_color=["skyblue", "skyblue"])
        self.topupframe.grid(row=0, column=1, rowspan=2, padx=20, pady=20, sticky="nsew")

        wallet_label = customtkinter.CTkLabel(self.topupframe, text="Amount:($)", text_color='white', font=("serif", 22))
        wallet_label.grid(row=0, column=0, padx=(20, 10), pady=(20, 5), sticky="w")

        fund_label = customtkinter.CTkLabel(self.topupframe, text="Currency", text_color='white', font=("serif", 22))
        fund_label.grid(row=1, column=0, padx=(20, 10), pady=5, sticky="w")

        # unit_label = customtkinter.CTkLabel(self.card_frame, text="Available Unit:", font=("serif", 22), text_color='white')
        # unit_label.grid(row=2, column=0, padx=(20, 10), pady=5, sticky="w")

        self.amount_value = customtkinter.CTkEntry(self.topupframe,placeholder_text='eg 20,40 etc', width=200, text_color=['black','white'], font=("serif", 22))
        self.amount_value.grid(row=0, column=1, padx=10, pady=(20, 5), sticky="w")

        self.currency_value = customtkinter.CTkComboBox(self.topupframe, values=['USD'], width=200, text_color=['black','white'], font=("serif", 22))
        self.currency_value.grid(row=1, column=1, padx=10, pady=5, sticky="w")

        # unit_value = customtkinter.CTkLabel(self.card_frame, text="0", width=200, text_color='white', font=("serif", 22))
        # unit_value.grid(row=2, column=1, padx=10, pady=5, sticky="w")

        fund_button = customtkinter.CTkButton(self.topupframe, text="Fund Wallet", width=200, text_color='white', font=("serif", 22),command=self.topUpEndPoint)
        fund_button.grid(row=3, column=1, padx=(20, 10), pady=(20, 20), sticky="w")

        self.topupframe.grid_remove()


        # the sendnavform
        # Create a card frame for wallet information
        self.sendnavform_frame = customtkinter.CTkFrame(self, corner_radius=10, fg_color=["skyblue", "skyblue"])
        self.sendnavform_frame.grid(row=0, column=1, rowspan=2, padx=20, pady=20, sticky="nsew")
        self.sendnavform_frame.grid_remove()

        self.email_host = customtkinter.CTkLabel(self.sendnavform_frame, text="Email_Host", text_color=['white','black'], font=("serif", 22))
        self.email_host.grid(row=0, column=0, padx=(20, 10), pady=(20, 5), sticky="w")

        self.email_host_user = customtkinter.CTkLabel(self.sendnavform_frame, text="Email_Host_User", text_color=['white','black'], font=("serif", 22))
        self.email_host_user.grid(row=1, column=0, padx=(20, 10), pady=5, sticky="w")

        self.host_password_label = customtkinter.CTkLabel(self.sendnavform_frame, text="Email_Host_Password", text_color=['white','black'], font=("serif", 22))
        self.host_password_label.grid(row=2, column=0, padx=(20, 40), pady=5, sticky="w")

        self.email_port_label = customtkinter.CTkLabel(self.sendnavform_frame, text="Email_Port", text_color=['white','black'], font=("serif", 22))
        self.email_port_label.grid(row=3, column=0, padx=(20, 40), pady=5, sticky="w")

        self.email_ssl_label = customtkinter.CTkLabel(self.sendnavform_frame, text="SSL/TLS", text_color=['white','black'], font=("serif", 22))
        self.email_ssl_label.grid(row=4, column=0, padx=(20, 40), pady=5, sticky="w")

        # self.email_tls_label = customtkinter.CTkLabel(card_frame, text="Use_TLS", text_color=['white','black'], font=("serif", 22))
        # self.email_tls_label.grid(row=5, column=0, padx=(20, 40), pady=5, sticky="w")
        # unit_label = customtkinter.CTkLabel(card_frame, text="Available Unit:", font=("serif", 22), text_color='white')
        # unit_label.grid(row=2, column=0, padx=(20, 10), pady=5, sticky="w")

        

        # fund_value = customtkinter.CTkComboBox(card_frame, values=['USD'], width=200, text_color='black', font=("serif", 22))
        # fund_value.grid(row=1, column=1, padx=10, pady=5, sticky="w")

        # unit_value = customtkinter.CTkLabel(card_frame, text="0", width=200, text_color='white', font=("serif", 22))
        # unit_value.grid(row=2, column=1, padx=10, pady=5, sticky="w")

        self.savebutton = customtkinter.CTkButton(self.sendnavform_frame, text="Save", width=200, text_color='white', font=("serif", 22),command=self.navigatetoMainSendView)
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
                self.emailhostfield = customtkinter.CTkEntry(self.sendnavform_frame,placeholder_text='eg mail.supressedman.com', width=400, text_color=['black','white'], font=("serif", 22))
                self.emailhostfield.insert(0,"None")
                self.emailhostfield.grid(row=0, column=1, padx=10, pady=(20, 5), sticky="w")

                self.emailhostuserfield = customtkinter.CTkEntry(self.sendnavform_frame,placeholder_text='eg support@supressedman.com', width=400, text_color=['black','white'], font=("serif", 22))
                self.emailhostuserfield.insert(0,"None")
                self.emailhostuserfield.grid(row=1, column=1, padx=10, pady=(20, 5), sticky="w")

                self.emailpasswordfield = customtkinter.CTkEntry(self.sendnavform_frame,placeholder_text='eg Sup1234!', width=400, text_color=['black','white'], font=("serif", 22))
                self.emailpasswordfield.insert(0,"None")
                self.emailpasswordfield.grid(row=2, column=1, padx=10, pady=(20, 5), sticky="w")

                self.emailportfield = customtkinter.CTkEntry(self.sendnavform_frame,placeholder_text='eg 420', width=400, text_color=['black','white'], font=("serif", 22))
                self.emailportfield.insert(0,"None")
                self.emailportfield.grid(row=3, column=1, padx=10, pady=(20, 5), sticky="w")

                self.sslfield = customtkinter.CTkComboBox(self.sendnavform_frame,values=['SSL','TLS'],width=400, text_color=['black','white'], font=("serif", 22))
                self.sslfield.grid(row=4, column=1, padx=10, pady=(20, 5), sticky="w")

                # self.tlsfield = customtkinter.CTkComboBox(card_frame,values=['SSL','TLS'], width=400, text_color=['black','white'], font=("serif", 22))
                # self.tlsfield.grid(row=5, column=1, padx=10, pady=(20, 5), sticky="w")
            else:
                
                self.emailhostfield = customtkinter.CTkEntry(self.sendnavform_frame,placeholder_text='eg mail.supressedman.com', width=400, text_color=['black','white'], font=("serif", 22))
                self.emailhostfield.insert(0,email_host)
                self.emailhostfield.grid(row=0, column=1, padx=10, pady=(20, 5), sticky="w")

                self.emailhostuserfield = customtkinter.CTkEntry(self.sendnavform_frame,placeholder_text='eg support@supressedman.com', width=400, text_color=['black','white'], font=("serif", 22))
                self.emailhostuserfield.insert(0,email_host_user)
                self.emailhostuserfield.grid(row=1, column=1, padx=10, pady=(20, 5), sticky="w")

                self.emailpasswordfield = customtkinter.CTkEntry(self.sendnavform_frame,placeholder_text='eg Sup1234!', width=400, text_color=['black','white'], font=("serif", 22),show="*")
                self.emailpasswordfield.insert(0,email_host_password)
                self.emailpasswordfield.grid(row=2, column=1, padx=10, pady=(20, 5), sticky="w")

                self.emailportfield = customtkinter.CTkEntry(self.sendnavform_frame,placeholder_text='eg 420', width=400, text_color=['black','white'], font=("serif", 22))
                self.emailportfield.insert(0,email_port)
                self.emailportfield.grid(row=3, column=1, padx=10, pady=(20, 5), sticky="w")

                self.sslfield = customtkinter.CTkComboBox(self.sendnavform_frame,values=['SSL','TLS'],width=400, text_color=['black','white'], font=("serif", 22))
                self.sslfield.grid(row=4, column=1, padx=10, pady=(20, 5), sticky="w")

                # self.tlsfield = customtkinter.CTkComboBox(card_frame,values=['False','True'], width=400, text_color=['black','white'], font=("serif", 22))
                # self.tlsfield.grid(row=5, column=1, padx=10, pady=(20, 5), sticky="w")
            # self.send_mail_ui.email_host_edit.setText(email_host)
            # self.send_mail_ui.email_host_user_edit.setText(email_host_user)
            # self.send_mail_ui.email_port_edit.setText(email_port)
            # self.send_mail_ui.emal_host_password_edit.setText(email_host_password)
        
        # import mainsendviewframe as mf

        # app=mf.MainSendLayoutComponent()
        
        # self.wallet_address_label.setText(str(walletid))
        # self.availablefund_label.setText(str(wallet_amount))
        # self.availableunit_label.setText(f'{units_of_mails}mails unit')
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
            import tkinter.messagebox as tkmb
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
    def navigateToTopup(self):
        # import topupview
        # topUpObj=topupview.App()
        # topUpObj.mainloop()
        self.card_frame.grid_remove()
        self.topupframe.grid()
    def navigateToHome(self):
        self.card_frame.grid_remove()
        self.topupframe.grid_remove()
        self.mainsend_frame.place_forget()
        self.sendnavform_frame.grid_remove()
        self.grid()

    def change_appearance_mode_event(self, new_appearance_mode: str):
        with open('themevalue.txt','w') as themefile:
            themefile.write(str(new_appearance_mode))
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    def sidebar_button_event(self):
        print("sidebar_button click")

    # def navigateToFundView(self):
    #     # import topupview
    #     # fundviewObj=topupview.App()
    #     # fundviewObj.mainloop()
    #     self.card_frame.pack_forget()
    #     self.topupframe.pack()
    
    def navigateToWallet(self):
        # import wallet
        # walletObj=wallet.App()
        # walletObj.mainloop()
        self.topupframe.grid_remove()
        self.card_frame.grid()
    def navigateToHome(self):
        import homeview
        homeObj=homeview.App()
        homeObj.mainloop()
    
    # def navigateToWallet(self):
    #     import wallet
    #     walletObj=wallet.App()
    #     walletObj.mainloop()

    # def navigateToSendView(self):
    #     import sendnavformview
    #     sendViewObj=sendnavformview.App()
    #     sendViewObj.mainloop()
    
    def upload_txt_file(self):
        import tkinter.messagebox as tkmb
        from tkinter import filedialog
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


    def loadthreadview(self):
        import simulateloading
        self.loadObj=simulateloading.root.mainloop()

    def start_load_thread(self):
        # import tkinter as tk
        # import simulateloading as sl

        # # if __name__ == "__main__":
        # self.root = tk.Tk()
        # self.app = sl.LoadingApp(self.root)
        # self.app.start_loading_thread()
        # self.root.mainloop()
        import threading
        global load_thread
    #   progress_bar.start()
        load_thread = threading.Thread(target=self.threa)
        load_thread.start()
    def stopload_thread(self):
        # global load_thread
        # if load_thread and load_thread.is_alive():
        #     load_thread.join()
        # progress_bar.stop()
        self.app.stop_loading_thread()

    def send_email(self):
        
        # tkmb.showinfo(title="Email Sending Alert",message="You are about sending messages to the uploaded email list txt file, time the receive success message depends on the number of emails to send")
        self.after(100,self.start_load_thread)
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
        import requests
        # Make a request to get SMTP credentials
        from baseurlfile import base_url
        smtp_response = requests.get(f'{base_url}api/smtpcredentials/', headers=headers)

        if smtp_response.status_code == 200:
            email_host = smtp_response.json().get('email_host')
            email_host_user = smtp_response.json().get('email_host_user')
            email_host_password = smtp_response.json().get('email_host_password')
            email_port = smtp_response.json().get('email_port')
            email_usessl_or_tls=smtp_response.json().get('email_usessl_or_tls')

            import smtplib
            from email.mime.text import MIMEText
            from email.mime.multipart import MIMEMultipart
            from multiprocessing import Pool
            import json
            import requests
            # SMTP server configuration
            smtp_server = 'server213.web-hosting.com'
            smtp_port = 25  # Replace with the appropriate SMTP port (e.g., 587 for TLS)
            smtp_username = 'support@codeblazeacademy.net'
            smtp_password = 'Kelechi1999!'
            from baseurlfile import base_url
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
            smtp_response = requests.get(f'{base_url}api/smtpcredentials/', headers=headers)

            if smtp_response.status_code == 200:
                email_host = smtp_response.json().get('email_host')
                email_host_user = smtp_response.json().get('email_host_user')
                email_host_password = smtp_response.json().get('email_host_password')
                email_port = smtp_response.json().get('email_port')
                email_usessl_or_tls=smtp_response.json().get('email_usessl_or_tls')
            # Function to send an email
            # def send_email(recipient_email, email_number, message):
                
                print(self.maillist['0'])
                if str(email_usessl_or_tls).lower()=='tls'.lower():
                #     import ast
                # # Remove the outer double quotes from the string to get the inner dictionary string
                #     innermaillist = maillist.strip('"')

                #     # Convert the inner dictionary string to a Python dictionary using ast.literal_eval()
                #     resultmaillist = ast.literal_eval(innermaillist)
                    

                #     # Convert the inner dictionary string to a Python dictionary using ast.literal_eval()
                    
                
                #     resultmaillist=list(resultmaillist.values())
                    
                #     # for _ in range(3-1):
                #     #     print(_)
                #     #     increment+=1
                #     # increment=increment
                #     # print(increment)
                #     # print(innermailbody)
                    
                
                #         # Remove newlines and unwanted characters from the line
                        
                                
                                
                    increment_send=0     
                    for _ in range(int(len(self.maillist))):
                        increment_send+=1
                    
                        import appdirs
                        from pathlib import Path

                        # Get the appropriate directory for application-specific data
                        app_data_dir = appdirs.user_data_dir()

                        file_name = "emails.json"
                        file_path = Path(app_data_dir) / file_name
                        
                        with open(file_path, 'r') as file:
                            
                            import json
                            import re
                            data_loaded=json.load(file)

                        # for index in int(len(data_loaded)):

                        # print(data_loaded[f'{increment_send}'])
                        # print(resultmailbody[increment])
                        print(self.maillist[str(increment_send-1)])
                        
                        # print((resultmailbody[increment]))

                # for listofmails in range(int(len(list()))):
                #     print((resultmaillist[listofmails]))

                
                        
                    # print(mailstosend)
                    # print(mailstosend[0])
                    
                        import smtplib
                        from email.mime.multipart import MIMEMultipart
                        from email.mime.text import MIMEText
                        # 'email_host','email_host_user','email_host_password','email_port
                        
                            # Create a MIME message
                        message = MIMEMultipart()
                        message['From'] = email_host_user
                        message['To'] = self.maillist[str(increment_send-1)]
                        message['Subject'] = title_text

                        text_content = "This is an important message."
                        html_content = """<!DOCTYPE html>
                        <html lang="en">

                            <head>
                                <meta charset="UTF-8">
                                <meta http-equiv="X-UA-Compatible" content="IE=edge">
                                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                                <title>Mail Template</title>
                                <style>div.messagebody{
                                        height: 100vh;
                                        width: 100vw;
                                        margin: 0;
                                        
                                        background:white;
                                    }
                                    div.footer{
                                        
                                        height: 2rem;
                                        background-color: rgb(91, 54, 169);;
                                    }
                                    div.footer p,div.footer p a{
                                        color:white;
                                        text-align: center;
                                        text-decoration: none;
                                    }
                                    div.navdiv{
                                        height: 2.5rem;
                                        padding: 0;
                                        color:white;
                                        text-align: center;
                                    }
                                    @media only screen and (max-width: 600px)  {
                                    body{
                                        width: 100vw;
                                        padding:0;
                                        margin:0;
                                    }
                                    
                                    div.messagebody{
                                        width: 100%;
                                        height: 80vh;
                                        background-color: white;
                                    }
                                    div.messagebody p{
                                        word-wrap: break-word;
                                        text-align: center;
                                    }
                                    }
                                    
                                    
                                </style>
                            </head>
                            <body style="background-color:rgb(91, 54, 169);">
                                <div class="navdiv" >
                                """+f"{title_text}"+f"""
                                    
                                    <p>Unlocking potentials through learning</p>
                                </div>

                                
                                <div class="messagebody">
                                    <p>"""+data_loaded[f'{increment_send}']+f""" click this link to visit my site {site_url_text}</a> </p>
                                </div>
                                <div class="footer">
                                    <p><a  href="">support@codeblazeacademy.net</a></p>
                                </div>
                            </body>
                            </html>"""
                            
                        
                        # Attach the HTML template to the email
                        message.attach(MIMEText(html_content, 'html'))
                        
                        if increment_send>(int(len(self.maillist))):
                            break
                        try:
                            with smtplib.SMTP(email_host, email_port) as server:  # Use SMTP_SSL for SSL connection
                                server.starttls()
                                server.login(email_host_user, email_host_password)
                                server.sendmail(email_host_user,self.maillist[str(increment_send-1)],message.as_string())
                                print(f'Email sent to ',self.maillist[str(increment_send-1)])
                                
                                
                                # return Response({"message_sent_response":f'Email sent to ,{resultmaillist[increment_send]}'},status=status.HTTP_200_OK)
                            
                               
                        except:
                            pass
                    import tkinter.messagebox as tkmb
                    tkmb.showinfo(title="Email Alert",message="Generated Messages sent successfully to the uploaded email list txt file")
                        
                        # except:
                        #     print(f'Failed to send email to : ',resultmaillist[increment_send])
                            
                        #     time.sleep(1)
                        #     return Response({"messege_sent_response":f'Failed to send email to :  ,{resultmaillist[increment_send]}'},status=status.HTTP_200_OK)
                        
                        

                        # increment_send+=1
                        # time.sleep(1)
                        
                            


                    # return Response({"message_sent_response":"messages sent to the uploaded emails successfully"},status=status.HTTP_200_OK)

                else:
                    
                    # import ast
                    # # Remove the outer double quotes from the string to get the inner dictionary string
                    # innermaillist = maillist.strip('"')

                    # # Convert the inner dictionary string to a Python dictionary using ast.literal_eval()
                    # resultmaillist = ast.literal_eval(innermaillist)
                    

                    # # Convert the inner dictionary string to a Python dictionary using ast.literal_eval()
                    
                
                    # resultmaillist=list(resultmaillist.values())
                    
                    # for _ in range(3-1):
                    #     print(_)
                    #     increment+=1
                    # increment=increment
                    # print(increment)
                    # print(innermailbody)
                    
                
                        # Remove newlines and unwanted characters from the line
                        
                                
                                
                    increment_send=0     
                    for _ in range(int(len(self.maillist))):
                        increment_send+=1
                        import os
                        import appdirs
                        from pathlib import Path

                        # Get the appropriate directory for application-specific data
                        app_data_dir = appdirs.user_data_dir()

                        file_name = "emails.json"
                        file_path = Path(app_data_dir) / file_name
                        
                        with open(file_path, 'r') as file:
                            
                            import json
                            import re
                            data_loaded=json.load(file)

                        # for index in int(len(data_loaded)):

                        # print(data_loaded[f'{increment_send}'])
                        # print(resultmailbody[increment])
                        # print(resultmaillist[increment_send-1])
                        
                        # print((resultmailbody[increment]))

                # for listofmails in range(int(len(list()))):
                #     print((resultmaillist[listofmails]))

                
                        
                    # print(mailstosend)
                    # print(mailstosend[0])
                    
                        import smtplib
                        from email.mime.multipart import MIMEMultipart
                        from email.mime.text import MIMEText
                        # 'email_host','email_host_user','email_host_password','email_port
                        
                            # Create a MIME message
                        message = MIMEMultipart()
                        message['From'] = email_host_user
                        message['To'] = self.maillist[str(increment_send-1)]
                        message['Subject'] = title_text

                        text_content = "This is an important message."
                        html_content = """<!DOCTYPE html>
                        <html lang="en">

                            <head>
                                <meta charset="UTF-8">
                                <meta http-equiv="X-UA-Compatible" content="IE=edge">
                                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                                <title>Mail Template</title>
                                <style>div.messagebody{
                                        height: 100vh;
                                        width: 100vw;
                                        margin: 0;
                                        
                                        background:white;
                                    }
                                    div.footer{
                                        
                                        height: 2rem;
                                        background-color: rgb(91, 54, 169);;
                                    }
                                    div.footer p,div.footer p a{
                                        color:white;
                                        text-align: center;
                                        text-decoration: none;
                                    }
                                    div.navdiv{
                                        height: 2.5rem;
                                        padding: 0;
                                        color:white;
                                        text-align: center;
                                    }
                                    @media only screen and (max-width: 600px)  {
                                    body{
                                        width: 100vw;
                                        padding:0;
                                        margin:0;
                                    }
                                    
                                    div.messagebody{
                                        width: 100%;
                                        height: 80vh;
                                        background-color: white;
                                    }
                                    div.messagebody p{
                                        word-wrap: break-word;
                                        text-align: center;
                                    }
                                    }
                                    
                                    
                                </style>
                            </head>
                            <body style="background-color:rgb(91, 54, 169);">
                                <div class="navdiv" >
                                """+f"{title_text}"+f"""
                                    
                                    <p>Unlocking potentials through learning</p>
                                </div>

                                
                                <div class="messagebody">
                                    <p>"""+data_loaded[f'{increment_send}']+f""" click this link to visit my site {site_url_text}</a> </p>
                                </div>
                                <div class="footer">
                                    <p><a  href="">support@codeblazeacademy.net</a></p>
                                </div>
                            </body>
                            </html>"""
                            
                        
                        # Attach the HTML template to the email
                        message.attach(MIMEText(html_content, 'html'))
                        
                        if increment_send>(int(len(self.maillist))):
                            break
                        try:
                            with smtplib.SMTP_SSL(email_host, email_port) as server:  # Use SMTP_SSL for SSL connection
                                server.login(email_host_user, email_host_password)
                                server.sendmail(email_host_user,self.maillist[str(increment_send-1)],message.as_string())
                                print(f'Email sent to ',self.maillist[str(increment_send-1)])
                                
                                
                                # return Response({"message_sent_response":f'Email sent to ,{resultmaillist[increment_send]}'},status=status.HTTP_200_OK)
                            
                                
                        except:
                            pass
                    import tkinter.messagebox as tkmb
                    self.stopload_thread()
                    self.root.destroy()
                    tkmb.showinfo(title="Email Alert",message="Generated Messages sent successfully to the uploaded email list txt file")
                        # except:
                        #     print(f'Failed to send email to : ',resultmaillist[increment_send])
                            
                        #     time.sleep(1)
                        #     return Response({"messege_sent_response":f'Failed to send email to :  ,{resultmaillist[increment_send]}'},status=status.HTTP_200_OK)
                        
                        

                        # increment_send+=1
                        # time.sleep(1)
                        
                            
    def navigatetoMainSendView(self):
        import tkinter.messagebox as tkmb
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
                # import mainsendview
                # mainSendObj=mainsendview.App()
                # mainSendObj.mainloop()
                self.card_frame.grid_remove()

                self.topupframe.grid_remove()
                self.sendnavform_frame.grid_remove()
                self.home_frame.grid_remove()
                # self.animate_frame()
                self.mainsend_frame.place(in_=self, anchor="c", relx=0.5, rely=0.5)

                
                
            else:
                pass
                
    def sendmail_thread(self):
        import threading
        global send_thread
        # progress_bar.sart()
        send_thread = threading.Thread(target=self.send_email)
        send_thread.start()
    def navigateToTopup(self):
        # import topupview
        # topUpObj=topupview.App()
        # topUpObj.mainloop()
        self.home_frame.grid_remove()
        self.card_frame.grid_remove()
        self.mainsend_frame.place_forget()
        self.sendnavform_frame.grid_remove()
        self.topupframe.grid()
        
    def navigateToHome(self):
        self.card_frame.grid_remove()
        self.mainsend_frame.place_forget()
        self.sendnavform_frame.grid_remove()
        self.topupframe.grid_remove()
        self.home_frame.grid()

    def load_template(self):
        import os
        selected_template = self.template_combobox.get()

        # Specify the folder where your email templates are stored
        template_folder = "email-templates/1"

        # Build the path to the selected template file
        template_path = os.path.join(template_folder, selected_template)

        # Read the selected template file and display it in a text widget or any other widget you prefer
        import tkinter as tk
        with open(template_path, 'r') as template_file:
            template_content = template_file.read()
            self.template_text_widget.delete('1.0', tk.END)  # Clear previous content
            self.template_text_widget.insert(tk.END, template_content)

    def change_appearance_mode_event(self, new_appearance_mode: str):
        with open('themevalue.txt','w') as themefile:
            themefile.write(str(new_appearance_mode))
        customtkinter.set_appearance_mode(new_appearance_mode)


    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    def sidebar_button_event(self):
        print("sidebar_button click")

    # def animate_frame(self):
    #     self.mainsend_frame.update()
    #     frame_height = self.mainsend_frame.winfo_height()
    #     frame_width = self.mainsend_frame.winfo_width()
    #     center_x = (self.winfo_width() - frame_width) / 2  # Centered position along the x-axis
    #     center_y = (self.winfo_height() - frame_height) / 2  # Centered position along the y-axis

    #     initial_y = frame_height  # Starting position above the window

    #     # Animate frame sliding from above to center
    #     for y in range(int(initial_y), int(center_y) + 1, 10):
    #         self.mainsend_frame.place_configure(relx=0.5, rely=0.5, x=center_x, y=y)
    #         self.update()
    #         self.after(20)  # Adjust the speed of animation by changing this value

    #     # Show the Send Mails button
    #     self.send_button.grid()
    #     self.update()

    def show_notification(self,message):
        import tkinter as tk
        notification_window = tk.Tk()
        notification_window.title("Notification")
        notification_window.geometry("300x100+900+500")  # Adjust the position as needed

        label = tk.Label(notification_window, text=message, padx=10, pady=10)
        label.pack()

        notification_window.after(60000, notification_window.destroy)  # Close notification after 5 seconds
        # notification_window.mainloop()

    # Create the main application window
    # root = tk.Tk()
    # root.title("App Version Checker")

    # Create a button to check the app version
    
    

        # Run the Tkinter main loop
        
    
    

    def set_light_theme():
        thememanager.set_theme("light")
    
    def navigateToHome(self):
        self.card_frame.grid_remove()
        self.mainsend_frame.place_forget()
        self.sendnavform_frame.grid_remove()
        self.topupframe.grid_remove()
        self.home_frame.grid()

# Function to change the theme to 'dark'
    def set_dark_theme():
        thememanager.set_theme("dark")

    # Function to change the theme to 'system'
    def set_system_theme():
        thememanager.set_theme("system")

    def navigateToWallet(self):
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self.makeAllWalletRequest())
        import json
        with open("cachefiles/wallet.json",'r') as walletFile:
            data=json.load(walletFile)
            # [{"wallet_amount": 3887, "wallet_id": "3809998921", "unit_of_mails": 388700.0}]
            walletid=data['wallet_id']
            wallet_amount=data['wallet_amount']
            units_of_mails=data['unit_of_mails']
        self.wallet_value.configure(text=str(walletid))

        self.fund_value.configure(text=str(wallet_amount))

        self.unit_value.configure(text=str(units_of_mails))

        self.unit_value = customtkinter.CTkLabel(self.card_frame, text=str(units_of_mails), width=200, text_color='white', font=("serif", 22))
        self.unit_value.grid(row=2, column=1, padx=10, pady=5, sticky="w")

        walletFile.close()
        self.topupframe.grid_remove()
        self.mainsend_frame.place_forget()
        self.sendnavform_frame.grid_remove()
        self.home_frame.grid_remove()
        self.card_frame.grid(row=0, column=1, rowspan=1, padx=20, pady=20, sticky="nsew")
        

    # def navigateToNavSendView(self):
        
    #     self.navform
        

if __name__ == "__main__":
    app = App()
    app.mainloop()
    import time
    check_app_version() 
   

    app.mainloop()
