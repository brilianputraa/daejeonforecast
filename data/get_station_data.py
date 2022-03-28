import os
import gzip
import shutil

from urllib.request import urlopen
from urllib.error import HTTPError, URLError


""" Within the Meteostat URL endpoint data duration has 3 selection: hourly, daily, and monthly"""


def get_weather_station_data(data_duration: str, station_number: int):
    data_url = f"https://bulk.meteostat.net/v2/{data_duration}/{station_number}.csv.gz"
    try:
        f = urlopen(data_url)
        with open(os.path.basename(data_url), "wb") as file:
            file.write(f.read())

    except URLError as error:
        print(error.reason, data_url)

    except HTTPError as error:
        print(error.code, data_url)


def extract_data(station_number, base_path: str):
    with gzip.open(os.path.join(base_path, f"{station_number}.csv.gz"), "rb") as f_input:
        with open(os.path.join(base_path, f"{station_number}.csv"), "wb") as f_output:
            shutil.copyfileobj(f_input, f_output)


def main():
    base_path = "/Users/brilianputraa/Documents/ProjectWeather/src"
    data_duration = 'daily'
    station_number = 47133
    try:
        with open(os.path.join(base_path, f"{station_number}.csv.gz"), 'r') as f:
            pass

    except FileNotFoundError:
        get_weather_station_data(data_duration, station_number)
    
    extract_data(station_number, base_path)

if __name__ == "__main__":
    main()