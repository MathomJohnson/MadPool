from flask import request, jsonify
from config import app, db
from models import User, Ride

@app.route("/rides", methods=['GET'])
def get_rides():
    rides = Ride.query.all()
    json_rides = list(map(lambda x: x.to_json(), rides))
    return jsonify({"rides": json_rides})

@app.route("/create_ride", methods=['POST'])
def create_ride():
    username = request.json.get('username')
    start_location = request.json.get('start_location')
    destination = request.json.get('destination')
    start_time = request.json.get('start_time')
    end_time = request.json.get('end_time')
    price = request.json.get('price')
    car = request.json.get('car')
    is_offer = request.json.get('is_offer')

    if not username or not start_location or not destination or not start_time or not price is None:
        return jsonify({"message": "You must include your username, start location, destination, start time, and price."}), 400

    new_ride = Ride(
        username=username,
        start_location=start_location,
        destination=destination,
        start_time=start_time,
        end_time=end_time,
        price=price,
        car=car,
        is_offer=is_offer
    )

    try:
        db.session.add(new_ride)
        db.session.commit()
    except Exception as e:
        return jsonify({"message": str(e)}), 400
    
    return jsonify({"message": "Ride created successfully."}), 201

@app.route("/update_ride/<int:ride_id>", methods=['PATCH'])
def update_ride(ride_id):
    ride = Ride.query.get(ride_id)

    if not ride:
        return jsonify({"message": "Ride not found."}), 404

    data = request.json
    ride.username = data.get('username', ride.username)
    ride.start_location = data.get('start_location', ride.start_location) 
    ride.destination = data.get('destination', ride.destination)
    ride.start_time = data.get('start_time', ride.start_time)
    ride.end_time = data.get('end_time', ride.end_time)
    ride.price = data.get('price', ride.price)
    ride.car = data.get('car', ride.car)
    ride.is_offer = data.get('is_offer', ride.is_offer)

    db.session.commit()

    return jsonify({"message": "Ride updated successfully."})

@app.route("/delete_ride/<int:ride_id>", methods=['DELETE'])
def delete_ride(ride_id):
    ride = Ride.query.get(ride_id)

    if not ride:
        return jsonify({"message": "Ride not found."}), 404

    db.session.delete(ride)
    db.session.commit()

    return jsonify({"message": "Ride deleted successfully."})


if __name__ == '__main__':
    with app.app_context():
        db.create_all()

    app.run(debug=True)