# Weather Forecast Application

This is a simple command-line application that retrieves and displays the weather forecast for a specified city using the OpenWeatherMap API.

## Features

- Retrieve weather forecast data for the next five days in three-hour intervals.
- Display temperature, humidity, wind speed, and weather description for each forecast entry.
- Support for choosing temperature units (Celsius or Fahrenheit) and wind speed units (meters per second or miles per hour).
- Error handling for invalid city names and failed API requests.

## Getting Started

### Prerequisites

- Python 3.12 installed on your system
- OpenWeatherMap API key (sign up at https://home.openweathermap.org/users/sign_up)

### Installation

1. Clone this repository to your local machine:

`git clone https://github.com/zielu2021/weather-forecast-app.git`


2. Navigate to the project directory:

`cd weather-forecast-app`


3. Install the required Python packages:

`pip install -r requirements.txt`

### Usage

1. Create a `.env` file in the project directory and add your OpenWeatherMap API key:

`API_KEY=your_api_key_here`



2. Run the application:

`python weather.py`



3. Follow the prompts to enter the city name, temperature unit (C/F), and wind speed unit (m/s/mph).

4. The application will retrieve and display the weather forecast for the specified city based on your input.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- OpenWeatherMap for providing the weather forecast data via their API.
- Python Dotenv library for managing environment variables.
- Requests library for making HTTP requests.
