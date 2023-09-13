import tkinter as tk
import customtkinter
import tkinter as tk
from tkinter import filedialog
import tkinter.messagebox as tkmb
import requests
import os
# customtkinter.set_appearance_mode("System")
# customtkinter.set_default_color_theme("blue")
import tkinter as tk
from tkinter import ttk
import threading
import time

# root.mainloop()
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


    def loadthreadview(self):
        import simulateloading
        self.loadObj=simulateloading.root.mainloop()

    def start_load_thread(self):
        import simulateloading as sl

        # if __name__ == "__main__":
        self.root = tk.Tk()
        self.app = sl.LoadingApp(self.root)
        self.app.start_loading_thread()
        self.root.mainloop()
    #     import threading
    #     global load_thread
    # #   progress_bar.start()
    #     load_thread = threading.Thread(target=self.loadthreadview)
    #     load_thread.start()
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
                    
                    self.stopload_thread()
                    self.root.destroy()
                    tkmb.showinfo(title="Email Alert",message="Generated Messages sent successfully to the uploaded email list txt file")
                        # except:
                        #     print(f'Failed to send email to : ',resultmaillist[increment_send])
                            
                        #     time.sleep(1)
                        #     return Response({"messege_sent_response":f'Failed to send email to :  ,{resultmaillist[increment_send]}'},status=status.HTTP_200_OK)
                        
                        

                        # increment_send+=1
                        # time.sleep(1)
                        
                            
    
    def sendmail_thread(self):
        import threading
        global send_thread
        # progress_bar.sart()
        send_thread = threading.Thread(target=self.send_email)
        send_thread.start()
        



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
        self.sidebar_frame.grid(row=0, column=0, rowspan=3, sticky="nsew")
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
        self.card_frame = customtkinter.CTkFrame(self, corner_radius=20, fg_color=["black", "black"],width=350,height=600)

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

        self.website_link = customtkinter.CTkEntry(self.card_frame, placeholder_text='eg https://codeblazeacademy.net', width=400, text_color='black', font=("serif", 22))
        self.website_link.grid(row=1, column=1, padx=10, pady=5, sticky="w")

        self.title_of_mail = customtkinter.CTkEntry(self.card_frame,placeholder_text='title of mail', width=400, text_color='black', font=("serif", 22))
        self.title_of_mail.grid(row=2, column=1, padx=10, pady=5, sticky="w")

        # Create a button at the bottom (Initially hidden)
        self.send_button = customtkinter.CTkButton(self.card_frame, text="Send Mails", width=200, text_color='black', font=("serif", 22),command=self.sendmail_thread)
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
        self.animate_frame()
    def load_template(self):
        selected_template = self.template_combobox.get()

        # Specify the folder where your email templates are stored
        template_folder = "email-templates/1"

        # Build the path to the selected template file
        template_path = os.path.join(template_folder, selected_template)

        # Read the selected template file and display it in a text widget or any other widget you prefer
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
