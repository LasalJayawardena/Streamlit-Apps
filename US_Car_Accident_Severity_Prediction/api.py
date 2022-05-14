import traceback
import numpy as np
from flask import Flask, request, send_file
import json
import pickle


# Iniatlize a Flask app
app = Flask('app')

with open('cat_model.pkl','rb') as f:
    clf = pickle.load(f)

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    return_dict = {}
    if request.method == 'POST':
        try:
            if request.args:
                try:
                    Start_Lat = float(request.args.get("Start_Lat"))
                    Start_Lng = float(request.args.get("Start_Lng"))
                    End_Lat = float(request.args.get("End_Lat"))
                    End_Lng = float(request.args.get("End_Lng"))
                    Distance = request.args.get("Distance")
                    Street = request.args.get("Street")
                    Side = request.args.get("Side")
                    City = request.args.get("City")
                    County = request.args.get("County")
                    State = request.args.get("State")
                    Zipcode = request.args.get("Zipcode")
                    Country = request.args.get("Country")
                    Timezone = request.args.get("Timezone")
                    Airport_Code = request.args.get("Airport_Code")
                    Weather_Timestamp = request.args.get("Weather_Timestamp")
                    Temperature = float(request.args.get("Temperature"))
                    Wind_Chill = float(request.args.get("Wind_Chill"))
                    Humidity = float(request.args.get("Humidity"))
                    Pressure = float(request.args.get("Pressure"))
                    Visibility = float(request.args.get("Visibility"))
                    Wind_Direction = request.args.get("Wind_Direction")
                    Wind_Speed = float(request.args.get("Wind_Speed"))
                    Precipitation = float(request.args.get("Precipitation"))
                    Weather_Condition = request.args.get("Weather_Condition")
                    Amenity = request.args.get("Amenity") == 'True'
                    Bump = request.args.get("Bump") == 'True'
                    Crossing = request.args.get("Crossing") == 'True'
                    Give_Way = request.args.get("Give_Way") == 'True'
                    Junction = request.args.get("Junction") == 'True'
                    No_Exit = request.args.get("No_Exit") == 'True'
                    Railway = request.args.get("Railway") == 'True'
                    Roundabout = request.args.get("Roundabout") == 'True'
                    Station = request.args.get("Station") == 'True'
                    Stop = request.args.get("Stop") == 'True'
                    Traffic_Calming = request.args.get("Traffic_Calming") == 'True'
                    Traffic_Signal = request.args.get("Traffic_Signal") == 'True'
                    Turning_Loop = request.args.get("Turning_Loop") == 'True'
                    Sunrise_Sunset = request.args.get("Sunrise_Sunset")
                    Civil_Twilight = request.args.get("Civil_Twilight")
                    Nautical_Twilight = request.args.get("Nautical_Twilight")
                    Astronomical_Twilight = request.args.get("Astronomical_Twilight")
                except:
                    raise Exception("All args are not properly provided")
            else:
                raise Exception("No args provided")

            feat_Arr = [ Start_Lat, Start_Lng, End_Lat, End_Lng, Distance,
            Street, Side, City, County, State, Zipcode, Country,
            Timezone, Airport_Code, Weather_Timestamp, Temperature,
            Wind_Chill, Humidity, Pressure, Visibility,
            Wind_Direction, Wind_Speed, Precipitation,
            Weather_Condition, Amenity, Bump, Crossing, Give_Way,
            Junction, No_Exit, Railway, Roundabout, Station, Stop,
            Traffic_Calming, Traffic_Signal, Turning_Loop, Sunrise_Sunset,
            Civil_Twilight, Nautical_Twilight, Astronomical_Twilight]

            try:
                pred = clf.predict(feat_Arr)
            except Exception as e:
                print("Model input err")

            return json.dumps({'severity': str(pred[0]), "Status": 200})
        except Exception as e:
            print(e)
            return json.dumps({"Status": 500})
    else:
        return "Predict route"


if __name__ == '__main__':
    app.run()
    # app.run(debug=True)