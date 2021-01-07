from app import request, redirect, url_for, app, get_current_user, render_template, get_current_teacher, db, abort
from models import Student, Teachers, Groups, All_teachers
from werkzeug.security import generate_password_hash


@app.route('/location-1')
def location1():
    user = get_current_user()
    try:
        if not user.director and not user.xojakent_admin :
            return redirect(url_for('home'))
    except AttributeError:
        return redirect(url_for('home'))
    show = Student.query.order_by('age').all()
    return render_template('Xojakent new students/xojakent.html', show=show, user=user)


@app.route('/location-2')
def location2():
    user = get_current_user()
    try:
        if not user.director and not user.gazalkent_admin:
            return redirect(url_for('home'))
    except AttributeError:
        return redirect(url_for('home'))
    show = Student.query.order_by('age').all()
    return render_template('Gazalkent new Students/gazalkent.html', show=show, user=user)


@app.route('/student_english')
def student_english():
    user = get_current_user()
    try:
        if not user.director and not user.xojakent_admin:
            return redirect(url_for('home'))
    except AttributeError:
        return redirect(url_for('home'))
    teachers = Teachers.query.filter_by(subject='eng')
    show = Student.query.order_by('age').all()
    return render_template('Xojakent new students/Xojakent_English New Students.html', show=show, user=user,
                           teachers=teachers)


@app.route('/student_xamshira')
def student_xamshira():
    user = get_current_user()
    try:
        if not user.director and not user.xojakent_admin:
            return redirect(url_for('home'))
    except AttributeError:
        return redirect(url_for('home'))
    teachers = Teachers.query.filter_by(subject='eng')
    show = Student.query.order_by('age').all()
    return render_template('Xojakent new students/uy xamshiraligi.html', show=show, user=user,
                           teachers=teachers)


@app.route('/gazalkent_xamshira')
def gazalkent_xamshira():
    user = get_current_user()
    try:
        if not user.director and not user.gazalkent_admin:
            return redirect(url_for('home'))
    except AttributeError:
        return redirect(url_for('home'))
    teachers = Teachers.query.filter_by(subject='eng')
    show = Student.query.order_by('age').all()
    return render_template('Gazalkent new Students/uy xamshiraligi.html', show=show, user=user,
                           teachers=teachers)


@app.route('/gazalkent_english')
def gazalkent_english():
    user = get_current_user()
    try:
        if not user.director and not user.gazalkent_admin:
            return redirect(url_for('home'))
    except AttributeError:
        return redirect(url_for('home'))
    show = Student.query.order_by('age').all()
    return render_template('Gazalkent new Students/gazalkent english.html', show=show, user=user)


@app.route('/gazalkent_student_russian')
def gazalkent_russian():
    user = get_current_user()
    try:
        if not user.director and not user.gazalkent_admin:
            return redirect(url_for('home'))
    except AttributeError:
        return redirect(url_for('home'))
    show = Student.query.order_by('age').all()
    return render_template('Gazalkent new Students/Gazalkent Russian Language.html', show=show, user=user)


@app.route('/xojakent_student_russian')
def xojakent_russian():
    user = get_current_user()
    try:
        if not user.director and not user.xojakent_admin:
            return redirect(url_for('home'))
    except AttributeError:
        return redirect(url_for('home'))
    show = Student.query.order_by('age').all()
    return render_template('Xojakent new students/Xojakent Russian Language.html', show=show, user=user)


@app.route('/xojakent_student_math')
def xojakent_math():
    user = get_current_user()
    try:
        if not user.director and not user.xojakent_admin:
            return redirect(url_for('home'))
    except AttributeError:
        return redirect(url_for('home'))
    show = Student.query.order_by('age').all()
    return render_template('Xojakent new students/xojakent_math.html', show=show, user=user)


