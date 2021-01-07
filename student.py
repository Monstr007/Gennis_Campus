from app import redirect, render_template, url_for, get_current_user, app, or_, request, get_current_teacher, PhotoForm, images, db
from models import Student, Groups, Attendance, reason_apset_days
from jinja2 import UndefinedError

@app.route('/info')
def info():
    user = get_current_user()
    try:
        if not user.gazalkent_admin and not user.director and not user.xojakent_admin and not user:
            return redirect(url_for('home'))
    except AttributeError:
        return redirect(url_for('home'))
    users = Student.query.filter_by(id=user.id).all()
    users2 = Student.query.filter_by(id=user.id).first()
    subject_1 = Groups.query.filter_by(id=users2.group1).first()
    subject_2 = Groups.query.filter_by(id=users2.group2).first()
    subject_3 = Groups.query.filter_by(id=users2.group3).first()

    for user1 in users:
        return render_template('base template/all_info.html', user=user, users=users,

                               subject_1=subject_1,subject_2=subject_2,subject_3=subject_3)
    return render_template('base template/all_info.html', user=user, users=users)


@app.route('/group1', methods=['POST', 'GET'])
def find_group():
    user = get_current_user()
    try:
        if not user:
            return redirect(url_for('home'))
    except AttributeError:
        return redirect(url_for('home'))
    student = Student.query.filter_by(id=user.id).first()
    groups = Groups.query.filter_by(id=student.group1)
    for st in groups:
        students = Student.query.filter(or_(Student.group1 == st.id, Student.group2 == st.id, Student.group3 == st.id))
        return render_template('student/student_group.html', students=students, user=user, groups=groups)
    return render_template('student/student_group.html', user=user, groups=groups)


@app.route('/group2', methods=['POST','GET'])
def find_group2():
    user = get_current_user()
    try:
        if not user:
            return redirect(url_for('home'))
    except AttributeError:
        return redirect(url_for('home'))
    student = Student.query.filter_by(id=user.id).first()
    groups = Groups.query.filter_by(id=student.group2)
    for st in groups:
        students = Student.query.filter(or_(Student.group1 == st.id, Student.group2 == st.id, Student.group3 == st.id))
        return render_template('student/st group2.html', students=students, user=user, groups=groups)
    return render_template('student/st group2.html', user=user, groups=groups)


@app.route('/group3', methods=['POST', 'GET'])
def find_group3():
    user = get_current_user()
    try:
        if not user:
            return redirect(url_for('home'))
    except AttributeError:
        return redirect(url_for('home'))
    student = Student.query.filter_by(id=user.id).first()
    groups = Groups.query.filter_by(id=student.group3)
    for st in groups:
        students = Student.query.filter(or_(Student.group1 == st.id, Student.group2 == st.id, Student.group3 == st.id))
        return render_template('student/st group3.html', students=students, user=user, groups=groups)
    return render_template('student/st group3.html', user=user, groups=groups)


@app.route('/my_attandance1',methods=['POST','GET'])
def find_attendance1():
    user = get_current_user()
    try:
        if not user:
            return redirect(url_for('home'))
    except AttributeError:
        return redirect(url_for('home'))
    try:
        student = Student.query.filter_by(id=user.id).first()
        groups = Groups.query.filter_by(id=student.group1).all()
        for st in groups:
            attendance1 = Attendance.query.filter_by(group_id=st.id).order_by('id').all()
            attendance2 = Attendance.query.filter_by(group_id=st.id).order_by('id').all()
            return render_template('student/my attendance.html', user=user, attendance=attendance1,attendance2=attendance2, groups=groups)
        return render_template('student/my attendance.html', user=user, groups=groups)
    except UndefinedError:
        return "Sizda birinchi guruh yo'q"


@app.route('/my_attandance2',methods=['POST', 'GET'])
def find_attendance2():
    user = get_current_user()
    try:
        if not user:
            return redirect(url_for('home'))
    except AttributeError:
        return redirect(url_for('home'))
    try:
        student = Student.query.filter_by(id=user.id).first()
        groups = Groups.query.filter_by(id=student.group2).all()
        for st in groups:
            attendance1 = Attendance.query.filter_by(group_id=st.id).order_by('id').all()
            attendance2 = Attendance.query.filter_by(group_id=st.id).order_by('id').all()
            return render_template('student/my att2.html', user=user, attendance=attendance1, attendance2=attendance2,
                                   groups=groups)
        return render_template('student/my att2.html', user=user, groups=groups)
    except UndefinedError:
        return "Sizda ikkinchi guruh yo'q"


@app.route('/my_attandance3',methods=['POST','GET'])
def find_attendance3():
    user = get_current_user()
    try:
        if not user:
            return redirect(url_for('home'))
    except AttributeError:
        return redirect(url_for('home'))
    try:
        student = Student.query.filter_by(id=user.id).first()
        groups = Groups.query.filter_by(id=student.group3)
        for st in groups:
            attendance1 = Attendance.query.filter_by(group_id=st.id).order_by('id').all()
            return render_template('student/my att3.html', user=user, attendance=attendance1, groups=groups)
        return render_template('student/my att3.html', user=user, groups=groups)
    except UndefinedError:
        return "Sizda uchinchi guruh yo'q"


@app.route('/apset_days<int:student_id><int:group_id>')
def apset_days(student_id,group_id):
    user = get_current_user()
    try:
        if not user:
            return redirect(url_for('home'))
    except AttributeError:
        return redirect(url_for('home'))
    apset_days = Attendance.query.filter_by(student_id=student_id,group_id=group_id).all()
    return render_template('student/apset_days.html',apset_days=apset_days,user=user)


@app.route('/due_days',methods=["POST","GET"])
def due_days1():
    user = get_current_user()
    try:
        if not user:
            return redirect(url_for('home'))
    except AttributeError:
        return redirect(url_for('home'))
    teacher = get_current_teacher()
    reason = request.form.get('reason')
    form = PhotoForm(meta={'csrf': False})
    get = Attendance.query.filter_by(for_sabab=True).first()
    if form.validate_on_submit():
        filename = images.save(form.image.data)
        image_url = images.url(filename)
        add = reason_apset_days(student_id=user.id,
                                img_due_days=image_url,reason_due=reason,
                                date_abset=get.apset,group_id=get.group_id)
        db.session.add(add)
        db.session.commit()

    return render_template('student/Sababli_kun.html', user=user, teacher=teacher,form=form, get=get)
