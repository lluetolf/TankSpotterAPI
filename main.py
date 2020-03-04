from flask import Flask, jsonify, request, render_template
import os

from InvalidUsage import InvalidUsage
from services.SpottingsRepository import SpottingsRepository

app = Flask(__name__)
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
    return jsonify(all_spottings), 200


#
#
# Run App
#
#
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
