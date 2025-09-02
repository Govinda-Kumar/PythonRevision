from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    user = {'username': 'Govinda'}
    items = ['Flask', 'Django', 'FastAPI']
    return render_template('index.html', user=user, items=items, title='Health Tracker')


@app.route('/welcome')
def welcome():
    return render_template('welcome.html')

if __name__ == '__main__':
    app.run(debug=True)

