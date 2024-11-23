from flask import Flask
from flask import render_template
import csv


def read_hostel_data_from_csv(csv_filename):
    hostel_data = []
    with open(csv_filename, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            row['position'] = list(map(float, row['position'].split(',')))
            hostel_data.append(row)
    return hostel_data


csv_filename = 'Hostel_Data.csv'
hostel_data = read_hostel_data_from_csv(csv_filename)

landmark_data = [
    {"position": [15.3926, 73.8803], "name": "Academic Block",
     "description": "Solar Panel: 15.78% efficiency, 20kW capacity, 33.16kW output"},
]

app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template('index.html', hostels=hostel_data, landmarks=landmark_data)


if __name__ == "__main__":
    app.run(debug=True)
