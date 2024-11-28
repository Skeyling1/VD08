from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    weather = None
    fact = None
    news = get_news()
    if request.method == 'POST':
        try:
            city = request.form['city']
            weather = get_weather(city)
        except:
            city = None

        try:
            number = request.form['number']
            fact = get_fact(number)
        except:
            fact = None

    return render_template("index.html", weather=weather, news=news, fact=fact)


def get_weather(city):
    api_key = "ваш API"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&APPID={api_key}&units=metric"
    response = requests.get(url)
    return response.json()

def get_news():
    api_key = "ваш API"
    url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}"
    response = requests.get(url)
    return response.json().get('articles', [])

def get_fact(number):
    url = f"http://numbersapi.com/{number}"
    response = requests.get(url)
    return response.text


if __name__ == '__main__':
    app.run(debug=True)