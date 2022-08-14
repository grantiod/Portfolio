from tkinter import Entry, Button, Label, Tk, W, E, N, S, mainloop
import requests
import json

class Weather:
    def __init__(self):
        self.WEATHER_API_KEY = "5711fdcec2171844b445fb2bc3a15f7c"
        self.root = Tk()
        self.root.title("Weather App")
        self.root.geometry("600x300")
        self.zip_entry = Entry(self.root)
        self.zip_entry.grid(row=0, column=0, sticky=W+E+N+S, padx=5)
        self.zip_button = Button(self.root, text="Lookup Zipcode", command=self.zipLookup)
        self.zip_button.grid(row=0, column=1, sticky=W+E+N+S, padx=5)

    # URL's:
    # https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=21204&distance=5&API_KEY=F13BA867-EB7C-4EFC-B552-277B9AC861CC
    # https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}
    # https://api.openweathermap.org/data/2.5/weather?lat=39&lon=76&appid=5711fdcec2171844b445fb2bc3a15f7c

    # create zipLookup function
    def zipLookup(self):
        try:
            # air quality api request
            self.air_api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + self.zip_entry.get() + "&distance=5&API_KEY=F13BA867-EB7C-4EFC-B552-277B9AC861CC")
            self.air_api = json.loads(self.air_api_request.content)
            self.city = self.air_api[0]['ReportingArea']
            self.air_quality = self.air_api[0]['AQI']
            self.air_category = self.air_api[0]['Category']['Name']
            self.lat = self.air_api[0]['Latitude']
            self.lon = self.air_api[0]['Longitude']

            # weather api request
            self.weather_api_request = requests.get("https://api.openweathermap.org/data/2.5/weather?lat=" + str(self.lat) + "&lon=" + str(self.lon) + "&appid=" + self.WEATHER_API_KEY)
            self.weather_api = json.loads(self.weather_api_request.content)
            self.weather = self.weather_api['weather'][0]['main']
            self.weather_description = self.weather_api['weather'][0]['description']
            self.temperature = self.weather_api['main']['temp'] # stores in kelvin
            self.temperature = (self.temperature * 1.8) - 459.67 # convert to fahrenheit
            self.temperature = round(self.temperature, 2) # round to nearest second digit
            self.wind_speed = self.weather_api['wind']['speed']
            self.humidity = self.weather_api['main']['humidity']

            if self.air_category == "Good":
                self.weather_color = "#0C0"
            elif self.air_category == "Moderate":
                self.weather_color = "#FFFF00"
            elif self.air_category == "Unhealthy for Sensitive Groups":
                self.weather_color = "#ff9900"
            elif self.air_category == "Unhealthy":
                self.weather_color = "#FF0000"
            elif self.air_category == "Very Unhealthy":
                self.weather_color = "#99066"
            elif self.air_category == "Hazardous":
                self.weather_color = "#660000"

            self.root.configure(background=self.weather_color)
            self.air_lbl = Label(self.root, text=self.city + " Air Quality " + str(self.air_quality) + " " + self.air_category, font=("Helvetica", 20), background=self.weather_color)
            self.air_lbl.grid(row=1, column=0, sticky=W+E)
            self.weather_lbl = Label(self.root, text=self.weather + " - " + self.weather_description, font=("Helvetica", 20), background=self.weather_color)
            self.weather_lbl.grid(row=2, column=0, sticky=W+E)
            self.temperature_lbl = Label(self.root, text=str(self.temperature) + " Degrees", font=("Helvetica", 20), background=self.weather_color)
            self.temperature_lbl.grid(row=3, column=0, sticky=W+E)
            self.wind_speed_lbl = Label(self.root, text='Wind Speed ' + str(self.wind_speed), font=("Helvetica", 20), background=self.weather_color)
            self.wind_speed_lbl.grid(row=4, column=0, sticky=W+E)
            self.humidity_lbl = Label(self.root, text='Humidity ' + str(self.humidity), font=("Helvetica", 20), background=self.weather_color)
            self.humidity_lbl.grid(row=5, column=0, sticky=W+E)
        except (Exception):
            return
    
    def run(self):
        mainloop()