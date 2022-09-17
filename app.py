import streamlit as st
import requests, json

st.markdown(
    """
    <style>
        header, footer{
            visibility: hidden;
        }
        .css-1kyxreq.etr89bj2{
            display: flex;
            justify-content: center;
        }
    </style>
    # Weather Application
    """, unsafe_allow_html=True
)

API_KEY = "4d5a661d7871bde4c7b3e984293da731"
base_url = "http://api.openweathermap.org/data/2.5/weather?"
icon_url = "http://openweathermap.org/img/wn/{}@2x.png"


with st.container():
    city = st.text_input("Enter city name: ")

with st.container():
    if city:
        complete_url = f"{base_url}appid={API_KEY}&q={city}"

        res = requests.get(complete_url)
        json = res.json()
        if json["cod"] != "404":
            weather = json["weather"]
            weather_description = weather[0]["description"]
            weather_icon = weather[0]["icon"]
            main = json["main"]
            temperature = round((main["temp"] - 273.15))
            feels_like = round((main["feels_like"] - 273.15))
            status = weather[0]["main"]

            st.image(icon_url.format(weather_icon), caption=weather_description) 
            st.info(f"Status: {status}")
            st.info(f"Temperature: {temperature}°C")
            st.info(f"Feels Like: {feels_like}°C")
        else:
            st.error("City not found")

        