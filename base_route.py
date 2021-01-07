from app import app, abort, render_template, redirect, request, url_for, \
    session, get_current_user, db, get_current_teacher
from models import Student, Teachers, All_students,All_groups,All_Capital_Expenditure,All_teachers,\
    All_overhead,All_Charity_Sums, All_withdrawal
from werkzeug.security import generate_password_hash, check_password_hash


@app.route('/')
def home():
    user = get_current_user()
    teacher = get_current_teacher()
    return render_template('base template/home.html', user=user, teacher=teacher)


@app.route('/register', methods=['POST', 'GET'])
def register():
    user = get_current_user()
    if request.method == 'POST':
        name = request.form.get('name').upper()
        surname = request.form.get('surname').upper()
        age = request.form.get('age')
        location = request.form.get('location')
        username = request.form.get('username')
        hashed = request.form.get('password')
        password = request.form.get('confirm_password')
        phone = request.form.get('phone')
        mother_phone = request.form.get('phone_mother')
        father_phone = request.form.get('phone_father')
        otasining_ismi = request.form.get('father_name')
        subject_1 = request.form.get('subject_1')
        subject_2 = request.form.get('subject_2')
        subject_3 = request.form.get('subject_3')
        if Student.query.filter_by(username=username).first():
            return "This username is already token"
        elif hashed != password:
            return 'please check your password'
        elif name == "":
           return "Enter your name"
        elif surname == "":
            "Enter your surname"
        elif age == "":
            "Enter your age"
        elif location == "":
            return "Enter your location"
        elif username == "":
            return "Enter your username"
        elif hashed == "":
            return "Enter your password"
        elif password == "":
            return "Confirm your password"

        hash = generate_password_hash(password,method='sha256')
        if location == "xojakent":
            location = 1
            num = 1
            total = All_students.students + num
            All_students.query.filter_by(id=1).update({'students':total})
            db.session.commit()
        elif location == "gazalkent":
            location = 2
            num = 1
            total = All_students.students + num
            All_students.query.filter_by(id=1).update({'students': total})
            db.session.commit()
        if subject_1 == "Ingliz tili":
            subject_1 = 'Ingliz tili'
        elif subject_1 == "Rus tili":
            subject_1 = 'Rus tili'
        elif subject_1 == "Matematika":
            subject_1 = 'Matematika'
        elif subject_1 == "Tarix":
            subject_1 = 'Tarix'
        elif subject_1 == "Kimyo":
            subject_1 = 'Kimyo'
        elif subject_1 == "Fizika":
            subject_1 = 'Fizika'
        elif subject_1 == "Ona tili va Adabiyot":
            subject_1 = 'Ona tili va Adabiyot'
        elif subject_1 == "Biologiya":
            subject_1 = 'Biologiya'
        elif subject_1 == "Uy xamshiraligi":
            subject_1 = "Uy xamshiraligi"
        elif subject_1 == "Birinchi Fan":
            return "Birinchi fanni kiriting"

        if subject_2 == "Ingliz tili":
            subject_2 = 'Ingliz tili'
        elif subject_2 == "Rus tili":
            subject_2 = 'Rus tili'
        elif subject_2 == "Matematika":
            subject_2 = 'Matematika'
        elif subject_2 == "Tarix":
            subject_2 = 'Tarix'
        elif subject_2 == "Kimyo":
            subject_2 = 'Kimyo'
        elif subject_2 == "Fizika":
            subject_2 = 'Fizika'
        elif subject_2 == "Ona tili va Adabiyot":
            subject_2 = 'Ona tili va Adabiyot'
        elif subject_2 == "Biologiya":
            subject_2 = 'Biologiya'
        elif subject_2 == "Uy xamshiraligi":
            subject_2 = "Uy xamshiraligi"
        elif subject_2 == "Ikkinchi Fan":
            subject_2 = None

        if subject_3 == "Ingliz tili":
            subject_3 = 'Ingliz tili'
        elif subject_3 == "Rus tili":
            subject_3 = 'Rus tili'
        elif subject_3 == "Matematika":
            subject_3 = 'Matematika'
        elif subject_3 == "Tarix":
            subject_3 = 'Tarix'
        elif subject_3 == "Kimyo":
            subject_3 = 'Kimyo'
        elif subject_3 == "Fizika":
            subject_3 = 'Fizika'
        elif subject_3 == "Ona tili va Adabiyot":
            subject_3 = 'Ona tili va Adabiyot'
        elif subject_3 == "Biologiya":
            subject_3 = 'Biologiya'
        elif subject_3 == "Uy xamshiraligi":
            subject_3 = "Uy xamshiraligi"
        elif subject_3 =="Uchinchi Fan":
            subject_3 = None

        if subject_1 == subject_2 or subject_1 == subject_3:
            return "Bir xil fan tanlamang"


        add = Student(name=name,
                      surname=surname,
                      age=age,
                      locations=location,
                      username=username,
                      password=hash,
                      subject_1=subject_1,
                      subject_2=subject_2,
                      subject_3=subject_3,
                      phone=phone,
                      director=False,
                      xojakent_admin=False,
                      gazalkent_admin=False,
                      for_group=False,
                      mother_phone=mother_phone,
                      father_phone=father_phone,
                      charity=0,
                      money=0,
                      otasining_ismi=otasining_ismi
                      )
        db.session.add(add)
        db.session.commit()
        if add.id == 1:
            add = All_Charity_Sums(bank_charity=0)
            add2 = All_overhead(total_sum=0)
            add3 = All_teachers(teachers=0)
            add4 = All_groups(all_groups=0)
            add5 = All_Capital_Expenditure(total_sum=0)
            add6 = All_students(students=0)
            add7 = All_withdrawal(total_sum=0)
            db.session.add(add)
            db.session.add(add2)
            db.session.add(add3)
            db.session.add(add4)
            db.session.add(add5)
            db.session.add(add6)
            db.session.add(add7)
            db.session.commit()
        return redirect(url_for('home'))
    return render_template('base template/Register.html', user=user)


@app.route('/login', methods=['POST', 'GET'])
def login():
    user = get_current_user()
    teacher = get_current_teacher()
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        username_sign = Student.query.filter_by(username=username).first()
        teacher_username = Teachers.query.filter_by(username=username).first()
        if username_sign and check_password_hash(username_sign.password, password):
            session['user'] = username_sign.username
            return redirect(url_for('home'))
        elif teacher_username and check_password_hash(teacher_username.password, password):
            session['teacher'] = teacher_username.username
            return redirect(url_for('home'))
        else:
            return 'password or username is incorrect'
    return render_template('base template/login.html', user=user, teacher=teacher)


@app.route('/logout')
def log_out():
    session.pop('user', None)
    session.pop('teacher', None)
    return redirect(url_for('home'))


@app.route('/delete_account/')
def delete():
    user = get_current_user()
    teacher = get_current_teacher()
    deleted = Student.query.filter_by(id=user.id).first()
    db.session.delete(deleted)
    db.session.commit()
    num = 1
    total = All_students.students - num
    All_students.query.filter_by(id=1).update({'students': total})
    db.session.commit()
    return render_template('base template/home.html', user=user, teacher=teacher)





