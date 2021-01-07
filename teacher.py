from app import app, get_current_teacher, get_current_user, render_template, redirect, url_for, request, or_, db
from models import Teachers, Groups, Student, Attendance, All_Charity_Sums, Teacher_cash
from datetime import datetime


@app.route('/info_teacher')
def info_teacher():
    teacher = get_current_teacher()
    try:
        if not teacher:
            return redirect(url_for('home'))
    except AttributeError:
        return redirect(url_for('home'))
    user = get_current_user()
    users = Teachers.query.filter_by(id=teacher.id)
    return render_template('Teacher/teacher_profile.html', teacher=teacher, users=users, user=user)


@app.route('/salaries')
def teacher_salary():
    teacher = get_current_teacher()
    try:
        if not teacher:
            return redirect(url_for('home'))
    except AttributeError:
        return redirect(url_for('home'))
    user = get_current_user()
    teacher_info = Teachers.query.filter_by(id=teacher.id).first()
    cash = Teacher_cash.query.filter_by(teacher_id=teacher.id)
    return render_template('Teacher/teacher_salary.html',teacher=teacher,teacher_info=teacher_info,cash=cash,user=user)


@app.route('/my_group1')
def my_group1():
    teacher = get_current_teacher()
    try:
        if not teacher:
            return redirect(url_for('home'))
    except AttributeError:
        return redirect(url_for('home'))
    user = get_current_user()
    groups = Groups.query.filter_by(teacher_1=teacher.id).first()
    teach = Teachers.query.filter_by(id=teacher.id).all()
    for gr1 in teach:
        group = Groups.query.filter_by(id=gr1.group1)
        for gr in group:
            query = Student.query.filter(or_(Student.group1 == gr.id, Student.group2 == gr.id,
                                             Student.group3 == gr.id)).order_by('id')
            return render_template('Teacher/my groups.html', groups=groups, group=group, teacher=teacher, user=user,
                                   query=query)
    return render_template('Teacher/my groups.html', groups=groups, teacher=teacher, user=user)


@app.route('/my_group2')
def my_group2():
    teacher = get_current_teacher()
    try:
        if not teacher:
            return redirect(url_for('home'))
    except AttributeError:
        return redirect(url_for('home'))
    user = get_current_user()
    groups = Groups.query.filter_by(teacher_1=teacher.id).first()
    teach = Teachers.query.filter_by(id=teacher.id).all()
    for gr1 in teach:
        group = Groups.query.filter_by(id=gr1.group2)
        for gr in group:
            query = Student.query.filter(or_(Student.group1 == gr.id, Student.group2 == gr.id,
                                             Student.group3 == gr.id)).order_by('id')
            return render_template('Teacher/mt groups2.html', groups=groups, group=group, teacher=teacher, user=user,
                                   query=query)
    return render_template('Teacher/mt groups2.html', groups=groups, teacher=teacher, user=user)


@app.route('/my_group3')
def my_group3():
    teacher = get_current_teacher()
    try:
        if not teacher:
            return redirect(url_for('home'))
    except AttributeError:
        return redirect(url_for('home'))
    user = get_current_user()
    groups = Groups.query.filter_by(teacher_1=teacher.id).first()
    teach = Teachers.query.filter_by(id=teacher.id).all()
    for gr1 in teach:
        group = Groups.query.filter_by(id=gr1.group3)
        for gr in group:
            query = Student.query.filter(or_(Student.group1 == gr.id, Student.group2 == gr.id,
                                             Student.group3 == gr.id)).order_by('id')
            return render_template('Teacher/my group3.html', groups=groups, group=group, teacher=teacher, user=user,
                                   query=query)
    return render_template('Teacher/my group3.html', groups=groups, teacher=teacher, user=user)


@app.route('/my_group4')
def my_group4():
    teacher = get_current_teacher()
    try:
        if not teacher:
            return redirect(url_for('home'))
    except AttributeError:
        return redirect(url_for('home'))
    user = get_current_user()
    groups = Groups.query.filter_by(teacher_1=teacher.id).first()
    teach = Teachers.query.filter_by(id=teacher.id).all()
    for gr1 in teach:
        group = Groups.query.filter_by(id=gr1.group4)
        for gr in group:
            query = Student.query.filter(or_(Student.group1 == gr.id, Student.group2 == gr.id,
                                             Student.group3 == gr.id)).order_by('id')
            return render_template('Teacher/mygroup4.html', groups=groups, group=group, teacher=teacher, user=user,
                                   query=query)
    return render_template('Teacher/mygroup4.html', groups=groups, teacher=teacher, user=user)


