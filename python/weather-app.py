from tkinter import Entry, Button, Label, Tk, W, E, N, S
import requests
import json

root = Tk()
root.title("Weather App")
root.geometry("600x100")

# URL:
# https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=21204&distance=5&API_KEY=F13BA867-EB7C-4EFC-B552-277B9AC861CC

# create zipLookup function
def zipLookup():
    # zip_lbl = Label(root, text=zip.get())
    # zip_lbl.grid(row=1, column=0, columnspan=2)

    try:
        # returns json file
        api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + zip.get() + "&distance=5&API_KEY=F13BA867-EB7C-4EFC-B552-277B9AC861CC")
        api = json.loads(api_request.content)
        city = api[0]['ReportingArea']
        quality = api[0]['AQI']
        category = api[0]['Category']['Name']

        if category == "Good":
            weather_color = "#0C0"
        elif category == "Moderate":
            weather_color = "#FFFF00"
        elif category == "Unhealthy for Sensitive Groups":
            weather_color = "#ff9900"
        elif category == "Unhealthy":
            weather_color = "#FF0000"
        elif category == "Very Unhealthy":
            weather_color = "#99066"
        elif category == "Hazardous":
            weather_color = "#660000"

        root.configure(background=weather_color)
        lbl = Label(root, text=city + " Air Quality " + str(quality) + " " + category, font=("Helvetica", 20), background=weather_color)
        lbl.grid(row=1, column=0, sticky=W+E)
    except Exception as e:
        api = "Error..."

zip = Entry(root)
zip.grid(row=0, column=0, sticky=W+E+N+S, padx=5)

zip_button = Button(root, text="Lookup Zipcode", command=zipLookup)
zip_button.grid(row=0, column=1, sticky=W+E+N+S, padx=5)

root.mainloop()