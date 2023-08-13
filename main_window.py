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
        
        self.geolocator = Nominatim(user_agent="ClimateSense")
        self.geocode = partial(self.geolocator.geocode)
        
        image_path = os.path.join("images", "background.png")
        self.setStyleSheet(f"background-image: url({image_path}); background-repeat: no-repeat; background-position: center;")
        
        self.weather_frame.hide()
        self.loading_frame.hide()

        
        self.submit_button.clicked.connect(self.on_button_submit)
        
    def on_button_submit(self):
        self.api_key = os.getenv("API_KEY")
        
        self.get_city_name = self.city_entry.text()
        self.name = self.geocode(self.get_city_name)
        self.location = self.geolocator.geocode(self.name)
        
        self.latitude = self.location.latitude
        self.longitude = self.location.longitude

        API_URL = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{self.latitude}%2C%20{self.longitude}?unitGroup=metric&key={self.api_key}&contentType=json"

        self.response = requests.get(API_URL)
        self.city_info = self.response.json()
        
        self.show_weather_info()
    
    def show_weather_info(self):
        self.weather_frame.show()
        self.city_name.setText(self.get_city_name.capitalize())
        
        get_temperature = f"Temperature : {self.city_info['currentConditions']['temp']:.0f} °C"
        get_feels_like = f"Feels like : {self.city_info['currentConditions']['feelslike']:.0f} °C"
        get_sunrise = f"Sunrise : {self.city_info['currentConditions']['sunrise']}"
        get_sunset = f"Sunset : {self.city_info['currentConditions']['sunset']}"
        get_weather_icon_text = self.city_info['currentConditions']['icon']

        self.temperature.setText(get_temperature)
        self.feels_like.setText(get_feels_like)
        self.sunrise.setText(get_sunrise)
        self.sunset.setText(get_sunset)
        self.description.setText(self.city_info['description'])
        self.weather_icon.setText(get_weather_icon_text)

