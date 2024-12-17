from flask import Flask, render_template, request
import requests

app = Flask(__name__)

def read_visits():
    try:
        with open('visits.txt', 'r') as file:
            visits = int(file.read())
    except FileNotFoundError:
        visits = 0
    return visits

def update_visits():
    ip_address = request.remote_addr
    if not is_ip_recorded(ip_address):
        visits = read_visits() + 1
        with open('visits.txt', 'w') as file:
            file.write(str(visits))
        record_ip(ip_address)
    else:
        visits = read_visits()
    return visits

def is_ip_recorded(ip_address):
    try:
        with open('ips.txt', 'r') as file:
            ips = [line.split(',')[0] for line in file.read().splitlines()]
        return ip_address in ips
    except FileNotFoundError:
        return False

def record_ip(ip_address):
    location = get_location(ip_address)
    with open('ips.txt', 'a') as file:
        file.write(f'{ip_address},{location}\n')

def get_location(ip_address):
    try:
        response = requests.get(f'https://ipapi.co/{ip_address}/json')
        data = response.json()
        location = f"{data['city']}, {data['region']}, {data['country']}"
    except:
        location = "Unknown"
    return location

@app.route('/')
def home():
    visits = update_visits()
    return render_template('home.html', visits=visits)

@app.route('/about')
def about():
    visits = read_visits()
    return render_template('about.html', visits=visits)

@app.route('/experiments')
def experiments():
    visits = read_visits()
    return render_template('experiments.html', visits=visits)

@app.route('/photos')
def photos():
    visits = read_visits()
    return render_template('photos.html', visits=visits)

@app.route('/calculator')
def calculator():
    visits = read_visits()
    return render_template('calculator.html', visits=visits)

@app.route('/quizzes')
def quizzes():
    visits = read_visits()
    return render_template('quizzes.html', visits=visits)

@app.route('/contact')
def contact():
    visits = read_visits()
    return render_template('contact.html', visits=visits)

if __name__ == '__main__':
    app.run(debug=True)
