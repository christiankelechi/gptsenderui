import App.home as home
import customtkinter
class MainSendLayoutComponent(home.App):
    def setupmainsendlayout(self):
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
        self.card_frame.grid()
    def navigateToTopup(self):
        import topupview
        topUpObj=topupview.App()
        topUpObj.mainloop()

