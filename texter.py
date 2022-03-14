import os
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv

load_dotenv()
def sendText(subject, body):
    msg = EmailMessage()
    msg.set_content(body)
    msg['subject'] = subject
    msg['to'] = os.getenv('CELL_EMAIL')
    msg['from'] = os.getenv('MAIN_EMAIL')

    user = os.getenv('MAIN_EMAIL')
    password = os.getenv('EMAIL_APP_PASSWORD')

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(user, password)
    server.send_message(msg)
    print("Sent text!")
    server.quit()

if __name__ == '__main__':
    sendText("Daily Update", "\nHi Arun\nHere's your daily update!")
