from texter import sendText
import os, time, requests
from dotenv import load_dotenv
import datetime as dt

load_dotenv()
def getAnime() -> tuple[str, str, str]:
    """Returns tuple of anime character, show, and then
    random quote"""
    anime_url = "https://animechan.vercel.app/api/random"
    data = requests.get(anime_url).json()
    character = data['character']
    quote = data['quote']
    anime = data['anime']
    # sendText("Anime Quote")
    return character, anime, quote

def getWeather() -> str:
    """Returns string containing temperature,
    feel like temp, high and low for Detroit"""
    WEATHER_API = os.getenv('WEATHER_API_KEY')
    def KtoF(x):
        return str(round(1.8*x-459.67))
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
    URL = BASE_URL + "q=" + "Detroit" + "&appid=" + WEATHER_API
    response = requests.get(URL)
    if response.status_code == 200:
        data = response.json()
        main = data['main']
        temp = KtoF(main['temp'])
        feelsLike = KtoF(main['feels_like'])
        highTemp, lowTemp = KtoF(main['temp_max']), KtoF(main['temp_min'])

        tempString = f"\nDetroit Weather:\nCurrent Temp: {temp}\
            \nFeels Like: {feelsLike}\
            \nHigh: {highTemp}    Low: {lowTemp}"
        # sendText("Detroit Weather", tempString)
        return tempString
        
    else:
        print("Error in HTTP request")

def getDate() -> str:
    """Returns current date in MM/DD/YYYY format"""
    date = dt.datetime.now()
    return f"{date.month}/{date.day}/{date.year}"

def getHour() -> int:
    """Returns current hour"""
    return dt.datetime.now().hour

def getMinute() -> int:
    return dt.datetime.now().minute


getAnime()

aChar = ""
aShow = ""
aString = ""
# print(aChar, aShow, aString)
while True:
    if getHour() == 8 and getMinute() == 0:
        a = getAnime()
        aChar, aShow, aString = a[0], a[1], a[2]
        subject = f"{getDate()[:-5]} Update!"
        weatherString = getWeather()
        finalMsg = weatherString + "\n\n" + \
            "Daily anime quote:\n" + aString + \
            "\n\nHave an awesome day!"
        sendText(subject, finalMsg)
    if getHour() == 11 and getMinute() == 0:
        sendText("Anime Answer", f"\nToday's anime quote was said by {aChar} from the anime {aShow}")
    time.sleep(60)
        #sendText(subject, finalMsg)