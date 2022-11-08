'''
Autor: Edgar Francisco Hernandez Mendez
Fecha:08/11/2022
Actividad:Seleccion de APIs

Nombre de API: Prediccion de Fotbol
Descripcion de la API: Predice el las anotaciones del juego antes de iniciar el partido
Portal: https://apilist.fun/api/football-prediction


'''
from datetime import datetime, timedelta, timezone
import os

import requests
import pytz

{
  "data": {
    "allowed_for_your_subscription": [
      "home_over_05",
      "btts",
      "over_35",
      "classic",
      "home_over_15",
      "over_25",
      "away_over_15",
      "away_over_05"
    ],
    "all": [
      "home_over_05",
      "btts",
      "over_35",
      "classic",
      "home_over_15",
      "over_25",
      "away_over_15",
      "away_over_05"
    ]
  }
}



api_tz = pytz.timezone("Europe/London")

# Change this to your timezone
local_tz = pytz.timezone("Europe/Rome")


def get_current_datetime_on_api_server():
    london_time = datetime.now(tz=timezone.utc).astimezone(api_tz)
    return london_time


def to_local_datetime(start_date):
    dt = datetime.strptime(start_date, "%Y-%m-%dT%H:%M:%S")
    return api_tz.localize(dt).astimezone(local_tz)


if __name__ == "__main__":
    # this is a datetime object with the timezone used by our api
    current_server_time = get_current_datetime_on_api_server()

    # obtaining the next day as python date object
    tomorrow = current_server_time.date() + timedelta(days=1)

    # setting our API key for auth
    headers = {
        'User-Agent': 'python_requests',
        "X-RapidAPI-Key": os.environ["RAPIDAPI_KEY"],
        # set "X-Mashape-Key if you are using mashape.com
    }

    session = requests.Session()
    session.headers = headers

    # setting our query params
    params = {
        "iso_date": tomorrow.isoformat(), # python date object should be transformed to ISO format (YYYY-MM-DD)
        "federation": "UEFA",
        "market": "classic"
    }

    prediction_endpoint = "https://football-prediction-api.p.rapidapi.com/api/v2/predictions"
    response = session.get(prediction_endpoint, params=params)

    if response.ok:
        json = response.json()
        json["data"].sort(key=lambda p: p["start_date"])

        for match in json["data"]:
            # going to print tab separated start_time, home_team vs away team, prediction @ predicted odds.
            output = "{st}\t{ht} vs {at}\t{p} @ {odd}"

            local_start_time = to_local_datetime(match["start_date"])
            home_team = match["home_team"]
            away_team = match["away_team"]
            prediction = match["prediction"]

            if "odds" in match:
                prediction_odds = match["odds"].get(prediction, None)
            else:
                # user is not able to see odds as it's subscription plan does not support it.
                prediction_odds = None

            print(output.format(st=local_start_time, ht=home_team, at=away_team, p=prediction, odd=prediction_odds))
    else:
        print("Bad response from server, status-code: {}".format(response.status_code))
        print(response.content)