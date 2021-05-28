from WeatherApp import db


class City(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), unique=True, nullable=False)
    temp = db.Column(db.Integer, nullable=False)
    temp_verbal = db.Column(db.String(40), nullable=False)
    image = db.Column(db.String(40), nullable=False)

    def __repr__(self):
        return f"{self.id}: {self.name} - {self.temp} C"
