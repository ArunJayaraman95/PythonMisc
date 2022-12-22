CELL_EMAIL = "2482668138@tmomail.net"
PASSWORD = "ktisdqxxyvcvgnwt"
MAIN_EMAIL = "riparun.aj@gmail.com"

import smtplib
from email.message import EmailMessage

# load_dotenv()
def sendText(subject, body):
    msg = EmailMessage()
    msg.set_content(body)
    msg['subject'] = subject
    msg['to'] = CELL_EMAIL
    msg['from'] = MAIN_EMAIL

    #msg.add_attachment(file_data, maintype="image", subtype=file_type,filename="TestSkull")

    user = MAIN_EMAIL
    password = PASSWORD

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(user, password)
    server.send_message(msg)
    print("Sent text!")
    server.quit()

if __name__ == '__main__':
    sendText("Daily Update", "\nLaptop: This is Arun the cool guy")
    print("Sentd text!")

# TODO: Weather
# TODO: Stock Changes
# TODO: Anime Quotes