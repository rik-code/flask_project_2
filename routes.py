from flask import render_template
from app import app
from forms import StudentForm, SubjectForm


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/add-student', methods=['GET', 'POST'])
def add_students():
    form = StudentForm()
    return render_template('add_students.html', form=form)


@app.route('/add-subject', methods=['GET', 'POST'])
def add_students():
    form = SubjectForm()
    return render_template('add_subject.html', form=form)