@app.route('/my_group5')
def my_group5():
    teacher = get_current_teacher()
    try:
        if not teacher:
            return redirect(url_for('home'))
    except AttributeError:
        return redirect(url_for('home'))
    user = get_current_user()
    groups = Groups.query.filter_by(teacher_1=teacher.id).first()
    teach = Teachers.query.filter_by(id=teacher.id).all()
    for gr1 in teach:
        group = Groups.query.filter_by(id=gr1.group5)
        for gr in group:
            query = Student.query.filter(or_(Student.group1 == gr.id, Student.group2 == gr.id,
                                             Student.group3 == gr.id)).order_by('id')
            return render_template('Teacher/my group5.html', groups=groups, group=group, teacher=teacher, user=user,
                                   query=query)
    return render_template('Teacher/my group5.html', groups=groups, teacher=teacher, user=user)


@app.route('/my_group6')
def my_group6():
    teacher = get_current_teacher()
    try:
        if not teacher:
            return redirect(url_for('home'))
    except AttributeError:
        return redirect(url_for('home'))
    user = get_current_user()
    groups = Groups.query.filter_by(teacher_1=teacher.id).first()
    teach = Teachers.query.filter_by(id=teacher.id).all()
    for gr1 in teach:
        group = Groups.query.filter_by(id=gr1.group6)
        for gr in group:
            query = Student.query.filter(or_(Student.group1 == gr.id, Student.group2 == gr.id,
                                             Student.group3 == gr.id)).order_by('id')
            return render_template('Teacher/my group6.html', groups=groups, group=group, teacher=teacher, user=user,
                                   query=query)
    return render_template('Teacher/my group6.html', groups=groups, teacher=teacher, user=user)


@app.route('/my_group7')
def my_group7():
    teacher = get_current_teacher()
    try:
        if not teacher:
            return redirect(url_for('home'))
    except AttributeError:
        return redirect(url_for('home'))
    user = get_current_user()
    groups = Groups.query.filter_by(teacher_1=teacher.id).first()
    teach = Teachers.query.filter_by(id=teacher.id).all()
    for gr1 in teach:
        group = Groups.query.filter_by(id=gr1.group7)
        for gr in group:
            query = Student.query.filter(or_(Student.group1 == gr.id, Student.group2 == gr.id,
                                             Student.group3 == gr.id)).order_by('id')
            return render_template('Teacher/my group7.html', groups=groups, group=group, teacher=teacher, user=user,
                                   query=query)
    return render_template('Teacher/my group7.html', groups=groups, teacher=teacher, user=user)


@app.route('/my_group8')
def my_group8():
    teacher = get_current_teacher()
    try:
        if not teacher:
            return redirect(url_for('home'))
    except AttributeError:
        return redirect(url_for('home'))
    user = get_current_user()
    groups = Groups.query.filter_by(teacher_1=teacher.id).first()
    teach = Teachers.query.filter_by(id=teacher.id).all()
    for gr1 in teach:
        group = Groups.query.filter_by(id=gr1.group8)
        for gr in group:
            query = Student.query.filter(or_(Student.group1 == gr.id, Student.group2 == gr.id,
                                             Student.group3 == gr.id)).order_by('id')
            return render_template('Teacher/my group 8.html', groups=groups, group=group, teacher=teacher, user=user,
                                   query=query)
    return render_template('Teacher/my group 8.html', groups=groups, teacher=teacher, user=user)


@app.route('/my_group9')
def my_group9():
    teacher = get_current_teacher()
    try:
        if not teacher:
            return redirect(url_for('home'))
    except AttributeError:
        return redirect(url_for('home'))
    user = get_current_user()
    groups = Groups.query.filter_by(teacher_1=teacher.id).first()
    teach = Teachers.query.filter_by(id=teacher.id).all()
    for gr1 in teach:
        group = Groups.query.filter_by(id=gr1.group9)
        for gr in group:
            query = Student.query.filter(or_(Student.group1 == gr.id, Student.group2 == gr.id,
                                             Student.group3 == gr.id)).order_by('id')
            return render_template('Teacher/my group9.html', groups=groups, group=group, teacher=teacher, user=user,
                                   query=query)
    return render_template('Teacher/my group9.html', groups=groups, teacher=teacher, user=user)


@app.route('/my_group10')
def my_group10():
    teacher = get_current_teacher()
    try:
        if not teacher:
            return redirect(url_for('home'))
    except AttributeError:
        return redirect(url_for('home'))
    user = get_current_user()
    groups = Groups.query.filter_by(teacher_1=teacher.id).first()
    teach = Teachers.query.filter_by(id=teacher.id).all()
    for gr1 in teach:
        group = Groups.query.filter_by(id=gr1.group10)
        for gr in group:
            query = Student.query.filter(or_(Student.group1 == gr.id,
                                             Student.group2 == gr.id, Student.group3 == gr.id)).order_by('id')
            return render_template('Teacher/my group10.html', groups=groups, group=group, teacher=teacher, user=user,
                                   query=query)
    return render_template('Teacher/my group10.html', groups=groups, teacher=teacher, user=user)


