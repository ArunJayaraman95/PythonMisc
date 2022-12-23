CELL_EMAIL = "2482668138@tmomail.net"
PASSWORD = "ktisdqxxyvcvgnwt"
MAIN_EMAIL = "riparun.aj@gmail.com"

import smtplib, requests
from email.message import EmailMessage
from datetime import date

def getBerserkQuote() -> tuple[str, str, str]:
    """Returns tuple of anime character, show, and then
    random quote"""
    anime_url = "https://animechan.vercel.app/api/random/anime?title=berserk"
    data = requests.get(anime_url).json()
    character = data['character']
    quote = data['quote']
    anime = data['anime']
    # sendText("Anime Quote")
    return character, anime, quote


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
    server.quit()

if __name__ == '__main__':
    currentDate = date.today().strftime("%b-%d-%Y")
    dailyQuote = getBerserkQuote()
    body = f"\nLaptop Notification \
        \n\nBerserk QotD: \
        \n\"{dailyQuote[2]}\" ~ {dailyQuote[0]}"

    sendText(f"Update for {currentDate}", body)
    print("Sent text!")

# TODO: Weather
# TODO: Stock Changes
# TODO: Anime Quotes