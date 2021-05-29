import os
import json
import requests
from datetime import datetime, timedelta
from WeatherApp.models import City
    

def get_temp_verbal(temp):
	if temp < 10:
		temp_verbal = 'Cold'
	elif 10 <= temp < 30:
		temp_verbal = 'Moderate'
	else:
		temp_verbal = 'Hot'
	return temp_verbal
	
	
def get_image(timezone_shift):
	local_hours = (datetime.utcnow() + timedelta(seconds=timezone_shift)).hour
	if local_hours < 7:
		image = 'night'
	elif local_hours < 9:
		image = 'evening-morning'
	elif local_hours < 18:
		image = 'day'
	elif local_hours < 22:
		image = 'evening-morning'
	else:
		image = 'night'
	return image 
	

def get_weather_data(city_name):
	# Following API key is taken from my OS's envionment variable
	# For the app to work you must generate 
	# an API key on https://openweathermap.org
	# Once you get your key, change the following variable like so:
	# API_KEY = 'some_random_character_sequence'
	API_KEY = os.environ['OWAPI_KEY']
	# ^
	# | 
	# Change that variable
	data = requests.get(f"""http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}""")
	return json.loads(data.content)

	
def generate_city(weather_data):
	name = weather_data['name']
	# openweather api sends shift in user's timezone in seconds as 'timezone'
	image = get_image(weather_data['timezone'])
	temp = int(weather_data['main']['temp'] - 273.15)
	temp_verbal = get_temp_verbal(temp)
	return City(name=name, temp=temp, temp_verbal=temp_verbal, image=image)
	
	
def update_city(city):
	weather_data = get_weather_data(city.name)
	temp = int(weather_data['main']['temp'] - 273.15)
	city.temp = temp
	city.temp_verbal = get_temp_verbal(temp)
	city.image = get_image(weather_data['timezone'])


