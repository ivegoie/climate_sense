# ClimateSense Weather App

ClimateSense is a simple weather application that retrieves and displays weather information for a given location. It utilizes the Visual Crossing Weather API to provide real-time weather data. The application is built using Python and the PySide6 library for the graphical user interface.

![ClimateSense App Screenshot](https://i.ibb.co/ZcJVsBn/climate-sense-showcase.png)

## Features

- Retrieves current weather information based on user-provided location.
- Displays temperature, feels-like temperature, sunrise, sunset, weather description, and an icon representing the current weather condition.
- Supports various weather conditions and corresponding weather icons.

## Prerequisites

- `Python` 3.x
- `requests` library
- `dotenv` library
- `geopy` library
- `PySide6` library
- `Montserrat` font family

## Installation

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/ivegoie/climate_sense.git
   cd climate_sense
   ```

2. Install the required libraries using pip:
    ```bash
    pip install requests dotenv geopy PySide6
    ```

3. Obtain an API key from [Visual Crossing Weather](https://www.visualcrossing.com) API and store it in a .env file in the root directory of the project:
    ```env
    API_KEY=your_api_key_here
    ```
## Usage
1. Run the main.py script:
    ```bash
    python main.py
    ```
2. The ClimateSense application window will open. Enter a city name or location in the provided input field and click the "Submit" button.
3. The application will fetch weather data for the entered location and display it on the interface.

## Weather Icons

The application displays weather icons corresponding to different weather conditions. The icons are located in the images directory. The appropriate icon is chosen based on the current weather condition.

![ClimateSense App Screenshot](https://i.ibb.co/4NpM930/showcase-dark.png)

## Acknowledgments
This project uses the [Visual Crossing Weather](https://www.visualcrossing.com) API to fetch weather data.

## License
This project is licensed under the [MIT License](LICENSE).