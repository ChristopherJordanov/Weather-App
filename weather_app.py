from streamlit_geolocation import streamlit_geolocation
import requests
from dotenv import load_dotenv
import streamlit as st
import datetime
import pandas as pd
import os

load_dotenv()
API_KEY = os.getenv('OWM_API_KEY')


st.markdown("<h1 style='text-align: center;'>Weather App</h1>", unsafe_allow_html=True)
query_type = st.radio('Choose how to search location data: ', ('Enter city name', 'Use my location'), index=None, horizontal=True)

#The user picks which location to choose
if query_type == 'Enter city name':
    city = st.text_input('Enter city name: ')
else:
    st.write('Press the button bellow button to automatically get your location')
    location = streamlit_geolocation()

units = st.selectbox('Pick a measurement unit', ('metric', 'imperial'))

#The url changes corresponding to the user's choice
if query_type == 'Enter city name' and city:
    current_weather_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units={units}"
    forecast_url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units={units}"
elif query_type == 'Use my location' and location and location.get('latitude') is not None and location.get('longitude') is not None:
    current_weather_url = f"https://api.openweathermap.org/data/2.5/weather?lat={location['latitude']}&lon={location['longitude']}&appid={API_KEY}&units={units}"
    forecast_url = f"https://api.openweathermap.org/data/2.5/forecast?lat={location['latitude']}&lon={location['longitude']}&appid={API_KEY}&units={units}"
else:
    current_weather_url = None
    forecast_url = None


if current_weather_url and forecast_url:
    curr_weather_response = requests.get(current_weather_url)
    forecast_response = requests.get(forecast_url)

    if curr_weather_response.status_code == 200 and forecast_response.status_code == 200:


        #Get and display current weather data
        st.markdown("<h2 style='text-align: center;'>Current weather information:</h2>", unsafe_allow_html=True)
        curr_weather_data = curr_weather_response.json()

        city_name = curr_weather_data['name']
        country = curr_weather_data['sys']['country']
        current_temp = curr_weather_data['main']['temp']
        current_sky_desc = curr_weather_data['weather'][0]['description']
        current_humidity = curr_weather_data['main']['humidity']
        current_wind_spd = curr_weather_data['wind']['speed']
        sunrise = curr_weather_data['sys']['sunrise']
        sunset = curr_weather_data['sys']['sunset']

        #Get the icon corresponding to the weather
        for curr_weather_icon in curr_weather_data['weather']:
            current_weather_icon = curr_weather_icon['icon']

            st.markdown(f"<h3 style='text-align: center;'>{city_name} - {country}</h3>", unsafe_allow_html=True)
            st.markdown(
                f"""
                <div style="display: flex; justify-content: center; align-items: center;">
                    <img src="http://openweathermap.org/img/w/{current_weather_icon}.png" width="80">
                </div>
                """,
                unsafe_allow_html=True
            )

        a, b = st.columns([1, 2])
        c, d, e = st.columns(3)

        def temp_to_color(column_name, temp_type):
            if units == 'metric':
                if temp_type < 15:
                    column_name.metric("Temperature", f"{temp_type} °C", delta="Cold", delta_color="normal", border=True)
                elif temp_type < 30:
                    column_name.metric("Temperature", f"{temp_type} °C", delta="Moderate", delta_color="normal", border=True)
                else:
                    column_name.metric("Temperature", f"{temp_type} °C", delta="Hot", delta_color="normal", border=True)
            elif units == 'imperial':
                if temp_type < 59:
                    column_name.metric("Temperature", f"{temp_type} °F", delta="Cold", delta_color="normal", border=True)
                elif temp_type < 86:
                    column_name.metric("Temperature", f"{temp_type} °F", delta="Moderate", delta_color="normal", border=True)
                else:
                    column_name.metric("Temperature", f"{temp_type} °F", delta="Hot", delta_color="normal", border=True)

        temp_to_color(a, current_temp)
        b.metric(f"Sky description", f"{current_sky_desc}", delta='Sky description', delta_color='off', border=True, label_visibility='hidden')
        c.metric(f"Humidity", f"{current_humidity} %", border=True)
        d.metric(f"Wind speed", f"{current_wind_spd} {'m/s' if units == 'metric' else 'mph'}", border=True)
        timezone_offset = curr_weather_data['timezone']

        # Convert Unix time to the city's local time using timezone-aware objects
        sunrise_time = (datetime.datetime.fromtimestamp(sunrise, datetime.timezone.utc) + datetime.timedelta(
            seconds=timezone_offset)).strftime('%H:%M')
        sunset_time = (datetime.datetime.fromtimestamp(sunset, datetime.timezone.utc) + datetime.timedelta(
            seconds=timezone_offset)).strftime('%H:%M')

        e.metric(f"Daylight hours", f"{sunrise_time} - {sunset_time}", border=True)

        #Get and display forecast data
        forecast_data = forecast_response.json()
        st.markdown("<h2 style='text-align: center;'>Forecast for the next 5 days:</h2>", unsafe_allow_html=True)
        time_of_day = st.selectbox('Pick a time of the day', ('06:00', '09:00', '12:00', '15:00', '18:00', '21:00'), index=None, placeholder='Please select a time of the day')
        date_data = []
        temp_data = []
        for forecast in forecast_data['list']:
            forecast_day = forecast['dt_txt']
            forecast_temp = forecast['main']['temp']
            forecast_sky_desc = forecast['weather'][0]['description']
            forecast_humidity = forecast['main']['humidity']
            forecast_wind_spd = forecast['wind']['speed']

            if time_of_day == forecast_day[11:16]:
                date_data.append({'Date': forecast_day[:10]})
                temp_data.append({'Temperature': forecast_temp})

                # Get the icon corresponding to the weather
                for frc_weather_icon in forecast['weather']:
                    forecast_weather_icon = frc_weather_icon['icon']
                    st.divider()
                    st.markdown(f"<h3 style='text-align: center;'>{forecast_day[:16]}</h3>", unsafe_allow_html=True)
                    st.markdown(
                        f"""
                        <div style="display: flex; justify-content: center; align-items: center;">
                            <img src="http://openweathermap.org/img/w/{forecast_weather_icon}.png" width="80">
                        </div>
                        """,
                        unsafe_allow_html=True
                    )
                w, x = st.columns([1, 2])
                y, z = st.columns(2)
                temp_to_color(w, forecast_temp)
                x.metric(f"Sky description", f"{forecast_sky_descgit }", delta='Sky description', delta_color='off', border=True, label_visibility='hidden')
                y.metric(f"Humidity", f"{forecast_humidity} %", border=True)
                z.metric(f"Wind speed", f"{current_wind_spd} {'m/s' if units == 'metric' else 'mph'}", border=True)

        st.divider()
        st.markdown(f"<h2 style='text-align: center;'>Line chart of the temperatures for the following 5 days</h2>", unsafe_allow_html=True)

        #Make a line chart of the temperatures for the following 5 days.
        if date_data and temp_data:
            combined_data = [{'Date': date['Date'], 'Temperature': temp['Temperature']} for date, temp in zip(date_data, temp_data)]
            df = pd.DataFrame(combined_data)
            df['Date'] = pd.to_datetime(df['Date']).dt.strftime('%a-%d')
            df.set_index('Date', inplace=True)

            st.line_chart(df['Temperature'], x_label='Dates', y_label='Temperatures', use_container_width=True)

    else:
        st.error('City not found. Please try again.')



