from flask import Flask
from flask import render_template
import csv


def data_from_csv(csv_filename):
    data = []
    with open(csv_filename, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            row['position'] = list(map(float, row['position'].split(',')))
            data.append(row)
    return data


hostel_data = data_from_csv('Hostel_Data.csv')

landmark_data = data_from_csv('Landmark_Data.csv')

app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template('index.html', hostels=hostel_data, landmarks=landmark_data)


if __name__ == "__main__":
    app.run(debug=True)
