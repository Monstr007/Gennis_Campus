from app import get_current_user, render_template, redirect, url_for, db, app, request, or_
from models import Student, Teachers, Groups, Attendance, All_Charity_Sums, All_students, All_teachers, \
    All_overhead, All_Capital_Expenditure, All_groups, Bank, reason_apset_days, due_days, All_withdrawal


@app.route('/profits')
def profits():
    user = get_current_user()
    try:
        if not user.gazalkent_admin and not user.director and not user.xojakent_admin:
            return redirect(url_for('home'))
    except AttributeError:
        return redirect(url_for('home'))
    charity = All_Charity_Sums.query.order_by('id').all()
    all_students = All_students.query.order_by('id').all()
    all_overhead = All_overhead.query.order_by('id').all()
    all_teachers = All_teachers.query.order_by('id').all()
    all_groups = All_groups.query.order_by('id').all()
    all_capital = All_Capital_Expenditure.query.order_by('id').all()
    banks = Bank.query.order_by('id').all()
    bank = Bank.query.filter_by(id=1).first()
    over = All_overhead.query.filter_by(id=1).first()
    capita = All_Capital_Expenditure.query.filter_by(id=1).first()
    witdh = All_withdrawal.query.filter_by(id=1).first()
    total = over.total_sum + capita.total_sum + witdh.total_sum
    polza = bank.cash - total
    return render_template('base template/profits.html', user=user, charity=charity, all_capital=all_capital,
                           all_overhead=all_overhead,
                           all_teachers=all_teachers, all_groups=all_groups, polza=polza, all_students=all_students,
                           banks=banks)


@app.route('/delete_teacher/<teacher_id>')
def delete_teacher(teacher_id):
    user = get_current_user()
    try:
        if not user.director:
            return redirect(url_for('home'))
    except AttributeError:
        return redirect(url_for('home'))
    delete = Teachers.query.filter_by(id=teacher_id).first()
    delete.delete()
    num = 1
    total = All_teachers.teachers - num
    All_teachers.query.filter_by(id=1).update({'teachers': total})
    return redirect(url_for('teacher'))


@app.route('/teachers')
def teacher():
    user = get_current_user()
    try:
        if not user.director:
            return redirect(url_for('home'))
    except AttributeError:
        return redirect(url_for('home'))
    teachers = Teachers.query.order_by('id').all()
    user1 = Student.query.order_by('id').all()
    return render_template('Teacher/teachers.html', user=user, teachers=teachers, user1=user1)


@app.route('/giving_charity/<id>', methods=['POST'])
def give_charity(id):
    user = get_current_user()
    try:
        if not user.director:
            return redirect(url_for('home'))
    except AttributeError:
        return redirect(url_for('home'))
    if request.method == "POST":
        charity = request.form.get('charity')
        Student.query.filter_by(id=id).update({'charity': charity})
        db.session.commit()
        return redirect(url_for('admin_users'))


@app.route('/admins')
def admin_users():
    user = get_current_user()
    try:
        if not user.director:
            return redirect(url_for('home'))
    except AttributeError:
        return redirect(url_for('home'))
    show = Student.query.order_by('id').all()
    return render_template('base template/admin users.html', show=show, user=user)


@app.route('/delete_user/<delete_id>')
def delete_user(delete_id):
    user = get_current_user()
    try:
        if not user.director:
            return redirect(url_for('home'))
    except AttributeError:
        return redirect(url_for('home'))
    delete = Student.query.filter_by(id=delete_id).first()
    delete.delete()
    num = 1
    total = All_students.students - num
    All_students.query.filter_by(id=1).update({'students': total})
    return redirect(url_for('admin_users'))


@app.route('/make_admin_xojakent/<int:admin_id>')
def admin(admin_id):
    user = get_current_user()
    try:
        if not user.director:
            return redirect(url_for('home'))
    except AttributeError:
        return redirect(url_for('home'))
    Student.query.filter_by(id=admin_id).update({'xojakent_admin': True})
    db.session.commit()
    return redirect(url_for('admin_users'))


@app.route('/kick_admin_xojakent/<int:admin_id>')
def admin_kick(admin_id):
    user = get_current_user()
    try:
        if not user.director:
            return redirect(url_for('home'))
    except AttributeError:
        return redirect(url_for('home'))
    Student.query.filter_by(id=admin_id).update({'xojakent_admin': False})
    db.session.commit()
    return redirect(url_for('admin_users'))


@app.route('/make_admin_gazalkent/<int:admin_id>')
def admin_gazalkent(admin_id):
    user = get_current_user()
    try:
        if not user.director:
            return redirect(url_for('home'))
    except AttributeError:
        return redirect(url_for('home'))
    Student.query.filter_by(id=admin_id).update({'gazalkent_admin': True})
    db.session.commit()
    return redirect(url_for('admin_users'))


@app.route('/kick_admin_gazalkent/<int:admin_id>')
def admin_kick_gazalkent(admin_id):
    user = get_current_user()
    try:
        if not user.director:
            return redirect(url_for('home'))
    except AttributeError:
        return redirect(url_for('home'))
    Student.query.filter_by(id=admin_id).update({'gazalkent_admin': False})
    db.session.commit()
    return redirect(url_for('admin_users'))


@app.route('/student_profile1/<student_id>')
def student_profile(student_id):
    user = get_current_user()
    try:
        if not user.director:
            return redirect(url_for('home'))
    except AttributeError:
        return redirect(url_for('home'))
    student = Student.query.filter_by(id=student_id).all()
    for i in student:
        group_name1 = Groups.query.filter_by(id=i.group1).all()
        group_name2 = Groups.query.filter_by(id=i.group2).all()
        group_name3 = Groups.query.filter_by(id=i.group3).all()
        return render_template('student/student_profile.html', student_q=student, group_name1=group_name1,
                               group_name2=group_name2,
                               group_name3=group_name3)


