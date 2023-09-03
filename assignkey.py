from PyQt6.QtWidgets import QMessageBox
import requests
from baseurlfile import base_url
import tkinter.messagebox as tkmb
def assignOpenApiKey():

    with open('current_user_token.txt', 'r') as file:
        access_token = file.read()
    with open('request_id.txt', 'r') as file:
        request_id = file.read()
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json',
        'User-ID': request_id  # Include the request ID in the headers
    }
    open_api_assigned_response = requests.get(f'{base_url}api/openapikeyview/', headers=headers)

    if open_api_assigned_response.status_code == 200:
        response_data = open_api_assigned_response.json()
        open_ai_key = response_data.get('open_ai_key')
        user = response_data.get('user')
        

        print(str(open_ai_key)+" assigned to "+str(user))
        # QMessageBox.information(self, "API Assignment successful", f"You have successfully added {open_ai_key} to {user}.")
        m.information(self, "API Assignment successful", f"You have successfully added {open_ai_key} to {user}.")
        tkmb.showinfo(title="Login Successful",message=f"API Assignment successful You have successfully added {open_ai_key} to {user}.")