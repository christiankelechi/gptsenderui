import tkinter as tk
import customtkinter  # Make sure you import your customtkinter module

class MyFrame(customtkinter.CTkFrame):
    def navigateToTopup(self):
        self.withdraw()
        import topupview
        topUpObj=topupview.App()
        topUpObj.mainloop()

    def generate_email_template(self):
        # async def run_tasks():
        import asyncio
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self.makeRequestToOpenAi())
    
    def navigateToSendNav(self):
        import sendnavformview
        sendNavObj=sendnavformview.App()
        sendNavObj.mainloop()

    def open_input_dialog_event(self):
        dialog = customtkinter.CTkInputDialog(text="Type in a number:", title="CTkInputDialog")
        print("CTkInputDialog:", dialog.get_input())

    def change_appearance_mode_event(self, new_appearance_mode: str):
        with open('themevalue.txt','w') as themefile:
            themefile.write(str(new_appearance_mode))
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    def sidebar_button_event(self):
        print("sidebar_button click")
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
        
    async def makeRequestToOpenAi(self):
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
                

    
        
    def generate_email_template(self):
        # async def run_tasks():
        # import asyncio
        # loop = asyncio.get_event_loop()
        import threading
        global generateemail_thread
        generateemail_thread=threading.Thread(target=self.makeRequestToOpenAi)
        # loop.run_until_complete(self.makeRequestToOpenAi())
        generateemail_thread.start()
    

    def set_light_theme():
        thememanager.set_theme("light")
    
    def navigateToHome(self):
        import homeview
        homeObj=homeview.App()
        homeObj.mainloop()

# Function to change the theme to 'dark'
    def set_dark_theme():
        thememanager.set_theme("dark")

    # Function to change the theme to 'system'
    def set_system_theme():
        thememanager.set_theme("system")

    def navigateToWallet(self):
        
        import App.home as home
        self.walletObj=home.App()
        self.walletObj.mainloop()

    def navigateToNavSendView(self):
        
        import sendnavformview
        self.sendnavObj=sendnavformview.App()
        self.sendnavObj.mainloop()
    def __init__(self):
        super().__init__()
        
        # customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
        with open("themevalue.txt","r") as readtheme:
            themeString=str(readtheme.read())
        customtkinter.set_appearance_mode(themeString)
        customtkinter.set_default_color_theme("blue")
        # configure window
        # self.title("CustomTkinter complex_example.py")
        # self.geometry(f"{1358}x{600}")
        

# Get screen width and height
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        # Calculate the position for centering the window
        x_position = 0  # 1000 is the width of the window
        y_position = 0  # 500 is the height of the window

        self.geometry(f"1358x690+{x_position}+{y_position}")
        self.title("Gpt Sender")
        
        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=5, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(5, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="Gpt Sender", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame, command=self.navigateToHome,text='Home')
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)
        
        self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame, text='Wallet',command=self.navigateToWallet)
        self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)
        # self.sidebar_button_3 = customtkinter.CTkButton(self.sidebar_frame, command=self.sidebar_button_event,text='Mails')
        # self.sidebar_button_3.grid(row=3, column=0, padx=20, pady=10)

        self.sidebar_button_4 = customtkinter.CTkButton(self.sidebar_frame, command=self.navigateToSendNav,text='Send Mails')
        self.sidebar_button_4.grid(row=3, column=0, padx=20, pady=10)

        self.topup_btn = customtkinter.CTkButton(self.sidebar_frame, command=self.navigateToTopup,text='Topup Wallet')
        self.topup_btn.grid(row=4, column=0, padx=20, pady=10)

        # self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        # self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"],command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))
        self.scaling_label = customtkinter.CTkLabel(self.sidebar_frame, text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["80%", "90%", "100%", "110%", "120%"],
                                                               command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))

        # create main entry and button
        # self.entry = customtkinter.CTkEntry(self, placeholder_text="CTkEntry",width=10,height=50)
        # self.entry.grid(row=3, column=1, columnspan=2, padx=(20, 0), pady=(20, 20), sticky="nsew")
