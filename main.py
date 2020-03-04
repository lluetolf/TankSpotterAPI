from flask import Flask, jsonify, request, render_template
import os

from InvalidUsage import InvalidUsage

app = Flask(__name__)
srv = os.getenv("CANAWEB_MONGO")


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


#
#
# Run App
#
#
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
