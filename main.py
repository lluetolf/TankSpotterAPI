from flask import Flask, jsonify, request, render_template
import os
from flask_cors import CORS

from InvalidUsage import InvalidUsage
from services.SpottingsRepository import SpottingsRepository

app = Flask(__name__)
CORS(app)


srv = os.getenv("TANKSPOTTER_MONGO")
TankSpotterDB = SpottingsRepository(srv)

@app.errorhandler(InvalidUsage)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response

#
# Static page
#
@app.route('/')
def index():
    return "TankSpotterAPI"


@app.route("/spottings", methods=['GET'])
def get_all_spottings() -> str:
    all_spottings = TankSpotterDB.read_all()
    for spotting in all_spottings:
        spotting['created'] = spotting['created'].isoformat()
        spotting['spotTime'] = spotting['spotTime'].isoformat()   
    return jsonify(all_spottings), 200


@app.route("/spottings", methods=['POST'])
def add_spotting() -> str:
    try:
        spotting = TankSpotterDB.create(request.json)
        return jsonify(spotting), 200
    except Exception as e:
        return jsonify({"message": "Error creating a new field."}), 400

#
#
# Run App
#
#
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
