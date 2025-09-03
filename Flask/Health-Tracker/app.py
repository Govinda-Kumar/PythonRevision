import os
import logging
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from forms import HealthDataForm

logging.basicConfig(level=logging.INFO)
app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'your_secret_key')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('POSTGRES_URL', 'sqlite:///health_data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

try:
    db = SQLAlchemy(app)
    logging.info('Database connection initialized.')
except Exception as e:
    logging.error(f'Error initializing database: {e}')

class HealthData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    exercise = db.Column(db.Integer, nullable=False)
    meditation = db.Column(db.Integer, nullable=False)
    sleep = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<HealthData {self.id}>'


try:
    db.create_all()
    logging.info('Database tables created.')
except Exception as e:
    logging.error(f'Error creating database tables: {e}')
    
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/form', methods=['GET', 'POST'])
def form():
    form = HealthDataForm()
    if form.validate_on_submit():
        try:
            new_data = HealthData(
                date=form.date.data,
                exercise = form.exercise.data,
                meditation = form.meditation.data,
                sleep = form.sleep.data
            )
            db.session.add(new_data)
            db.session.commit()
            logging.info('New health data entry added.')
            return redirect(url_for('dashboard'))
        except Exception as e:
            logging.error(f'Error adding health data: {e}')
            flash('An error occurred while saving your data. Please try again.', 'danger')
    return render_template('form.html', form=form)

@app.route('/dashboard')
def dashboard():
    try:
        all_data = HealthData.query.all()
        dates = [data.date.strftime("%Y-%m-%d") for data in all_data]
        exercise_data = [data.exercise for data in all_data]
        meditation_data = [data.meditation for data in all_data]
        sleep_data = [data.sleep for data in all_data]
        return render_template('dashboard.html', dates=dates, exercise_data=exercise_data, meditation_data=meditation_data, sleep_data=sleep_data)
    except Exception as e:
        logging.error(f'Error loading dashboard data: {e}')
        flash('An error occurred while loading dashboard data.', 'danger')
        return render_template('dashboard.html', dates=[], exercise_data=[], meditation_data=[], sleep_data=[])

if __name__ == '__main__':
    app.run(debug=True)