# Import Libraries

import streamlit as st 
import requests

# def get_pred(arr):
#     params ={ {x:x for x in arr}
    # try:
    #     r = requests.post("http://127.0.0.1:5000/get_text_analysis", params=params, timeout=5000)
    #     return r.content
    # except Exception as e:
    #     print(e)

dict_names = [
            "Start_Lat",
            "Start_Lng",
            "End_Lat",
            "End_Lng",
            "Distance",
            "Street",
            "Side",
            "City",
            "County",
            "State",
            "Zipcode",
            "Country",
            "Timezone",
            "Airport_Code",
            "Weather_Timestamp",
            "Temperature",
            "Wind_Chill",
            "Humidity",
            "Pressure",
            "Visibility",
            "Wind_Direction",
            "Wind_Speed",
            "Precipitation",
            "Weather_Condition",
            "Amenity",
            "Bump",
            "Crossing",
            "Give_Way",
            "Junction",
            "No_Exit",
            "Railway",
            "Roundabout",
            "Station",
            "Stop",
            "Traffic_Calming",
            "Traffic_Signal",
            "Turning_Loop",
            "Sunrise_Sunset",
            "Civil_Twilight",
            "Nautical_Twilight",
            "Astronomical_Twilight"
        ]

def get_pred(arr):
    params = {y:x for x,y in list(zip(arr, dict_names))}
    print(params)
    try:
        r = requests.post("http://127.0.0.1:5000/predict", params=params, timeout=5000)
        # return r.content
    except Exception as e:
        print(e)
    return r.json()["severity"]

def main():
    """
        Vehicle Accident Severity Predictor App
    """

    st.title("Vehicle Accident Severity Predictor")
    html_temp = """
    <div style="background-color:green;padding:10px">
    <h2 style="color:white;text-align:center;">Dashboard</h2>
    </div>
    <br>
    """
    st.markdown(html_temp,unsafe_allow_html=True)

    Start_Lat = st.text_input("Enter Starting Latitude","Type Here")
    Start_Lng = st.text_input("Enter Starting Longitude","Type Here")
    End_Lat = st.text_input("Enter End Latitude","Type Here")
    End_Lng = st.text_input("Enter End_Lng","Type Here")
    Distance = st.text_input("Enter Distance(mi)","Type Here")
    Street = st.text_input("Enter Street","Type Here")
    Side = st.text_input("Enter Side","Type Here")
    City = st.text_input("Enter City","Type Here")
    County = st.text_input("Enter County","Type Here")
    State = st.text_input("Enter State","Type Here")
    Zipcode = st.text_input("Enter Zipcode","Type Here")
    Country = st.text_input("Enter Country","Type Here")
    Timezone = st.text_input("Enter Timezone","Type Here")
    Airport_Code = st.text_input("Enter Airport_Code","Type Here")
    Weather_Timestamp = st.text_input("Enter Weather_Timestamp","Type Here")
    Temperature = st.text_input("Enter Temperature(F)","Type Here")
    Wind_Chill = st.text_input("Enter Wind_Chill(F)","Type Here")
    Humidity = st.text_input("Enter Humidity(%)","Type Here")
    Pressure = st.text_input("Enter Pressure(in)","Type Here")
    Visibility = st.text_input("Enter Visibility(mi)","Type Here")
    Wind_Direction = st.text_input("Enter Wind_Direction","Type Here")
    Wind_Speed = st.text_input("Enter Wind_Speed(mph)","Type Here")
    Precipitation = st.text_input("Enter Precipitation(in)","Type Here")
    Weather_Condition = st.text_input("Enter Weather_Condition","Type Here")
    Amenity = st.text_input("Enter Amenity","Type Here")
    Bump = st.text_input("Enter Bump","Type Here")
    Crossing = st.text_input("Enter Crossing","Type Here")
    Give_Way = st.text_input("Enter Give_Way","Type Here")
    Junction = st.text_input("Enter Junction","Type Here")
    No_Exit = st.text_input("Enter No_Exit","Type Here")
    Railway = st.text_input("Enter Railway","Type Here")
    Roundabout = st.text_input("Enter Roundabout","Type Here")
    Station = st.text_input("Enter Station","Type Here")
    Stop = st.text_input("Enter Stop","Type Here")
    Traffic_Calming = st.text_input("Enter Traffic_Calming","Type Here")
    Traffic_Signal = st.text_input("Enter Traffic_Signal","Type Here")
    Turning_Loop = st.text_input("Enter Turning_Loop","Type Here")
    Sunrise_Sunset = st.text_input("Enter Sunrise_Sunset","Type Here")
    Civil_Twilight = st.text_input("Enter Civil_Twilight","Type Here")
    Nautical_Twilight = st.text_input("Enter Nautical_Twilight","Type Here")
    Astronomical_Twilight = st.text_input("Enter Astronomical_Twilight","Type Here")

    if st.button("Predict"):
        result = get_pred([
            Start_Lat,
            Start_Lng,
            End_Lat,
            End_Lng,
            Distance,
            Street,
            Side,
            City,
            County,
            State,
            Zipcode,
            Country,
            Timezone,
            Airport_Code,
            Weather_Timestamp,
            Temperature,
            Wind_Chill,
            Humidity,
            Pressure,
            Visibility,
            Wind_Direction,
            Wind_Speed,
            Precipitation,
            Weather_Condition,
            Amenity,
            Bump,
            Crossing,
            Give_Way,
            Junction,
            No_Exit,
            Railway,
            Roundabout,
            Station,
            Stop,
            Traffic_Calming,
            Traffic_Signal,
            Turning_Loop,
            Sunrise_Sunset,
            Civil_Twilight,
            Nautical_Twilight,
            Astronomical_Twilight
        ])

        st.success('Predicted Severity is Class {}'.format(result[0]))

    if st.button("About"):
        st.text("Built with Streamlit & ♥")


if __name__ == '__main__':
	main()