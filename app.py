from flask import Flask, render_template, redirect, request, url_for, abort, session, flash
from flask_sqlalchemy import SQLAlchemy
import os
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired
from flask_uploads import UploadSet, IMAGES, configure_uploads
from sqlalchemy import String, Boolean, Integer, Column, ForeignKey, ARRAY, or_, DateTime, DATE
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from werkzeug.exceptions import RequestEntityTooLarge
from werkzeug.security import generate_password_hash, check_password_hash



DB_HOST = os.getenv('DB_HOST', 'localhost:5432')
DB_USER = os.getenv('DB_USER', 'postgres')
DB_PASSWORD = os.getenv('DB_PASSWORD', '123')
DB_NAME = os.getenv('DB_NAME', 'gennis_3.0')
database_path = 'postgresql://{}:{}@{}/{}'.format(DB_USER, DB_PASSWORD, DB_HOST, DB_NAME)

app = Flask(__name__)
app.config['UPLOADED_IMAGES_DEST'] = 'uploads/images'
INSTALLED_APPS = [
  'fontawesome-free'
]
app.config['SQLALCHEMY_DATABASE_URI'] = database_path
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['MAX_CONTENT_LENGTH'] = 1 * 922 * 1200
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = os.urandom(24)
images = UploadSet('images', IMAGES)
configure_uploads(app, images)

db = SQLAlchemy(app)
migrate = Migrate(app, db)


def get_current_user():
    user_result = None
    if 'user' in session:
        user = session['user']
        user = Student.query.filter_by(username=user).first()
        user_result = user

    return user_result


def get_current_teacher():
    teacher_result = None
    if 'teacher' in session:
        user = session['teacher']
        user = Teachers.query.filter_by(username=user).first()
        teacher_result = user

    return teacher_result


class PhotoForm(FlaskForm):
    image = FileField('photo', validators=[FileRequired()
                                           ])


@app.route('/photo_user', methods=['GET', 'POST'])
def photo_add():
    user = get_current_user()
    try:
        if not user.gazalkent_admin and not user.director and not user.xojakent_admin and not user:
            return redirect(url_for('home'))
    except AttributeError:
        return redirect(url_for('home'))
    form = PhotoForm(meta={'csrf': False})
    if form.validate_on_submit():
        filename = images.save(form.image.data)
        image_url = images.url(filename)
        Student.query.filter_by(id=user.id).update({'photo': image_url})
        db.session.commit()
        return redirect(url_for('info'))
    return render_template('student/photo.html', user=user, form=form)


@app.route('/photo_teacher', methods=['GET', 'POST'])
def photo_teacher():
    teacher = get_current_teacher()
    try:
        if not teacher:
            return redirect(url_for('home'))
    except AttributeError:
        return redirect(url_for('home'))
    form = PhotoForm(meta={'csrf': False})
    if form.validate_on_submit():
        filename = images.save(form.image.data)
        image_url = images.url(filename)
        Teachers.query.filter_by(id=teacher.id).update({'photo': image_url})
        db.session.commit()
        return redirect(url_for('info_teacher'))
    return render_template('Teacher/photo teacher.html', form=form)


@app.route('/change_info')
def change_info():
    user = get_current_user()
    try:
        if not user.gazalkent_admin and not user.director and not user.xojakent_admin and not user:
            return redirect(url_for('home'))
    except AttributeError:
        return redirect(url_for('home'))
    users = Student.query.filter_by(id=user.id).all()
    return render_template('base template/change info.html', user=user, users=users)


@app.route('/change_teacher')
def change_teacher():
    user = get_current_user()
    teacher = get_current_teacher()
    try:
        if not teacher:
            return redirect(url_for('home'))
    except AttributeError:
        return redirect(url_for('home'))
    users = Teachers.query.filter_by(id=teacher.id).all()
    return render_template('Teacher/change teacher info.html',user=user,teacher=teacher,users=users)


@app.route('/change_password_teacher', methods=['POST', 'GET'])
def change_password_teacher():
    user = get_current_user()
    teacher = get_current_teacher()
    try:
        if not teacher:
            return redirect(url_for('home'))
    except AttributeError:
        return redirect(url_for('home'))
    if request.method == 'POST':
        current_password = request.form.get('current_password')
        password = Teachers.query.filter_by(id=teacher.id).first()
        if password and check_password_hash(password.password,current_password):
            new_password = request.form.get('new_password')
            confirm_password = request.form.get('confirm_password')
            if new_password == confirm_password:
                confirmed = generate_password_hash(confirm_password)
                Teachers.query.filter_by(id=teacher.id).update({'password':confirmed})
                db.session.commit()
                return redirect(url_for('home'))
            else:
                return 'Your passwords are not seemed true'

        else:
            return 'Your current password is invalid'

    return render_template('Teacher/channge teacher password.html', user=user)


