from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/weather', methods=['GET'])
def get_weather():
    cities = request.args.get('cities')
    if not cities:
        return render_template('index.html', error='City parameter is missing!')
    
    cities_list = cities.split(',')
    weather_data = {}
    for city in cities_list:
        response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=37aa7417db97de30a60f5fa5bd3b1d0b')
        if response.status_code == 200:
            data = response.json()
            weather_data[city] = {
                'Temperature': data.get('main', {}).get('temp'),
                'Feels Like': data.get('main', {}).get('feels_like'),
                'Minimum Temperature': data.get('main', {}).get('temp_min'),
                'Maximum Temperature': data.get('main', {}).get('temp_max'),
                'Pressure': data.get('main', {}).get('pressure'),
                'Humidity': data.get('main', {}).get('humidity'),
                'Weather Description': data.get('weather', [{}])[0].get('description'),
                'Wind Speed': data.get('wind', {}).get('speed'),
                'Wind Direction': data.get('wind', {}).get('deg'),
                'Cloudiness': data.get('clouds', {}).get('all'),
                'Visibility': data.get('visibility'),
                'Sunrise': data.get('sys', {}).get('sunrise'),
                'Sunset': data.get('sys', {}).get('sunset'),
            }
        else:
            weather_data[city] = {'error': 'Failed to retrieve weather data!'}
    
    return render_template('weather.html', weather_data=weather_data)

if __name__ == '__main__':
    app.run(debug=True)
