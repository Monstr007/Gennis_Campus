from app import app,get_current_user,get_current_teacher,or_,redirect,render_template,request,url_for,db
from models import Student,Groups, Teachers, All_students, Deleted_students


@app.route('/manage/<int:id>', methods=['POST', 'GET'])
def manage(id):
    user = get_current_user()
    try:
        if not user.gazalkent_admin and not user.director and not user.xojakent_admin:
            return redirect(url_for('home'))
    except AttributeError:
        return redirect(url_for('home'))
    teacher = get_current_teacher()
    groups = Groups.query.filter_by(id=id).all()
    experts = Teachers.query.filter_by(teacher=True).all()
    for group in groups:
        student = Student.query.filter(or_(Student.group1 == group.id,Student.group2 == group.id,Student.group3==group.id))
        if user.locations ==1:
            return render_template('Groups/manage_group.html',students=student,groups=groups, user=user,teachers=experts)
        elif user.locations == 2:
            return render_template('Groups/manage_group2.html', students=student, groups=groups, user=user,
                                   teachers=experts)

    return render_template('Groups/manage_group.html',groups=groups,user=user, teachers=experts)


@app.route('/show_group/<int:group_id>', methods=['POST', 'GET'])
def show_group(group_id):
    user = get_current_user()
    try:
        if not user.gazalkent_admin and not user.director and not user.xojakent_admin:
            return redirect(url_for('home'))
    except AttributeError:
        return redirect(url_for('home'))
    teacher = get_current_teacher()
    query_groups = Groups.query.order_by('id').all()
    query_students = Student.query.filter_by(for_moved=True).order_by('id').all()
    if user.locations == 1:
        return render_template('Groups/Show_group.html', groups=query_groups, old_id=group_id, students=query_students,
                               user=user)
    elif user.locations == 2:
        return render_template('Groups/Show_group2.html', groups=query_groups, old_id=group_id,students=query_students,user=user)


@app.route('/check_moved/<check_id>', methods=["POST"])
def check_moved(check_id):
    completed = request.get_json()['completed']
    todo_id = Student.query.get(check_id)
    todo_id.for_moved = completed
    db.session.commit()
    return redirect(url_for('attendance'))


@app.route('/move_to_group/<int:old_id>/<int:group_id>')
def move_to_group(old_id,group_id):
    user = get_current_user()
    try:
        if not user.gazalkent_admin and not user.director and not user.xojakent_admin:
            return redirect(url_for('home'))
    except AttributeError:
        return redirect(url_for('home'))
    query = Student.query.filter_by(for_moved=True).first()
    query_group = Groups.query.filter_by(id=group_id).all()
    old_group = Groups.query.filter_by(id=old_id).first()
    for i in query_group:
        if query.group1 == old_group.id:
            Student.query.filter_by(for_moved=True).update({'group1': i.id, 'for_moved': False})
            db.session.commit()

        elif query.group2 == old_group.id:
            if query.group1 == i.id:
                return 'Bu gruppa band'
            else:
                Student.query.filter_by(for_moved=True).update({'group2': i.id, 'for_moved': False})
                db.session.commit()

        elif query.group3 == old_group.id:
            if query.group1 == i.id:
                return 'Bu gruppa band'
            elif query.group2 == i.id:
                return 'Bu gruppa band'
            else:
                Student.query.filter_by(for_moved=True).update({'group3': i.id, 'for_moved': False})
                db.session.commit()
    print(old_group.id)
    if old_group.location == 1:
        return redirect(url_for('inside_of_group',id=old_id))
    elif old_group.location == 2:
        return redirect(url_for('inside_of_group2',id=old_id))


@app.route('/del_name_group<int:id>')
def del_name_group(id):
    user = get_current_user()
    try:
        if not user.gazalkent_admin and not user.director and not user.xojakent_admin:
            return redirect(url_for('home'))
    except AttributeError:
        return redirect(url_for('home'))
    query = Groups.query.filter_by(id=id).first()
    Groups.query.filter_by(id=id).update({'old_name':query.name,
                                         'name': ''})

    db.session.commit()

    return redirect(url_for('manage', id=id))


@app.route('/rename_group<int:id>', methods=["POST"])
def rename_group(id):
    user = get_current_user()
    try:
        if not user.gazalkent_admin and not user.director and not user.xojakent_admin:
            return redirect(url_for('home'))
    except AttributeError:
        return redirect(url_for('home'))
    name = request.form.get('name')
    Groups.query.filter_by(id=id).update({'name': name})
    db.session.commit()

    return redirect(url_for('manage', id=id))


@app.route('/delete_page<int:id>')
def delete_page(id):
    user = get_current_user()
    try:
        if not user.gazalkent_admin and not user.director and not user.xojakent_admin:
            return redirect(url_for('home'))
    except AttributeError:
        return redirect(url_for('home'))
    student = Student.query.filter_by(id=id).first()
    return render_template('student/deleted_students.html',user=user, student_id=student)


@app.route('/deleted_students<int:id>',methods=["POST","GET"])
def deleted_students(id):
    user = get_current_user()
    try:
        if not user.gazalkent_admin and not user.director and not user.xojakent_admin:
            return redirect(url_for('home'))
    except AttributeError:
        return redirect(url_for('home'))
    reason = request.form.get('reason')
    query_student = Student.query.filter_by(id=id).first()
    add = Deleted_students(reason=reason,student_name=query_student.name,
                           student_id=query_student.id,student_phone=query_student.phone,
                           student_surname=query_student.surname,student_parent_phone=query_student.father_phone)

    db.session.add(add)
    db.session.commit()
    num = 1
    total = All_students.students - num
    All_students.query.filter_by(id=1).update({'students': total})
    db.session.commit()
    query_student.delete()
    return render_template('base template/home.html', user=user)