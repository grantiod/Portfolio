from tkinter import Entry, Button, Label, Tk, W, E, N, S, mainloop
import requests
import json

class AirQuality:
    def __init__(self):
        self.root = Tk()
        self.root.title("Weather App")
        self.root.geometry("600x200")
        self.zip_entry = Entry(self.root)
        self.zip_entry.grid(row=0, column=0, sticky=W+E+N+S, padx=5)
        self.zip_button = Button(self.root, text="Lookup Zipcode", command=self.zipLookup)
        self.zip_button.grid(row=0, column=1, sticky=W+E+N+S, padx=5)

        # URL:
        # https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=21204&distance=5&API_KEY=F13BA867-EB7C-4EFC-B552-277B9AC861CC

    # create zipLookup function
    def zipLookup(self):
        try:
            # air quality api request
            self.air_api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + self.zip_entry.get() + "&distance=5&API_KEY=F13BA867-EB7C-4EFC-B552-277B9AC861CC")
            # print('requesting api')
            self.air_api = json.loads(self.air_api_request.content)
            self.city = self.air_api[0]['ReportingArea']
            self.air_quality = self.air_api[0]['AQI']
            self.air_category = self.air_api[0]['Category']['Name']

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
        except (Exception):
            return

    def run(self):
        mainloop()