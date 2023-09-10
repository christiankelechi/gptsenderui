import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from multiprocessing import Pool
import json
import requests
import tkinter as tk
from tkinter import messagebox

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
# Function to send an email
def send_email(recipient_email, email_number, message):
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_username, smtp_password)

        subject = f"Subject for Email {email_number}"
        sender_email = 'support@codeblazeacademy.net'  # Replace with your email address
        msg = MIMEMultipart()
        msg['From'] = email_host_user
        msg['To'] = recipient_email
        msg['Subject'] = subject

        body = """<!DOCTYPE html>
                <!-- ... (rest of your HTML template) ... -->
                </html>"""

        msg.attach(MIMEText(body, 'html'))

        server.sendmail(sender_email, recipient_email, msg.as_string())
        print(f"Email {email_number} sent to {recipient_email}")

        server.quit()
    except Exception as e:
        print(f"Email {email_number} sending failed with error: {str(e)}")

# ... Rest of your code ...

if __name__ == "__main__":
    # Create a Tkinter GUI window
    root = tk.Tk()
    root.title("Email Sender")

    # Initialize the email counter label
    email_counter = 0
    counter_label = tk.Label(root, text=f"Emails sent: {email_counter}")
    counter_label.pack()

    # Load email messages from JSON file
    with open('emails.json', 'r') as file:
        email_messages = json.load(file)

    # List of email addresses from a text file
    with open('emailslist.txt', 'r') as file:
        email_list = [line.strip() for line in file]

    # Define the number of processes (adjust as needed)
    num_processes = 10

    # Create a pool of processes and distribute the work
    with Pool(processes=num_processes) as pool:
        for i, recipient_email in enumerate(email_list):
            if str(i + 1) in email_messages:  # Check if a message exists for this email
                message = email_messages[str(i + 1)]
                pool.apply_async(send_email, (recipient_email, i + 1, message))
                email_counter += 1  # Increment the email counter
                counter_label.config(text=f"Emails sent: {email_counter}")  # Update the counter label

        # Close the pool and wait for all processes to complete
        pool.close()
        pool.join()

    print("All emails sent successfully.")

    # Start the Tkinter main loop
    root.mainloop()
