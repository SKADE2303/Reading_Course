from flask import Flask
from flask import render_template

app = Flask(__name__)

hostel_data = [
    {"position": [15.3921, 73.8785], "name": "AH1", "description": "Solar Panel: 22.61% efficiency, 6kW capacity, 1.36kW output"},
    {"position": [15.3919, 73.8782], "name": "AH2", "description": "Solar Panel: 24.67% efficiency, 10kW capacity, 2.47kW output"},
    {"position": [15.391, 73.8772], "name": "AH3", "description": "Solar Panel: 21.02% efficiency, 10kW capacity, 2.1kW output"},
    {"position": [15.3907, 73.87687], "name": "AH4", "description": "Solar Panel: 23.33% efficiency, 13kW capacity, 3.03kW output"},
    {"position": [15.3903, 73.87655], "name": "AH5", "description": "Solar Panel: 18.12% efficiency, 9kW capacity, 1.63kW output"},
    {"position": [15.39, 73.8762], "name": "AH6", "description": "Solar Panel: 19.93% efficiency, 8kW capacity, 1.59kW output"},
    {"position": [15.392, 73.87773], "name": "AH7", "description": "Solar Panel: 18.07% efficiency, 10kW capacity, 1.81kW output"},
    {"position": [15.3915, 73.87718], "name": "AH8", "description": "Solar Panel: 15.78% efficiency, 20kW capacity, 3.16kW output"},
    {"position": [15.38975, 73.876], "name": "AH9", "description": "Solar Panel: 18.60% efficiency, 18kW capacity, 3.35kW output"},
    {"position": [15.3898, 73.8795], "name": "CH7", "description": "Solar Panel: 19.62% efficiency, 20kW capacity, 3.92kW output"}
]

landmark_data = [
    {"position": [15.3926, 73.8803], "name": "Academic Block",
     "description": "Solar Panel: 15.78% efficiency, 20kW capacity, 33.16kW output"},
]


@app.route("/")
def hello_world():
    return render_template('index.html', hostels=hostel_data, landmarks=landmark_data)


if __name__ == "__main__":
    app.run(debug=True)