@app.route('/attendence_1<int:student_id><int:group_id>', methods=["POST", "GET"])
def attendance_1(student_id,group_id):
    user = get_current_user()
    teacher = get_current_teacher()
    try:
        if not teacher:
            return redirect(url_for('home'))
    except AttributeError:
        return redirect(url_for('home'))
    if request.method == 'POST':
        query = Student.query.filter_by(attendance=True).first()
        query2 = Groups.query.filter_by(id=group_id).first()
        group = Groups.query.filter(
            or_(Groups.id == query.group1, Groups.id == query.group2, Groups.id == query.group3)).first()
        query_teacher = Teachers.query.filter_by(id=group.teacher_1).first()
        query_teacher1 = Teachers.query.filter_by(id=teacher.id).first()
        slesh = group.cost / 13 + query.charity
        boluv = slesh / 2
        if query_teacher.salary is None:
            salery = boluv
        else:
            salery = query_teacher.salary + boluv
        if query.money is None:
            plus2 = -slesh
        else:
            plus2 = query.money - slesh
        get_date = datetime.now()
        if teacher.subject == 'Ingliz tili' or teacher.subject == 'Rus tili':
            get_homework = int(request.form.get('homework'))
            get_dictonary = int(request.form.get('dictionary'))
            get_class_activity = int(request.form.get('active'))
            plus1 = get_homework + get_dictonary + get_class_activity
            boluv2 = plus1 / 3
            add = Attendance(group_id=group_id, student_id=student_id, teacher_id=teacher.id,
                             darsga_tayyorgarligi=get_homework, lugat=get_dictonary,
                             darsda_qatnashishi=get_class_activity,
                             ortacha_baho=boluv2,
                             present=get_date, fan=group.subject, apset=None)
            db.session.add(add)
            db.session.commit()
            print(teacher.subject)
        elif teacher.subject == 'Matematika' or teacher.subject == 'Tarix' or \
                teacher.subject == 'Fizika' or teacher.subject == 'Ona tili va Adabiyot' \
                or teacher.subject == 'Biologiya':
            get_homework2 = int(request.form.get('homework'))
            get_class_activity2 = int(request.form.get('active'))
            plus3 = get_homework2 + get_class_activity2
            boluv3 = plus3 / 2
            add2 = Attendance(group_id=group_id, student_id=student_id, teacher_id=teacher.id,
                             darsga_tayyorgarligi=get_homework2,
                             darsda_qatnashishi=get_class_activity2,
                             ortacha_baho=boluv3,lugat=0,
                             present=get_date, fan=group.subject, apset=None)
            db.session.add(add2)
            db.session.commit()
            print(teacher.subject)
        Student.query.filter_by(attendance=True).update({'money': plus2,
                                                         'attendance': False})
        Teachers.query.filter_by(id=group.teacher_1).update({'salary': salery})
        db.session.commit()
        query_charity = All_Charity_Sums.query.order_by('bank_charity').first()

        plus_charity = query_charity.bank_charity + query.charity
        All_Charity_Sums.query.update({'bank_charity': plus_charity})
        db.session.commit()

        if query2.id == query_teacher1.group1:
            return redirect(url_for('my_group1'))
        elif query2.id == query_teacher1.group1:
            return redirect(url_for('my_group2'))
        elif query2.id == query_teacher1.group1:
            return redirect(url_for('my_group3'))
        elif query2.id == query_teacher1.group1:
            return redirect(url_for('my_group4'))
        elif query2.id == query_teacher1.group1:
            return redirect(url_for('my_group5'))
        elif query2.id == query_teacher1.group1:
            return redirect(url_for('my_group6'))
        elif query2.id == query_teacher1.group1:
            return redirect(url_for('my_group7'))
        elif query2.id == query_teacher1.group1:
            return redirect(url_for('my_group8'))
        elif query2.id == query_teacher1.group1:
            return redirect(url_for('my_group9'))
        elif query2.id == query_teacher1.group1:
            return redirect(url_for('my_group10'))
    groups = Groups.query.filter_by(teacher_1=teacher.id).all()
    for i in groups:
        student = Student.query.filter(or_(Student.group1 == i.id, Student.group2 == i.id, Student.group3 == i.id))
        return render_template('Teacher/my groups.html', user=user, teacher=teacher, groups=groups, students=student)

    return render_template('Teacher/my groups.html', user=user, teacher=teacher, groups=groups)