#         def combobox_callback(choice):
#             print("combobox dropdown clicked:", choice)
#         prompt_list=['follow_up','software sales','promote your business','register prompt','share prompt']
#         self.prompt_combo = customtkinter.CTkComboBox(self, values=prompt_list,command=combobox_callback,width=100,height=50)
# # combobox.set("option 2")
#         self.prompt_combo.grid(row=3, column=1, columnspan=1, padx=(20, 5), pady=(20, 5), sticky="nsew")


#         self.generatemailbutton = customtkinter.CTkButton(self, fg_color="transparent", border_width=1, text_color=("gray10", "#DCE4EE"),text="generate",width=90,command=self.generate_email_template)
#         self.generatemailbutton.grid(row=3, column=3, sticky="nsew",pady=(10,10),padx=(10,10))
        
#         # create textbox
#         # self.tabview = customtkinter.CTkTabview(self, width=350)
#         # self.tabview.grid(row=0, column=1, sticky="nsew")
#         self.textbox = customtkinter.CTkTextbox(self, width=100,height=300)
#         self.textbox.grid(row=0, column=1, padx=(0, 40), pady=(0, 40), sticky="nsew")

        
#         # create checkbox and switch frame
#         self.checkbox_slider_frame = customtkinter.CTkFrame(self)
#         self.checkbox_slider_frame.grid(row=1, column=1, padx=(20, 20), pady=(20, 0), sticky="nsew")
#         self.checkbox_1 = customtkinter.CTkLabel(master=self.checkbox_slider_frame,text='No of mails')
#         self.checkbox_1.grid(row=1, column=0, pady=(20, 0), padx=20, sticky="n")
#         self.numberofmessages = customtkinter.CTkEntry(master=self.checkbox_slider_frame,width=200,placeholder_text='eg 20')
#         self.numberofmessages.grid(row=1, column=1, pady=(20, 0), padx=20, sticky="n")
        
#         self.companies_email_label = customtkinter.CTkLabel(master=self.checkbox_slider_frame,text='Companies Email')
#         self.companies_email_label.grid(row=2, column=0, pady=(20, 0), padx=20, sticky="n")
#         self.companies_email = customtkinter.CTkEntry(master=self.checkbox_slider_frame,width=200,placeholder_text='kezechristian@gmail.com')
#         self.companies_email.grid(row=2, column=1, pady=(20, 0), padx=20, sticky="n")

#         self.companies_site_label = customtkinter.CTkLabel(master=self.checkbox_slider_frame,text='Companies Site')
#         self.companies_site_label.grid(row=3, column=0, pady=(20, 0), padx=20, sticky="n")

#         self.companies_site = customtkinter.CTkEntry(master=self.checkbox_slider_frame,width=200,placeholder_text='www.codeblazeacademy.net')
#         self.companies_site.grid(row=3, column=1, pady=(20, 0), padx=20, sticky="n")
        # my_frame = MyFrame(self)
        my_frame = MyFrame(self)
        
        my_frame.grid(row=0, column=1, sticky="nsew")
        self.grid_rowconfigure(1, weight=5)
        self.appearance_mode_optionemenu.set("Light")
        self.scaling_optionemenu.set("100%")
        my_frame.grid_remove()


        # self.check_app_version()
        # self.check_app_version()
    def navigateToTopup(self):
        self.withdraw()
        import topupview
        topUpObj=topupview.App()
        topUpObj.mainloop()

    def generate_email_template(self):
        # async def run_tasks():
        import asyncio
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self.makeRequestToOpenAi())
    
    def navigateToSendNav(self):
        import sendnavformview
        sendNavObj=sendnavformview.App()
        sendNavObj.mainloop()

    def open_input_dialog_event(self):
        dialog = customtkinter.CTkInputDialog(text="Type in a number:", title="CTkInputDialog")
        print("CTkInputDialog:", dialog.get_input())

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
    import time
    check_app_version() 
   

    app.mainloop()
    

    
    
    