@app.route('/gazalkent_student_math')
def gazalkent_math():
    user = get_current_user()
    try:
        if not user.director and not user.gazalkent_admin:
            return redirect(url_for('home'))
    except AttributeError:
        return redirect(url_for('home'))
    show = Student.query.order_by('age').all()
    return render_template('Gazalkent new Students/gazalkent math.html', show=show, user=user)


@app.route('/xojakent_student_history')
def xojakent_history():
    user = get_current_user()
    try:
        if not user.director and not user.xojakent_admin:
            return redirect(url_for('home'))
    except AttributeError:
        return redirect(url_for('home'))
    show = Student.query.order_by('age').all()
    return render_template('Xojakent new students/xojakent_history.html', show=show, user=user)


@app.route('/gazalkent_student_history')
def gazalkent_history():
    user = get_current_user()
    try:
        if not user.director and not user.gazalkent_admin:
            return redirect(url_for('home'))
    except AttributeError:
        return redirect(url_for('home'))
    show = Student.query.order_by('age').all()
    return render_template('Gazalkent new Students/gazalkent_history.html', show=show, user=user)


@app.route('/xojakent_student_tongue')
def xojakent_tongue():
    user = get_current_user()
    try:
        if not user.director and not user.xojakent_admin:
            return redirect(url_for('home'))
    except AttributeError:
        return redirect(url_for('home'))
    show = Student.query.order_by('age').all()
    return render_template('Xojakent new students/xojakent_mother_tongue.html', show=show, user=user)


@app.route('/gazalkent_student_tongue')
def gazalkent_tongue():
    user = get_current_user()
    try:
        if not user.director and not user.gazalkent_admin:
            return redirect(url_for('home'))
    except AttributeError:
        return redirect(url_for('home'))
    show = Student.query.order_by('age').all()
    return render_template('Gazalkent new Students/gazalkent_tongue.html', show=show, user=user)


@app.route('/xojakent_student_chemistry')
def xojakent_chemistry():
    user = get_current_user()
    try:
        if not user.director and not user.xojakent_admin:
            return redirect(url_for('home'))
    except AttributeError:
        return redirect(url_for('home'))
    show = Student.query.order_by('age').all()
    return render_template('Xojakent new students/xojakent_chemistry.html', show=show, user=user)


@app.route('/gazalkent_student_chemistry')
def gazalkent_chemistry():
    user = get_current_user()
    try:
        if not user.director and not user.gazalkent_admin:
            return redirect(url_for('home'))
    except AttributeError:
        return redirect(url_for('home'))
    show = Student.query.order_by('age').all()
    return render_template('Gazalkent new Students/gazalkent_chemistry.html', show=show, user=user)


@app.route('/xojakent_student_physics')
def xojakent_physics():
    user = get_current_user()
    try:
        if not user.director and not user.xojakent_admin:
            return redirect(url_for('home'))
    except AttributeError:
        return redirect(url_for('home'))
    show = Student.query.order_by('age').all()
    return render_template('Xojakent new students/xojaknet_physics.html', show=show, user=user)


@app.route('/gazalkent_student_physics')
def gazalkent_physics():
    user = get_current_user()
    try:
        if not user.director and not user.gazalkent_admin:
            return redirect(url_for('home'))
    except AttributeError:
        return redirect(url_for('home'))
    show = Student.query.order_by('age').all()
    return render_template('Gazalkent new Students/gazalkent_physics.html', show=show, user=user)


@app.route('/gazalkent_student_biology')
def gazalkent_biology():
    user = get_current_user()
    try:
        if not user.director and not user.gazalkent_admin:
            return redirect(url_for('home'))
    except AttributeError:
        return redirect(url_for('home'))
    show = Student.query.order_by('age').all()
    return render_template('Gazalkent new Students/gazalkent biology.html', show=show, user=user)


@app.route('/xojakent_student_biology')
def xojakent_biology():
    user = get_current_user()
    try:
        if not user.director and not user.xojakent_admin:
            return redirect(url_for('home'))
    except AttributeError:
        return redirect(url_for('home'))
    show = Student.query.order_by('age').all()
    return render_template('Xojakent new students/xojakent biology.html', show=show, user=user)