@app.route('/attendance_3<int:student_id><int:group_id>', methods=['POST', 'GET'])
def attendance_3(student_id,group_id):
    user = get_current_user()
    teacher = get_current_teacher()
    try:
        if not teacher:
            return redirect(url_for('home'))
    except AttributeError:
        return redirect(url_for('home'))
    if request.method == 'POST':
        query2 = Groups.query.filter_by(id=group_id).first()
        query = Student.query.filter_by(id=student_id).first()
        group = Groups.query.filter(or_(Groups.id == query.group1, Groups.id == query.group2,
                                        Groups.id == query.group3)).first()
        query_teacher1 = Teachers.query.filter_by(id=teacher.id).first()
        query_teacher = Teachers.query.filter_by(id=group.teacher_1).first()
        slesh = group.cost / 13
        boluv = slesh / 2
        salery = query_teacher.salary + boluv
        plus = query.money - slesh + query.charity
        get_date = datetime.now()
        Student.query.filter_by(id=student_id).update({'money': plus})
        Teachers.query.filter_by(id=group.teacher_1).update({'salary': salery})
        db.session.commit()
        add = Attendance(group_id=group.id, student_id=student_id, teacher_id=teacher.id, present=None, apset=get_date)
        db.session.add(add)
        db.session.commit()
        query_charity = All_Charity_Sums.query.order_by('id').first()

        plus_charity = query_charity.bank_charity + query.charity
        All_Charity_Sums.query.update({'bank_charity': plus_charity})
        db.session.commit()
        if query2.id == query_teacher1.group1:
            return redirect(url_for('my_group1'))
        elif query2.id == query_teacher1.group1:
            return redirect(url_for('my_group2'))
        elif query2.id == query_teacher1.group1:
            return redirect(url_for('my_group3'))
        elif query2.id == query_teacher1.group1:
            return redirect(url_for('my_group4'))
        elif query2.id == query_teacher1.group1:
            return redirect(url_for('my_group5'))
        elif query2.id == query_teacher1.group1:
            return redirect(url_for('my_group6'))
        elif query2.id == query_teacher1.group1:
            return redirect(url_for('my_group7'))
        elif query2.id == query_teacher1.group1:
            return redirect(url_for('my_group8'))
        elif query2.id == query_teacher1.group1:
            return redirect(url_for('my_group9'))
        elif query2.id == query_teacher1.group1:
            return redirect(url_for('my_group10'))
    groups = Groups.query.filter_by(teacher_1=teacher.id).all()
    for i in groups:
        student = Student.query.filter(or_(Student.group1 == i.id, Student.group2 == i.id, Student.group3 == i.id))
        return render_template('Teacher/my groups.html', user=user, teacher=teacher, groups=groups, students=student)

    return render_template('Teacher/my groups.html', user=user, teacher=teacher, groups=groups)


@app.route('/check1/<check_id>', methods=["POST"])
def check2(check_id):
    completed = request.get_json()['completed']
    todo_id = Student.query.get(check_id)
    todo_id.attendance = completed
    db.session.commit()
    return redirect(url_for('my_group1'))


@app.route('/see_att/<id>')
def see_att(id):
    user = get_current_user()
    teacher = get_current_teacher()
    try:
        if not teacher:
            return redirect(url_for('home'))
    except AttributeError:
        return redirect(url_for('home'))
    attendance = Attendance.query.filter_by(student_id=id, teacher_id=teacher.id).order_by('id').all()
    return render_template('Teacher/student_att.html', user=user, teacher=teacher, attendance=attendance)


@app.route('/change_data/<id>')
def change_present(id):
    user = get_current_user()
    teacher = get_current_teacher()
    try:
        if not teacher:
            return redirect(url_for('home'))
    except AttributeError:
        return redirect(url_for('home'))
    pres = Attendance.query.filter_by(id=id).first()
    Attendance.query.filter_by(id=id).update({'apset': pres.present})
    Attendance.query.filter_by(id=id).update({'present': None})
    db.session.commit()
    return redirect(url_for('see_att', id=pres.student_id))


@app.route('/change_absent/<id>')
def change_absent(id):
    user = get_current_user()
    teacher = get_current_teacher()
    try:
        if not teacher:
            return redirect(url_for('home'))
    except AttributeError:
        return redirect(url_for('home'))
    pres = Attendance.query.filter_by(id=id).first()
    Attendance.query.filter_by(id=id).update({'present': pres.apset})
    Attendance.query.filter_by(id=id).update({'apset': None})
    db.session.commit()
    return redirect(url_for('see_att', id=pres.student_id))

