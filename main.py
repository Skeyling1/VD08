from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    weather = None
    news = None
    if request.method == 'POST':
        city = request.form['city']
        weather = get_weather(city)
        news = get_news()
    return render_template("index.html", weather=weather, news=news)


def get_weather(city):
    api_key = "63b52308593f20bc73d96a66df4e7dfa"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&APPID={api_key}&units=metric"
    response = requests.get(url)
    return response.json()

def get_news():
    api_key = "2c905e26210848e2a0322f1ee94123de"
    url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}"
    response = requests.get(url)
    return response.json().get('articles', [])

if __name__ == '__main__':
    app.run(debug=True)