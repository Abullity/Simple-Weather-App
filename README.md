# Simple-Weather-App
A simple python backend project inspired by one of JetBrains Academy projects.

[Hosted on Heroku](https://simplesweatherapp.herokuapp.com/)

Frontend styles as well as basic idea comes from JetBrains Academy,
logic/backend of the app is provided by me with the help of Flask framework


# What does the app do

App takes existing city name as an input and generates a card of a given city with:

  • temperature
  
  • colloqual description of the temperature
  
  • background image which correlates to local time of the city
  
  
All the generated cards will be saved in a sqlite database,
so they should be there after termination and relaunch of the program

You could also delete a city card which is no longer needed and it'll also be deleted from the database

Everytime you refresh the page or add/delete a card, data of every saved card will also be updated 

for more info on OpenWeatherAPI, visit: 
https://openweathermap.org/current


# Installation and dependencies

App uses Flask as the backend framework

The required modules (Including Flask and Flask_Sqlalchemy) are given in requirements.txt file,
which was generated by 'pip freeze' command.

To install required modules run 'pip -r requirements.txt' command from project's root directory

App also uses data from OpenWeatherApi, which is essential to run the app,
so in order to get a valid API key,
you must register at https://home.openweathermap.org/users/sign_up


Once you get your API key, assign your API key to API_KEY variable on line 41 in WeatherApp/helpers.py  

After you have every package installed and API_KEY variable assign with valid key, execute run.py file, the rest should work without issues.

# Running the app

Open terminal in project's root directory and run the following command 

"python run.py"

or 

"python3 run.py"

The command takes two arguments host address and port, you don't have to specify these and by default the app will be run on
localhost port 5000  --->  http://127.0.0.1:5000/

