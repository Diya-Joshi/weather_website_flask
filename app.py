from flask import Flask, render_template, request, redirect, url_for
from weather_data import get_weather_data  

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/weather', methods=['POST'])
def weather():
    city = request.form['city']
    if not city:
        return redirect(url_for('index'))

    weather_data = get_weather_data(city)  
    if not weather_data:
        return redirect(url_for('index'))

    return render_template('weather.html', weather=weather_data)

if __name__ == '__main__':
    app.run(debug=True)
