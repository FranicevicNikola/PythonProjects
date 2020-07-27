import requests
from pprint import pprint


opuzen = requests.get(
    'http://api.openweathermap.org/data/2.5/weather?zip=20355,hr&appid=5e19fe7d8d441718a20d7adea3506f35&units=metric')

# pprint(opuzen.json())
#print(str(opuzen.json()['main']['temp']) + ' stupnjeva celzijevih')
pprint(str(opuzen.json()['weather'][0]['icon']))
