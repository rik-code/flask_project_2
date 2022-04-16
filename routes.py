from flask import render_template, redirect, url_for
from app import app, db, login
from forms import StudentForm, SubjectForm, LoginForm, RegisterForm, TeacherForm, LessonForm
from models import Subjects, Students, User, Teachers, Lessons
from flask_login import current_user, login_user, logout_user, login_required


@login.user_loader
def load_user(id):
    return User.query.get(int(id))


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/add-student', methods=['GET', 'POST'])
@login_required
def add_student():
    form = StudentForm()
    form.subject.choices = [(subject.id, subject.name) for subject in Subjects.query.order_by(Subjects.name).all()]
    students = Students.query.order_by(Students.name).all()
    if form.validate_on_submit():
        student = Students(
            name=form.name.data,
            birth_date=form.birth_date.data,
            mark=form.mark.data,
            subject_id=form.subject.data,
            status=form.status.data
        )
        db.session.add(student)
        db.session.commit()
        return redirect(url_for('add_student'))

    return render_template('add_students.html', form=form, items=students)


@app.route('/add-subject', methods=['GET', 'POST'])
@login_required
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
    form.subject.choices = [(subject.id, subject.name) for subject in Subjects.query.order_by(Subjects.name).all()]
    if form.validate_on_submit():
        students.name = form.name.data
        students.birth_date = form.birth_date.data
        students.mark = form.mark.data
        students.subject_id = form.subject.data
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


@app.route('/delete-subj/<int:id>')
def delete_subject(id):
    subject = Subjects.query.get_or_404(id)
    try:
        db.session.delete(subject)
        db.session.commit()
        return redirect(url_for('add_subject'))
    except:
        return 'Что-то пошло не так'


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('index'))
    return render_template('login.html', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html', form=form)


@app.route('/timetable')
def timetable():
    return render_template('timetable.html')


@app.route('/add-teacher', methods=['GET', 'POST'])
@login_required
def add_teacher():
    form = TeacherForm()
    form.subject.choices = [(subject.id, subject.name) for subject in Subjects.query.order_by(Subjects.name).all()]
    teacher_list = Teachers.query.order_by(Teachers.name).all()
    if form.validate_on_submit():
        teacher = Teachers(
            name=form.name.data,
            subject_id=form.subject.data
        )
        db.session.add(teacher)
        db.session.commit()
    return render_template('add_teacher.html', form=form, items=teacher_list)


@app.route('/add-lesson', methods=['GET', 'POST'])
@login_required
def add_lesson():
    form = LessonForm()
    subjects = Subjects.query.order_by(Subjects.name).all()
    teachers = Teachers.query.order_by(Teachers.name).all()

    form.subject.choices = [(subject.id, subject.name) for subject in subjects]
    form.teacher.choices = [(teachers.id, teacher.name) for teacher in teachers]

    return render_template('add_lesson.html', form=form)