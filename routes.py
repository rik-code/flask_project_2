from flask import render_template
from app import app


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/add-student')
def add_students():
    return render_template('add_students.html')


@app.route('/add-subject')
def add_students():
    return render_template('add_subject.html')
