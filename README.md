# Weather App

This is a simple web application built with Flask that allows users to retrieve weather information for multiple cities.
![Sample Image](![Screenshot (409).png](https://github.com/piyushrai007/leadzen/blob/f4a6f3f49b88f400d953c4d1906b610cf02ee9b4/Screenshot%20(409).png))
![Sample Image]![(Screenshot (410).png](https://github.com/piyushrai007/leadzen/blob/f4a6f3f49b88f400d953c4d1906b610cf02ee9b4/Screenshot%20(410).png))


## Tech Stack

- **Python**: The backend of the application is written in Python using the Flask framework.
- **HTML/CSS**: The frontend of the application uses HTML for structure and CSS for styling.
- **JavaScript**: JavaScript is used to make asynchronous requests to the Flask backend and update the webpage dynamically.
- **OpenWeatherMap API**: Weather data is fetched from the OpenWeatherMap API.

## Features

- Users can input multiple city names separated by commas and retrieve weather details for each city.
- Weather details include temperature, feels like temperature, minimum temperature, maximum temperature, pressure, humidity, weather description, wind speed, wind direction, cloudiness, visibility, sunrise, and sunset.
- Error handling for failed requests to the OpenWeatherMap API.

## Setup

1. Clone the repository:

    ```
    git clone https://github.com/piyushrai007/leadzen.git
    ```

2. Install dependencies:

    ```
    pip install -r requirements.txt
    ```

3. Obtain an API key from [OpenWeatherMap](https://openweathermap.org/api) and replace `'YOUR_API_KEY'` in `api.py` with your API key.

4. Run the Flask application:

    ```
    python api.py
    ```

5. Open your web browser and navigate to `http://localhost:5000` to use the weather app.

## Usage

1. Enter the names of the cities you want to get weather information for in the input field, separated by commas.
2. Click on the "Get Weather Details" button.
3. Weather details for each city will be displayed below the input field.

## Contributing

Contributions are welcome! If you find any bugs or have suggestions for improvement, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
