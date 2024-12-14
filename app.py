from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/experiments')
def experiments():
    return render_template('experiments.html')

@app.route('/photos')
def photos():
    return render_template('photos.html')

@app.route('/calculator')
def calculator():
    return render_template('calculator.html')

@app.route('/quizzes')
def quizzes():
    return render_template('quizzes.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
