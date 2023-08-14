import os
from functools import partial

import requests
from dotenv import load_dotenv
from geopy.geocoders import Nominatim
from PySide6.QtGui import QPixmap
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
        self.setStyleSheet("QMainWindow { background-image: url(" + image_path + "); background-repeat: no-repeat;}")
        
        self.weather_frame.hide()
        
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
        self.city_name.setText(self.get_city_name.title())
        self.entry_label.setText("Search for your location")
        
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
        
        match get_weather_icon_text:
            case 'clear-night':
                image_path = os.path.join("images", "night_full_moon_clear.png")
                pixmap = QPixmap(image_path)
                
                self.weather_icon.setPixmap(pixmap)
                
            case 'clear-day':
                image_path = os.path.join("images", "day_clear")
                pixmap = QPixmap(image_path)
                
                self.weather_icon.setPixmap(pixmap)
                
            case 'partly-cloudy-night':
                image_path = os.path.join("images", "night_full_moon_partial_cloud.png")
                pixmap = QPixmap(image_path)
                
                self.weather_icon.setPixmap(pixmap)
                
            case 'partly-cloudy-day':
                image_path = os.path.join("images", "day_partial_cloud.png")
                pixmap = QPixmap(image_path)
                
                self.weather_icon.setPixmap(pixmap)
                
            case 'cloudy':
                image_path = os.path.join("images", "cloudy.png")
                pixmap = QPixmap(image_path)
                
                self.weather_icon.setPixmap(pixmap)
                
            case 'wind':
                image_path = os.path.join("images", "wind.png")
                pixmap = QPixmap(image_path)
                
                self.weather_icon.setPixmap(pixmap)
                
            case 'fog':
                image_path = os.path.join("images", "fog.png")
                pixmap = QPixmap(image_path)
                
                self.weather_icon.setPixmap(pixmap)

        
            case 'showers-night':
                image_path = os.path.join("images", "night_full_moon_rain.png")
                pixmap = QPixmap(image_path)
                
                self.weather_icon.setPixmap(pixmap)
        
            case 'showers-day':
                image_path = os.path.join("images", "day_rain")
                pixmap = QPixmap(image_path)
                
                self.weather_icon.setPixmap(pixmap)
                
            case 'rain':
                image_path = os.path.join("images", "rain")
                pixmap = QPixmap(image_path)
                
                self.weather_icon.setPixmap(pixmap)
                
            case 'thunder-showers-night':
                image_path = os.path.join("images", "night_full_moon_rain_thunder.png")
                pixmap = QPixmap(image_path)
                
                self.weather_icon.setPixmap(pixmap)
                
            case 'thunder-showers-day':
                image_path = os.path.join("images", "dday_rain_thunder.png")
                pixmap = QPixmap(image_path)
                
                self.weather_icon.setPixmap(pixmap)
                
            case 'thunder-rain':
                image_path = os.path.join("images", "rain_thunder.png")
                pixmap = QPixmap(image_path)
                
                self.weather_icon.setPixmap(pixmap)
                
            case 'snow-showers-night':
                image_path = os.path.join("images", "night_full_moon_sleet.png")
                pixmap = QPixmap(image_path)
                
                self.weather_icon.setPixmap(pixmap)
                
            case 'snow-showers-day':
                image_path = os.path.join("images", "day_sleet.png")
                pixmap = QPixmap(image_path)
                
                self.weather_icon.setPixmap(pixmap)
                
            case 'snow':
                image_path = os.path.join("images", "snow.png")
                pixmap = QPixmap(image_path)
                
                self.weather_icon.setPixmap(pixmap)

        self.weather_frame.show()
        
        if self.get_city_name == "":
            self.entry_label.setText("Please enter your location")
            self.weather_frame.hide()

        
