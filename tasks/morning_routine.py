#The aim of this script is to send me the daily weather report in the morning
#and provide an ETA of my commute to work via Text message SMS
#script is triggered by a cronjob on my EC2 server instance

import requests
import json
import googlemaps
from datetime import datetime
from twilio.rest import Client


def celcius_to_farenheit(celcius):
    return (celcius * 9/5 ) + 32;


def get_commute_eta():
    home_address = "home.."
    work_address = "work.."
    google_maps_api_key = "your google api key"
    gmaps = googlemaps.Client(key=google_maps_api_key)
    directions = gmaps.directions(home_address, work_address)
    first_leg = directions[0]['legs'][0]
    duration = first_leg['duration']['text']

    return duration


def send_text_message(message):
    twilio_account_sid = "twilio sid"
    twilio_account_token = "twilio token"
    twilio_phone_num = "twilio phone"
    your_phone_number = "phone num"
    client = Client(twilio_account_sid, twilio_account_token)

    client.message.create(
    to=your_phone_number,
    from_=twilio_phone_num,
    body=message
    )   


def get_weather():
    url = "https://api.tomorrow.io/v4/weather/forecast?location=san%20jose&timesteps=1d&apikey=8bQzSQ1a72kX213FfucYxBR8zmP2d0yX"
    headers = {"accept": "application/json"}
    response = requests.get(url, headers=headers)
    data = json.loads(response.text)
    temperature_max = data["timelines"]["daily"][0]["values"]["temperatureMax"]
    temperature_min = data["timelines"]["daily"][0]["values"]["temperatureMin"]
    current_date = data["timelines"]["daily"][0]["time"]
    date_obj = datetime.strptime(current_date, "%Y-%m-%dT%H:%M:%SZ")
    formatted_date = date_obj.strftime("%m-%d-%y")
    rounded_max = round(celcius_to_farenheit(temperature_max))
    rounded_min = round(celcius_to_farenheit(temperature_min))

    return rounded_max, rounded_min, formatted_date


def main():
    weather = get_weather()
    eta = get_commute_eta()

    message = (
    f"Good morning Luis!\nHere's the weather report for today, dated {weather[2]}\n"
    f"The maximum temperature expected is {weather[0]}°F\n"
    f"The lowest temperature anticipated is {weather[1]}°F\n"
    f"Your estimated ETA for work is {eta}, so it's time to get going!"
    )
    send_text_message(message)



if __name__ == "__main__":
    main()
