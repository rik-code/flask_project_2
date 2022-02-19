from flask import render_template
from app import app, db
from forms import StudentForm, SubjectForm
from models import Subjects, Students


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/add-student', methods=['GET', 'POST'])
def add_student():
    form = StudentForm()
    if form.validate_on_submit():
        student = Students(
            name=form['name'],
            birth_date=form['birth_date'],
            mark=form['mark'],
            status=form['status']
        )

    return render_template('add_students.html', form=form)


@app.route('/add-subject', methods=['GET', 'POST'])
def add_subject():
    form = SubjectForm()
    return render_template('add_subject.html', form=form)
