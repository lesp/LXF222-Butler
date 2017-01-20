import feedparser
from gtts import gTTS
import os
import pyowm
news = feedparser.parse("http://feeds.bbci.co.uk/news/rss.xml?edition=uk")
stories = []

print(news['feed']['title'])

for i in range(3):
    tts = gTTS(text=(news['entries'][i]['title']), lang='en-us')
    tts.save("news.mp3")
    os.system("mpg321 news.mp3")


owm = pyowm.OWM('API KEY')
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

print("The current weather is, ",w.get_status())
print("The current temperature is, ",w.get_temperature('celsius')['temp_max']
)
