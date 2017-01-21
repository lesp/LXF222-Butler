from gpiozero import MotionSensor
import feedparser
import time
from gtts import gTTS
import os
import pyowm

news = feedparser.parse("http://feeds.bbci.co.uk/news/rss.xml?edition=uk")
pir = MotionSensor(17)

while True:
    status = pir.wait_for_inactive()
    if status == True:

        current_time = time.ctime()
        str(current_time)
        tts = gTTS(text=(current_time), lang='en-us')
        tts.save("time.mp3")
        os.system("mpg321 time.mp3")

        for i in range(5):
            tts = gTTS(text=(news['entries'][i]['title']), lang='en-us')
            tts.save("news.mp3")
            os.system("mpg321 news.mp3")


        owm = pyowm.OWM('77bcfa639fe392ddcdcf102938a2d3b5')
        observation = owm.weather_at_place("Blackpool,uk")
        w = observation.get_weather()

        weather = w.get_status()
        tts = gTTS(text=("The current weather is, "+str(weather)), lang='en-us')
        tts.save("weather.mp3")
        os.system("mpg321 weather.mp3")

        temperature = w.get_temperature('celsius')['temp_max']
        tts = gTTS(text=("The current temperature is, "+str(temperature)+"celsius"), lang='en-us')
        tts.save("temperature.mp3")
        os.system("mpg321 temperature.mp3")
