from config import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False, unique=True)
    email = db.Column(db.String, nullable=False, unique=True)

    def to_json(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email
        }

class Ride(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False)
    start_location = db.Column(db.String, nullable=False)
    destination = db.Column(db.String, nullable=False)
    start_time = db.Column(db.DateTime, nullable=False)
    end_time = db.Column(db.DateTime, nullable=False)
    price = db.Column(db.Float, nullable=False)
    car = db.Column(db.String, nullable=False)
    is_offer = db.Column(db.Boolean, nullable=False)

    def to_json(self):
        return {
            'id': self.id,
            'username': self.username,
            'start_location': self.start_location,
            'destination': self.destination,
            'start_time': self.start_time.isoformat(),
            'end_time': self.end_time.isoformat(),
            'price': self.price,
            'car': self.car,
            'is_offer': self.is_offer
        }
