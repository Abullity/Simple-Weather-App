from WeatherApp import app, db
from WeatherApp.models import City
from WeatherApp.helpers import get_weather_data, generate_city, update_city
from flask import request, render_template, redirect, flash


@app.route('/')
def index():
	cities=City.query.all()
	for city in cities:
		update_city(city)
	db.session.commit()
	return render_template('index.html', cities=cities)


@app.route('/add', methods=['POST', 'GET'])
def add_city():
    if request.form and request.form["city_name"]:
        weather_data = get_weather_data(request.form["city_name"])
        
        if weather_data['cod'] == '404':
            flash("The city doesn't exist!")
            return redirect('/')
        elif City.query.filter_by(name=weather_data['name']).first():
            flash("The city has already been added to the list!")
            return redirect('/')
            
        city = generate_city(weather_data)
        db.session.add(city)
        db.session.commit()
    return redirect('/')


@app.route('/delete/<city_id>', methods=['GET'])
def delete(city_id):
    city = City.query.get(city_id)
    db.session.delete(city)
    db.session.commit()
    return redirect('/')
