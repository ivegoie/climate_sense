import os
from functools import partial

import requests
from dotenv import load_dotenv
from geopy.geocoders import Nominatim
from PySide6.QtWidgets import QMainWindow

from ui_climate_sense import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        load_dotenv()
        api_key = os.getenv("API_KEY")
        
        geolocator = Nominatim(user_agent="ClimateSense")
        geocode = partial(geolocator.geocode)

        city_name = geocode("Pula")

        longitude = city_name.longitude
        latitude = city_name.latitude
        
        API_URL = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{latitude}%2C%20{longitude}?unitGroup=metric&key={api_key}&contentType=json"

        response = requests.get(API_URL)

        city_info = response.json()
        

        self.label.setText(f"Temperatura u Puli iznosi: {city_info['currentConditions']['temp']}")

        