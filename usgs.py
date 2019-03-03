import requests
import datetime
from datetime import timedelta

USGS_URL = 'https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime='
currentDT = datetime.datetime.today()
enddate = currentDT.date()
date_range = 1 #set how recent the earthquakes are
start = currentDT-datetime.timedelta(days=date_range)
startdate = start.date()
min_magnitude = 5 #set minimum magnitude
min_magnitude = str(min_magnitude)
URL = USGS_URL+str(startdate)+'&endtime='+str(enddate)+'&minmagnitude='+min_magnitude
req = requests.get(URL)
res = req.json()

quakes = []
for i in range(len(res['features'])):
	quake = {}
	quake_id = res['features'][i]['id']
	quake['location'] = res['features'][i]['geometry']['coordinates']
	quake['place'] = res['features'][i]['properties']['place']
	quake['time_zone'] = res['features'][i]['properties']['tz']
	print(quake['time_zone'])
	quake['title'] = res['features'][i]['properties']['title']
	quake['status'] = res['features'][i]['properties']['status']
	quake['url'] = res['features'][i]['properties']['url']
	
	quakes.append(quake)
print(quakes)