@app.route('/absent_days/<student_id>')
def absent(student_id):
    user = get_current_user()
    try:
        if not user.director:
            return redirect(url_for('home'))
    except AttributeError:
        return redirect(url_for('home'))
    attendance = Attendance.query.filter_by(student_id=student_id).all()
    student = Student.query.filter_by(id=student_id).first()
    group = Groups.query.filter(or_(Groups.id == student.group1, Groups.id == student.group2,
                                    Groups.id == student.group3))
    for i in group:
        teacher = i.teacher_1
        return render_template('base template/absent students1.html', teacher=teacher, group=group, attendance=attendance,
                               student=student,
                               id=student_id)
    return render_template('base template/absent students1.html', user=user, attendance=attendance, id=student_id)


@app.route('/delete_days/<day_id><student_id>')
def delete_days(day_id, student_id):
    user = get_current_user()
    try:
        if not user.director:
            return redirect(url_for('home'))
    except AttributeError:
        return redirect(url_for('home'))
    delete = Attendance.query.filter(Attendance.id == day_id).first()
    delete.delete()
    query = Student.query.filter_by(id=student_id).first()
    group = Groups.query.filter(or_(Groups.id == query.group1, Groups.id == query.group2, Groups.id == query.group3))
    for i in group:
        query_teacher = Teachers.query.filter_by(id=i.teacher_1).first()
        slesh = i.cost / 13
        boluv = slesh / 2
        plus = query.money + slesh
        minus = query_teacher.salary - boluv
        Student.query.filter_by(id=student_id).update({'money': plus})
        Teachers.query.filter_by(id=i.teacher_1).update({'salary': minus})
        db.session.commit()
        qosh = query.charity
        total = All_Charity_Sums.bank_charity - qosh
        All_Charity_Sums.query.filter_by(id=1).update({'bank_charity': total})
        db.session.commit()

    return redirect(url_for('student_profile'))


@app.route('/new_students')
def new_students():
    user = get_current_user()
    try:
        if not user.director:
            return redirect(url_for('home'))
    except AttributeError:
        return redirect(url_for('home'))
    return render_template('base template/new students.html', user=user)


@app.route('/get_id/<check_id>', methods=["POST"])
def get_id(check_id):
    completed = request.get_json()['completed']
    todo_id = Attendance.query.get(check_id)
    todo_id.for_sabab = completed
    db.session.commit()
    return redirect(url_for('due_days1'))


@app.route('/sababli_qilish')
def sababli_qilish():
    user = get_current_user()
    try:
        if not user.director:
            return redirect(url_for('home'))
    except AttributeError:
        return redirect(url_for('home'))
    get_student = reason_apset_days.query.order_by('student_id').all()
    for i in get_student:
        query = Student.query.filter_by(id=i.student_id).all()
        return render_template('base template/Sababli_qilish.html', user=user, query=query)
    return render_template('base template/Sababli_qilish.html', user=user)


@app.route('/show_due_days<int:student_id>')
def show_due_days(student_id):
    user = get_current_user()
    try:
        if not user.director:
            return redirect(url_for('home'))
    except AttributeError:
        return redirect(url_for('home'))
    query = Attendance.query.filter_by(student_id=student_id,for_sabab=True).all()
    show = reason_apset_days.query.filter_by(student_id=student_id).all()
    return render_template('base template/Show_due_days.html', user=user, query=query, show=show)


@app.route('/commit<int:student_id><int:id_reason>')
def commit_due(student_id,id_reason):
    user  = get_current_user()
    try:
        if not user.director:
            return redirect(url_for('home'))
    except AttributeError:
        return redirect(url_for('home'))
    query = reason_apset_days.query.filter_by(id=id_reason).all()
    query_apsets = Attendance.query.filter_by(student_id=student_id,for_sabab=True).delete()
    db.session.commit()
    query1 = reason_apset_days.query.filter_by(id=id_reason).delete()
    db.session.commit()
    for items in query:

        add2 = due_days(group_id_student=items.group_id,
                        img_due_days=items.img_due_days, id_of_student=items.student_id,
                        date_of_absent=items.date_abset,
                        reason_due=items.reason_due)
        db.session.add(add2)
        db.session.commit()
    query = Student.query.filter_by(id=student_id).first()
    group = Groups.query.filter(or_(Groups.id == query.group1, Groups.id == query.group2, Groups.id == query.group3))
    for i in group:
        query_teacher = Teachers.query.filter_by(id=i.teacher_1).first()
        slesh = i.cost / 13 + query.charity
        boluv = slesh / 2
        plus = query.money + slesh
        minus = query_teacher.selery - boluv
        Student.query.filter_by(id=student_id).update({'money': plus})
        Teachers.query.filter_by(id=i.teacher_1).update({'salary': minus})
        db.session.commit()

        query_charity = All_Charity_Sums.query.order_by('id').first()
        minus = query_charity.bank_charity - query.charity
        All_Charity_Sums.query.update({'bank_charity': minus})
        db.session.commit()

    return redirect(url_for('sababli_qilish'))


@app.route('/refuse<int:student_id><int:id_reason>')
def refuse_due(student_id,id_reason):
    user = get_current_user()
    try:
        if not user.director:
            return redirect(url_for('home'))
    except AttributeError:
        return redirect(url_for('home'))
    Attendance.query.filter_by(student_id=student_id, for_sabab=True).update({'for_sabab': False})
    db.session.commit()
    query = reason_apset_days.query.filter_by(id=id_reason).delete()
    db.session.commit()
    return redirect(url_for('sababli_qilish'))