@app.route('/change_password', methods=['POST', 'GET'])
def change_password():
    user = get_current_user()
    try:
        if not user.gazalkent_admin and not user.director and not user.xojakent_admin and not user:
            return redirect(url_for('home'))
    except AttributeError:
        return redirect(url_for('home'))
    if request.method == 'POST':
        current_password = request.form.get('current_password')
        password = Student.query.filter_by(id=user.id).first()
        if password and check_password_hash(password.password,current_password):
            new_password = request.form.get('new_password')
            confirm_password = request.form.get('confirm_password')
            if new_password == confirm_password:
                confirmed = generate_password_hash(confirm_password)
                Student.query.filter_by(id=user.id).update({'password':confirmed})
                db.session.commit()
                return redirect(url_for('home'))
            else:
                return 'Your passwords are not seemed true'

        else:
            return 'Your current password is invalid'

    return render_template('student/password changing.html', user=user)


@app.route('/change_teacher_info', methods=['POST'])
def change_teacher_info():
    user = get_current_user()
    teacher = get_current_teacher()
    name = request.form.get('name')
    surname = request.form.get('surname')
    gmail = request.form.get('gmail')
    phone = request.form.get('phone')
    Teachers.query.filter_by(id=teacher.id).update(
        {'name': name, 'surname': surname, 'gmail': gmail, 'phone': phone})
    db.session.commit()
    return redirect(url_for('home'))


@app.route('/change', methods=['POST'])
def change():
    user = get_current_user()
    try:
        if not user.gazalkent_admin and not user.director and not user.xojakent_admin and not user:
            return redirect(url_for('home'))
    except AttributeError:
        return redirect(url_for('home'))
    name = request.form.get('name')
    surname = request.form.get('surname')
    gmail = request.form.get('gmail')
    phone = request.form.get('phone')
    subject_1 = request.form.get('subject_1')
    subject_2 = request.form.get('subject_2')
    subject_3 = request.form.get('subject_3')
    subject = Student.query.filter_by(id=user.id)
    for subjects in subject:
        if subject_1 == subjects.subject_1:
            subject_1 = subjects.subject_1
        elif subject_1 == "English Language":
            subject_1 = 'english language'
        elif subject_1 == "Russian Language":
            subject_1 = 'russian language'
        elif subject_1 == "Mathematics":
            subject_1 = 'math'
        elif subject_1 == "History":
            subject_1 = 'history'
        elif subject_1 == "Chemistry":
            subject_1 = 'chemistry'
        elif subject_1 == "Physics":
            subject_1 = 'physics'
        elif subject_1 == "Mother Tongue and Literature":
            subject_1 = 'mother tongue and literature'
        elif subject_1 == "Choose your first subject":
            subject_1 = ""

        if subject_2 == subjects.subject_2:
            subject_2 = subjects.subject_2
        elif subject_2 == "English Language":
            subject_2 = 'english language'
        elif subject_2 == "Russian Language":
            subject_2 = 'russian language'
        elif subject_2 == "Mathematics":
            subject_2 = 'math'
        elif subject_2 == "History":
            subject_2 = 'history'
        elif subject_2 == "Chemistry":
            subject_2 = 'chemistry'
        elif subject_2 == "Physics":
            subject_2 = 'physics'
        elif subject_2 == "Mother Tongue and Literature":
            subject_2 = 'mother tongue and literature'
        elif subject_2 == "Choose your second subject":
            subject_2 = ""

        if subject_3 == subjects.subject_3:
            subject_3 = subjects.subject_3
        elif subject_3 == "English Language":
            subject_3 = 'english language'
        elif subject_3 == "Russian Language":
            subject_3 = 'russian language'
        elif subject_3 == "Mathematics":
            subject_3 = 'math'
        elif subject_3 == "History":
            subject_3 = 'history'
        elif subject_3 == "Chemistry":
            subject_3 = 'chemistry'
        elif subject_3 == "Physics":
            subject_3 = 'physics'
        elif subject_3 == "Mother Tongue and Literature":
            subject_3 = 'mother tongue and literature'
        elif subject_3 == "Choose your third subject":
            subject_3 = ""

        Student.query.filter_by(id=user.id).update(
            {'name': name, 'surname': surname, 'username': gmail, 'phone': phone,
             'subject_1': subject_1,
             'subject_2': subject_2,
             'subject_3': subject_3,})
        db.session.commit()
        return redirect(url_for('home'))


from base_route import *
from admin import *
from admin2 import *
from admin3 import *
from admin4 import *
from admin5 import *
from director import *
from teacher import *
from student import *

manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == "__main__":
    manager.run()
