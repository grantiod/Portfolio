from tkinter import Entry, Button, Label, Tk, W, E, N, S
import requests
import json

WEATHER_API_KEY = "5711fdcec2171844b445fb2bc3a15f7c"

root = Tk()
root.title("Weather App")
root.geometry("600x300")

# URL's:
# https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=21204&distance=5&API_KEY=F13BA867-EB7C-4EFC-B552-277B9AC861CC
# https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}
# https://api.openweathermap.org/data/2.5/weather?lat=39&lon=76&appid=5711fdcec2171844b445fb2bc3a15f7c

# create zipLookup function
def zipLookup():
    # zip_lbl = Label(root, text=zip.get())
    # zip_lbl.grid(row=1, column=0, columnspan=2)

    try:
        # air quality api request
        air_api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + zip_entry.get() + "&distance=5&API_KEY=F13BA867-EB7C-4EFC-B552-277B9AC861CC")
        air_api = json.loads(air_api_request.content)
        city = air_api[0]['ReportingArea']
        air_quality = air_api[0]['AQI']
        air_category = air_api[0]['Category']['Name']
        lat = air_api[0]['Latitude']
        lon = air_api[0]['Longitude']

        # weather api request
        weather_api_request = requests.get("https://api.openweathermap.org/data/2.5/weather?lat=" + str(lat) + "&lon=" + str(lon) + "&appid=" + WEATHER_API_KEY)
        weather_api = json.loads(weather_api_request.content)
        weather = weather_api['weather'][0]['main']
        temperature = weather_api['main']['temp'] # stores in kelvin
        temperature = (temperature * 1.8) - 459.67 # convert to fahrenheit
        temperature = round(temperature, 2) # round to nearest second digit
        wind_speed = weather_api['wind']['speed']
        humidity = weather_api['main']['humidity']

        if air_category == "Good":
            weather_color = "#0C0"
        elif air_category == "Moderate":
            weather_color = "#FFFF00"
        elif air_category == "Unhealthy for Sensitive Groups":
            weather_color = "#ff9900"
        elif air_category == "Unhealthy":
            weather_color = "#FF0000"
        elif air_category == "Very Unhealthy":
            weather_color = "#99066"
        elif air_category == "Hazardous":
            weather_color = "#660000"

        root.configure(background=weather_color)
        air_lbl = Label(root, text=city + " Air Quality " + str(air_quality) + " " + air_category, font=("Helvetica", 20), background=weather_color)
        air_lbl.grid(row=1, column=0, sticky=W+E)
        weather_lbl = Label(root, text=weather, font=("Helvetica", 20), background=weather_color)
        weather_lbl.grid(row=2, column=0, sticky=W+E)
        temperature_lbl = Label(root, text=str(temperature) + " Degrees", font=("Helvetica", 20), background=weather_color)
        temperature_lbl.grid(row=3, column=0, sticky=W+E)
        wind_speed_lbl = Label(root, text='Wind Speed ' + str(wind_speed), font=("Helvetica", 20), background=weather_color)
        wind_speed_lbl.grid(row=4, column=0, sticky=W+E)
        humidity_lbl = Label(root, text='Humidity ' + str(humidity), font=("Helvetica", 20), background=weather_color)
        humidity_lbl.grid(row=5, column=0, sticky=W+E)

    except Exception as e:
        print("Error...")

zip_entry = Entry(root)
zip_entry.grid(row=0, column=0, sticky=W+E+N+S, padx=5)
zip_button = Button(root, text="Lookup Zipcode", command=zipLookup)
zip_button.grid(row=0, column=1, sticky=W+E+N+S, padx=5)

root.mainloop()