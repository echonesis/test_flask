from flask import Flask, render_template, request, g
from flask import jsonify
import sqlite3
import os
app = Flask(__name__)
port = int(os.environ.get("PORT", 5000))

# 
SQLITE_DB_PATH = "members.db"

# test data
tpe = {
    "id": 0,
    "city_name": "Taipei",
    "country_name": "Taiwan",
    "is_capital": True,
    "location": {
        "longitude": 121.569649,
        "latitude": 25.036786
    }
}
nyc = {
    "id": 1,
    "city_name": "New York",
    "country_name": "United States",
    "is_capital": False,
    "location": {
        "longitude": -74.004364,
        "latitude": 40.710405
    }
}
ldn = {
    "id": 2,
    "city_name": "London",
    "country_name": "United Kingdom",
    "is_capital": True,
    "location": {
        "longitude": -0.114089,
        "latitude": 51.507497
    }
}
cities = [tpe, nyc, ldn]

test_sample = {
  "center_location": [
    13.24,
    14.24
  ],
  "zoomin": 2,
  "map_marker_list": [{
    "location": [
      23.13,
      23.32
    ],
    "marker_type": 1,
    "marker_color": "#2F0000",
    "marker_size": 2,
    "plan_day": 1,
    "plan_order": 1
  }, {
    "location": [
      23.13,
      23.32
    ],
    "marker_type": 1,
    "marker_color": "#2F0000",
    "marker_size": 2,
    "plan_day": 1,
    "plan_order": 2
  }, {
    "location": [
      23.13,
      23.32
    ],
    "marker_type": 1,
    "marker_color": "#2F0000",
    "marker_size": 2,
    "plan_day": 1,
    "plan_order": 3
  }],
  "day_filter_list": [
    {
      "status": 1,
      "ref_map_marker": 3,
      "type": 1,
      "color": "#2F0000",
      "size": 1,
      "order": 1
    },
    {
      "status": 1,
      "ref_map_marker": 3,
      "type": 1,
      "color": "#2F0000",
      "size": 1,
      "order": 2
    },
    {
      "status": 1,
      "ref_map_marker": 3,
      "type": 1,
      "color": "#2F0000",
      "size": 1,
      "order": 3
    }
  ]
}

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(SQLITE_DB_PATH)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close() 

@app.route('/', methods=['GET'])
def hello_world():
    return '<h1>Flask GET test!</h1>'

@app.route('/cities/all', methods=['GET'])
def cities_all():
    return jsonify(cities)

@app.route('/api/planner/getuuid', methods=['GET'])
def getuuid():
    uuid = request.args.get('uuid')
    print(uuid)
    if uuid == "59487408":
        return jsonify(test_sample)
    else:
        return '<h1>Not valid uuid!</h1>'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=port)