@app.route('/register_teacher', methods=['POST', 'GET'])
def register_teacher():
    user = get_current_user()
    try:
        if not user.xojakent_admin and not user.director and not user.gazalkent_admin:
            return redirect(url_for('home'))
    except AttributeError:
        return redirect(url_for('home'))
    teacher = get_current_teacher()
    if request.method == 'POST':
        teacher_name = request.form.get('name').upper()
        teacher_surname = request.form.get('surname').upper()
        teacher_age = request.form.get('age')
        teacher_location = request.form.get('location')
        teacher_username = request.form.get('username')
        teacher_hashed_password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')
        teacher_phone = request.form.get('phone')
        otasining_ismi = request.form.get('father_name')
        teacher_subject = request.form.get('subject_1')
        if Teachers.query.filter_by(username=teacher_username).first():
            return "This username is already token"
        if teacher_name == "":
            abort(422)
        elif teacher_surname == "":
            abort(422)
        elif teacher_age == "":
            abort(422)

        if teacher_hashed_password != confirm_password:
            return "Parolingiz bir biriga to'g'ri kelmadi"
        hash = generate_password_hash(confirm_password,method='sha256')
        if teacher_location == "xojakent":
            teacher_location = 1
            num = 1
            total = All_teachers.teachers + num
            All_teachers.query.filter_by(id=1).update({'teachers': total})
        elif teacher_location == "gazalkent":
            teacher_location = 2
            num = 1
            total = All_teachers.teachers + num
            All_teachers.query.filter_by(id=1).update({'teachers': total})

        if teacher_subject == "Ingliz tili":
            teacher_subject = 'Ingliz tili'
        elif teacher_subject == "Rus tili":
            teacher_subject = 'Rus tili'
        elif teacher_subject == "Matematika":
            teacher_subject = 'Matematika'
        elif teacher_subject == "Tarix":
            teacher_subject = 'Tarix'
        elif teacher_subject == "Kimyo":
            teacher_subject = 'Kimyo'
        elif teacher_subject == "Fizika":
            teacher_subject = 'Fizika'
        elif teacher_subject == "Ona tili va Adabiyot":
            teacher_subject = 'Ona tili va Adabiyot'
        elif teacher_subject == "Biologiya":
            teacher_subject = 'Biologiya'
        elif teacher_subject == "Uy xamshiraligi":
            teacher_subject = "Uy xamshiraligi"
        add = Teachers(name=teacher_name,
                       surname=teacher_surname,
                       age=teacher_age,
                       locations=teacher_location,
                       username=teacher_username,
                       password=hash,
                       subject=teacher_subject,
                       phone=teacher_phone,
                       teacher=True,
                       number_groups=0,
                       otasining_ismi=otasining_ismi
                       )
        add.add_teacher()
    return render_template('base template/Register_teacher.html', user=user, teacher=teacher)


