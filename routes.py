from flask import render_template, redirect, url_for
from app import app, db
from forms import StudentForm, SubjectForm
from models import Subjects, Students


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/add-student', methods=['GET', 'POST'])
def add_student():
    form = StudentForm()
    form.subject.choices = [(1, 'First'), (2, 'Second')]
    students = Students.query.order_by(Students.name).all()
    if form.validate_on_submit():
        student = Students(
            name=form.name.data,
            birth_date=form.birth_date.data,
            mark=form.mark.data,
            status=form.status.data
        )
        db.session.add(student)
        db.session.commit()
        return redirect(url_for('add_student'))

    return render_template('add_students.html', form=form, items=students)


@app.route('/add-subject', methods=['GET', 'POST'])
def add_subject():
    form = SubjectForm()
    subjects = Subjects.query.order_by(Subjects.name).all()
    if form.validate_on_submit():
        subj = Subjects(
            name=form.name.data
        )
        db.session.add(subj)
        db.session.commit()
        return redirect(url_for('add_subject'))
    return render_template('add_subject.html', form=form, items=subjects)


@app.route('/update-student/<int:id>', methods=['GET', 'POST'])
def update(id):
    students = Students.query.get_or_404(id)
    form = StudentForm()
    if form.validate_on_submit():
        students.name = form.name.data
        students.birth_date = form.birth_date.data
        students.mark = form.mark.data
        students.status = form.status.data
        try:
            db.session.commit()
        except:
            return 'There was a problem updating data.'
        return redirect(url_for('add_student'))
    else:
        return render_template('update-student.html', form=form, student=students)


@app.errorhandler(404)
def error_404(error):
    return render_template('404.html'), 404


@app.route('/delete/<int:id>')
def delete_student(id):
    student = Students.query.get_or_404(id)
    try:
        db.session.delete(student)
        db.session.commit()
        return redirect(url_for('add_student'))
    except:
        return 'Что-то пошло не так'