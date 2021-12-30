from tkinter import *
import requests
import json
import sys

if (len(sys.argv) == 2):
    zip = sys.argv[1]
else:
    print('No zipcode entered')
    exit()

root = Tk()
root.title('Air Quality Info')
root.geometry("440x25")

try:
    address = "https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + zip + "&distance=5&API_KEY=B55A7332-8E1B-4F17-84CC-557B195AF970"
    api_r = requests.get(address)
    api = json.loads(api_r.content)
    city = api[0]['ReportingArea']
    quality = api[0]['AQI']
    category = api[0]['Category']['Name']
    if quality > 0 and quality <= 50:
        color = 'green'
    elif quality > 50 and quality <= 100:
        color = 'yellow'
        fontc = 'black'
    elif quality > 100  and quality <= 150:
        color = 'orange'
    elif quality > 150  and quality <= 200:
        color = 'red'
    elif quality > 200  and quality <= 300:
        color = 'purple'
    elif quality > 300:
        color = '#660000'
    root.configure(bg = color)

    label = Label(root, text = city + ": Air Quality -- " + str(quality) + " " + category, font = ("Courier", 15), bg = color)
    label.pack()
except Exception as x:
    api = "Error.."

root.mainloop()