@app.route('/join_group', methods=['POST', 'GET'])
def add_group():
    teacher = get_current_teacher()
    user = get_current_user()
    try:
        if not user.xojakent_admin and not user.director and not user.gazalkent_admin:
            return redirect(url_for('home'))
    except AttributeError:
        return redirect(url_for('home'))
    if request.method == 'POST':
        name = request.form.get('group')

        calc = Student.query.filter_by(for_group=True).all()
        calculate = len(calc)
        all = Groups.number_students + calculate
        Groups.query.filter_by(name=name).update({'number_students': all})
        db.session.commit()

        query = Student.query.filter_by(for_group=True).first()
        show = Groups.query.filter_by(name=name).all()
        for i in show:
            if query.group1 is None and query.group2 is None and query.group3 is None:
                if i.subject == query.subject_1:
                    Student.query.filter_by(for_group=True).update(
                        {'group1': i.id, 'for_group': False, 'subject_1': None})
                    db.session.commit()
                elif i.subject == query.subject_2:
                    Student.query.filter_by(for_group=True).update(
                        {'group1': i.id, 'for_group': False, 'subject_2': None})
                    db.session.commit()
                elif i.subject == query.subject_3:
                    Student.query.filter_by(for_group=True).update(
                        {'group1': i.id, 'for_group': False, 'subject_3': None})
                    db.session.commit()

            elif query.group1 is not None and query.group2 is None and query.group3 is None:
                if query.group1 == i.id:
                    return 'Bu gruppa band'
                else:
                    if i.subject == query.subject_1:
                        Student.query.filter_by(for_group=True).update(
                            {'group2': i.id, 'for_group': False, 'subject_1': None})
                        db.session.commit()
                    elif i.subject == query.subject_2:
                        Student.query.filter_by(for_group=True).update(
                            {'group2': i.id, 'for_group': False, 'subject_2': None})
                        db.session.commit()
                    elif i.subject == query.subject_3:
                        Student.query.filter_by(for_group=True).update(
                            {'group2': i.id, 'for_group': False, 'subject_3': None})
                        db.session.commit()

            elif query.group1 is not None and query.group2 is not None and query.group3 is None:
                if query.group1 == i.id:
                    return 'Bu gruppa band'
                elif query.group2 == i.id:
                    return 'Bu gruppa band'
                else:
                    if i.subject == query.subject_1:
                        Student.query.filter_by(for_group=True).update(
                            {'group3': i.id, 'for_group': False, 'subject_1': None})
                        db.session.commit()
                    elif i.subject == query.subject_2:
                        Student.query.filter_by(for_group=True).update(
                            {'group3': i.id, 'for_group': False, 'subject_2': None})
                        db.session.commit()
                    elif i.subject == query.subject_3:
                        Student.query.filter_by(for_group=True).update(
                            {'group3': i.id, 'for_group': False, 'subject_3': None})
                        db.session.commit()
    experts = Teachers.query.filter_by(teacher=True).all()
    student = Student.query.filter_by(director=False, xojakent_admin=False, gazalkent_admin=False, for_group=True)
    groups = Groups.query.order_by("id").all()
    students = Student.query.order_by('id').all()
    return render_template('Groups/add_group.html', user=user, teachers=experts, student=student, groups=groups,
                           students=students, teacher=teacher)


@app.route('/teachers2')
def teacher2():
    user = get_current_user()
    try:
        if not user.xojakent_admin and not user.director and not user.gazalkent_admin:
            return redirect(url_for('home'))
    except AttributeError:
        return redirect(url_for('home'))
    teachers = Teachers.query.order_by('id').all()
    user1 = Student.query.order_by('id').all()
    return render_template('Teacher/teachers2.html', user=user, teachers=teachers, user1=user1)


@app.route('/teacher_profile/<int:id>')
def teacher_profile(id):
    user = get_current_user()
    try:
        if not user.xojakent_admin and not user.director and not user.gazalkent_admin:
            return redirect(url_for('home'))
    except AttributeError:
        return redirect(url_for('home'))
    teacher = Teachers.query.filter_by(id=id)
    groups = Groups.query.filter_by(teacher_1=id).all()
    return render_template('Teacher/teacher_information.html',user=user,teacher=teacher,groups=groups)


@app.route('/student_profile2/<student_id>')
def student_profile2(student_id):
    user = get_current_user()
    try:
        if not user.xojakent_admin and not user.director and not user.gazalkent_admin:
            return redirect(url_for('home'))
    except AttributeError:
        return redirect(url_for('home'))
    student = Student.query.filter_by(id=student_id).all()
    for i in student:
        group_name1 = Groups.query.filter_by(id=i.group1).all()
        group_name2 = Groups.query.filter_by(id=i.group2).all()
        group_name3 = Groups.query.filter_by(id=i.group3).all()

        return render_template('student/student_profile2.html', student_q=student, group_name1=group_name1,
                               group_name2=group_name2,
                               group_name3=group_name3)
