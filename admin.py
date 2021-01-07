from app import get_current_user, app, redirect, render_template, request, url_for, db, get_current_teacher, or_

from models import Teachers, Student, Groups


@app.route('/check3/<check_id>', methods=["POST"])
def check3(check_id):
    completed = request.get_json()['completed']
    todo_id = Teachers.query.get(check_id)
    todo_id.for_group = completed
    db.session.commit()
    return redirect(url_for('teacher2'))


@app.route('/all_groups')
def all_groups():
    user = get_current_user()
    try:
        if not user.xojakent_admin and not user.director:
            return redirect(url_for('home'))
    except AttributeError:
        return redirect(url_for('home'))
    groups = Groups.query.order_by('id').all()
    print(groups)
    for group in groups:
        teacher = Teachers.query.filter_by(id=group.teacher_1).first()

        return render_template('Groups/Groups.html',teacher_1=teacher, groups=groups, user=user)
    return render_template('Groups/Groups.html', groups=groups,user=user)


@app.route('/inside_of_group/<id>', methods=['POST', 'GET'])
def inside_of_group(id):
    user = get_current_user()
    try:
        if not user.xojakent_admin and not user.director:
            return redirect(url_for('home'))
    except AttributeError:
        return redirect(url_for('home'))
    groups = Groups.query.filter_by(id=id).all()
    experts = Teachers.query.filter_by(teacher=True).all()
    for group in groups:
        student = Student.query.filter(
            or_(Student.group1 == group.id, Student.group2 == group.id, Student.group3 == group.id))
        return render_template('Groups/Inside of Group.html', students=student, groups=groups, user=user,
                               teachers=experts)
    return render_template('Groups/Inside of Group.html', groups=groups, user=user, teachers=experts)


@app.route('/Groups_without_teacher')
def group_without_teacher():
    user = get_current_user()
    try:
        if not user.xojakent_admin and not user.director:
            return redirect(url_for('home'))
    except AttributeError:
        return redirect(url_for('home'))
    teacher = get_current_teacher()
    groups = Groups.query.filter_by(teacher_1=0).all()

    return render_template('Groups/Without Teacher.html', teacher=teacher,user=user, groups=groups)


@app.route('/delete_group/<int:id><int:gr>')
def delete_group(id,gr):
    user = get_current_user()
    try:
        if not user.xojakent_admin and not user.director and not user.gazalkent_admin:
            return redirect(url_for('home'))
    except AttributeError:
        return redirect(url_for('home'))
    del_gr = Groups.query.filter_by(id=id).first()
    students = Student.query.filter(or_(Student.group1 == id,Student.group2 ==id, Student.group3 == id))
    groups_n1 = Groups.query.filter_by(id=id).all()
    for q in groups_n1:
        for i in students:
            if i.group1 == id:
                if i.subject_1 is None:
                    Student.query.filter_by(group1=id).update({'group1': i.group2,
                                                               'group2': i.group3,
                                                               'group3': None,
                                                               'subject_1': q.subject})
                    db.session.commit()
                if i.subject_2 is None:
                    Student.query.filter_by(group1=id).update({'group1': i.group2,
                                                               'group2': i.group3,
                                                               'group3': None,
                                                               'subject_2': q.subject})
                    db.session.commit()
                if i.subject_3 is None:
                    Student.query.filter_by(group1=id).update({'group1': i.group2,
                                                               'group2': i.group3,
                                                               'group3': None,
                                                               'subject_3': q.subject})
                    db.session.commit()

            if i.group2 == id:
                if i.subject_1 is None:
                    Student.query.filter_by(group2=id).update({'group2': i.group3,
                                                                   'group3': None,
                                                                   'subject_1': q.subject})
                    db.session.commit()
                if i.subject_2 is None:
                    Student.query.filter_by(group2=id).update({'group2': i.group3,
                                                                   'group3': None,
                                                                   'subject_2': q.subject})
                    db.session.commit()
                if i.subject_3 is None:
                    Student.query.filter_by(group2=id).update({'group2': i.group3,
                                                                   'group3': None,
                                                                   'subject_3': q.subject})
                    db.session.commit()
            if i.group3 == id:
                if i.subject_1 is None:
                    Student.query.filter_by(group3=id).update({'group3': None,
                                                                   'subject_1': q.subject})
                    db.session.commit()
                if i.subject_2 is None:
                    Student.query.filter_by(group3=id).update({'group3': None,
                                                               'subject_2': q.subject})
                    db.session.commit()
                if i.subject_3 is None:
                    Student.query.filter_by(group3=id).update({'group3': None,
                                                                   'subject_3': q.subject})
                    db.session.commit()
    teachers = Teachers.query.filter_by(id=gr).all()
    for i in teachers:
        if i.group1 == id:
            Teachers.query.filter_by(id=gr, group1=id).update({'group1': i.group2,
                                                                     'group2': i.group3,
                                                                     'group3': i.group4,
                                                                     'group4': i.group5,
                                                                     'group5': i.group6,
                                                                     'group6': i.group7,
                                                                     'group7': i.group8,
                                                                     'group8': i.group9,
                                                                     'group9': i.group10,
                                                                     'group10': None})
            db.session.commit()
        elif i.group2 == id:
            Teachers.query.filter_by(id=gr, group2=id).update({'group2': i.group3,
                                                                     'group3': i.group4,
                                                                     'group4': i.group5,
                                                                     'group5': i.group6,
                                                                     'group6': i.group7,
                                                                     'group7': i.group8,
                                                                     'group8': i.group9,
                                                                     'group9': i.group10,
                                                                     'group10': None
                                                                     })
            db.session.commit()
        elif i.group3 == id:
            Teachers.query.filter_by(id=gr, group3=id).update({'group3': i.group4,
                                                                     'group4': i.group5,
                                                                     'group5': i.group6,
                                                                     'group6': i.group7,
                                                                     'group7': i.group8,
                                                                     'group8': i.group9,
                                                                     'group9': i.group10,
                                                                     'group10': None
                                                                     })
            db.session.commit()
        elif i.group4 == id:
            Teachers.query.filter_by(id=gr, group4=id).update({'group4': i.group5,
                                                                     'group5': i.group6,
                                                                     'group6': i.group7,
                                                                     'group7': i.group8,
                                                                     'group8': i.group9,
                                                                     'group9': i.group10,
                                                                     'group10': None
                                                                     })
            db.session.commit()
        elif i.group5 == id:
            Teachers.query.filter_by(id=gr, group5=id).update({'group5': i.group6,
                                                                     'group6': i.group7,
                                                                     'group7': i.group8,
                                                                     'group8': i.group9,
                                                                     'group9': i.group10,
                                                                     'group10': None
                                                                     })
            db.session.commit()


        elif i.group6 == id:
            Teachers.query.filter_by(id=gr, group6=id).update({'group6': i.group7,
                                                                     'group7': i.group8,
                                                                     'group8': i.group9,
                                                                     'group9': i.group10,
                                                                     'group10': None
                                                                     })
            db.session.commit()
        elif i.group7 == id:
            Teachers.query.filter_by(id=gr, group7=id).update({'group7': i.group8,
                                                                     'group8': i.group9,
                                                                     'group9': i.group10,
                                                                     'group10': None
                                                                     })
            db.session.commit()
        elif i.group8 == id:
            Teachers.query.filter_by(id=gr, group8=id).update({'group8': i.group9,
                                                                     'group9': i.group10,
                                                                     'group10': None
                                                                     })
            db.session.commit()
        elif i.group9 == id:
            Teachers.query.filter_by(id=gr, group9=id).update({'group9': i.group10,
                                                                     'group10': None
                                                                     })
            db.session.commit()
        elif i.group10 == id:
            Teachers.query.filter_by(id=gr, group10=id).update({'group10': None
                                                                      })
            db.session.commit()

    teach = Teachers.query.filter_by(id=gr).first()
    num = 1
    total = teach.number_groups - num
    Teachers.query.filter_by(id=gr).update({'number_groups': total})
    db.session.commit()
    del_gr.delete()
    if del_gr.location == 1:
        return redirect(url_for('all_groups'))
    elif del_gr.location == 2:
        return redirect(url_for('all_groups2'))


@app.route('/add_teacher<group_id>', methods=["POST","GET"])
def add_teacher(group_id):
    user = get_current_user()
    user = get_current_user()
    try:
        if not user.xojakent_admin and not user.director and not user.gazalkent_admin:
            return redirect(url_for('home'))
    except AttributeError:
        return redirect(url_for('home'))
    teacher_id = request.form.get('Names')
    show = Groups.query.filter_by(id=group_id).all()
    group_for = Groups.query.filter_by(id=group_id).first()
    query_teacher = Teachers.query.filter_by(id=teacher_id).first()
    num = 1
    teach = Teachers.query.filter_by(id=teacher_id).first()
    total = teach.number_groups + num
    Teachers.query.filter_by(id=teacher_id).update({'number_groups': total})
    db.session.commit()

    for i in show:
        if query_teacher.group1 is None and query_teacher.group2 is None and query_teacher.group3 is None and \
                query_teacher.group4 is None and query_teacher.group5 is None and \
                query_teacher.group6 is None and query_teacher.group7 is None and \
                query_teacher.group8 is None and query_teacher.group9 is None and query_teacher.group10 is None:
            Teachers.query.filter_by(id=teacher_id).update({'group1': i.id})
            db.session.commit()
            Groups.query.filter_by(id=group_id).update({'teacher_1': query_teacher.id,'teacher_name' : query_teacher.name,
                                                       'teacher_surname': query_teacher.surname})
            db.session.commit()

        elif query_teacher.group1 is not None and query_teacher.group2 is None and query_teacher.group3 is None \
                and query_teacher.group4 is None and query_teacher.group5 is None and \
                query_teacher.group6 is None and query_teacher.group7 is None and \
                query_teacher.group8 is None and query_teacher.group9 is None and query_teacher.group10 is None:
            if query_teacher.group1 == i.id:
                return 'Bu grda ustoz uje bor'
            else:
                Teachers.query.filter_by(id=teacher_id).update({'group2': i.id})
                db.session.commit()
                Groups.query.filter_by(id=group_id).update({'teacher_1': query_teacher.id, 'teacher_name': query_teacher.name,
                     'teacher_surname': query_teacher.surname})
                db.session.commit()

        elif query_teacher.group1 is not None and query_teacher.group2 is not None and query_teacher.group3 is None \
                and query_teacher.group4 is None and query_teacher.group5 is None and \
                query_teacher.group6 is None and query_teacher.group7 is None and \
                query_teacher.group8 is None and query_teacher.group9 is None and query_teacher.group10 is None:
            if query_teacher.group1 == i.id:
                return 'Bu grda ustoz uje bor'
            elif query_teacher.group2 == i.id:
                return 'Bu grda ustoz uje bor'

            else:
                Teachers.query.filter_by(id=teacher_id).update({'group3': i.id})
                db.session.commit()
                Groups.query.filter_by(id=group_id).update({'teacher_1': query_teacher.id, 'teacher_name': query_teacher.name,
                     'teacher_surname': query_teacher.surname})
                db.session.commit()


        elif query_teacher.group1 is not None and query_teacher.group2 is not None and query_teacher.group3 is not None \
                and query_teacher.group4 is None and query_teacher.group5 is None and \
                query_teacher.group6 is None and query_teacher.group7 is None and \
                query_teacher.group8 is None and query_teacher.group9 is None and query_teacher.group10 is None:
            if query_teacher.group1 == i.id:
                return 'Bu grda ustoz uje bor'
            elif query_teacher.group2 == i.id:
                return 'Bu grda ustoz uje bor'
            elif query_teacher.group3 == i.id:
                return 'Bu grda ustoz uje bor'
            else:
                Teachers.query.filter_by(id=teacher_id).update({'group4': i.id})
                db.session.commit()
                Groups.query.filter_by(id=group_id).update({'teacher_1': query_teacher.id, 'teacher_name': query_teacher.name,
                     'teacher_surname': query_teacher.surname})
                db.session.commit()

        elif query_teacher.group1 is not None and query_teacher.group2 is not None and query_teacher.group3 is not None \
                and query_teacher.group4 is not None and query_teacher.group5 is None and \
                query_teacher.group6 is None and query_teacher.group7 is None and \
                query_teacher.group8 is None and query_teacher.group9 is None and query_teacher.group10 is None:
            if query_teacher.group1 == i.id:
                return 'Bu grda ustoz uje bor'
            elif query_teacher.group2 == i.id:
                return 'Bu grda ustoz uje bor'
            elif query_teacher.group3 == i.id:
                return 'Bu grda ustoz uje bor'
            elif query_teacher.group4 == i.id:
                return 'Bu grda ustoz uje bor'
            else:
                Teachers.query.filter_by(id=teacher_id).update({'group5': i.id})
                db.session.commit()
                Groups.query.filter_by(id=group_id).update({'teacher_1': query_teacher.id, 'teacher_name': query_teacher.name,
                     'teacher_surname': query_teacher.surname})
                db.session.commit()

        elif query_teacher.group1 is not None and query_teacher.group2 is not None and query_teacher.group3 is not None \
                and query_teacher.group4 is not None and query_teacher.group5 is not None and \
                query_teacher.group6 is None and query_teacher.group7 is None and \
                query_teacher.group8 is None and query_teacher.group9 is None and query_teacher.group10 is None:
            if query_teacher.group1 == i.id:
                return 'Bu grda ustoz uje bor'
            elif query_teacher.group2 == i.id:
                return 'Bu grda ustoz uje bor'
            elif query_teacher.group3 == i.id:
                return 'Bu grda ustoz uje bor'
            elif query_teacher.group4 == i.id:
                return 'Bu grda ustoz uje bor'
            elif query_teacher.group5 == i.id:
                return 'Bu grda ustoz uje bor'
            else:
                Teachers.query.filter_by(id=teacher_id).update({'group6': i.id})
                db.session.commit()
                Groups.query.filter_by(id=group_id).update({'teacher_1': query_teacher.id, 'teacher_name': query_teacher.name,
                     'teacher_surname': query_teacher.surname})
                db.session.commit()


        elif query_teacher.group1 is not None and query_teacher.group2 is not None and query_teacher.group3 is not None \
                and query_teacher.group4 is not None and query_teacher.group5 is not None and \
                query_teacher.group6 is not None and query_teacher.group7 is None and \
                query_teacher.group8 is None and query_teacher.group9 is None and query_teacher.group10 is None:
            if query_teacher.group1 == i.id:
                return 'Bu grda ustoz uje bor'
            elif query_teacher.group2 == i.id:
                return 'Bu grda ustoz uje bor'
            elif query_teacher.group3 == i.id:
                return 'Bu grda ustoz uje bor'
            elif query_teacher.group4 == i.id:
                return 'Bu grda ustoz uje bor'
            elif query_teacher.group5 == i.id:
                return 'Bu grda ustoz uje bor'
            elif query_teacher.group6 == i.id:
                return 'Bu grda ustoz uje bor'
            else:
                Teachers.query.filter_by(id=teacher_id).update({'group7': i.id})
                db.session.commit()
                Groups.query.filter_by(id=group_id).update(
                    {'teacher_1': query_teacher.id, 'teacher_name': query_teacher.name,
                     'teacher_surname': query_teacher.surname})
                db.session.commit()

        elif query_teacher.group1 is not None and query_teacher.group2 is not None and query_teacher.group3 is not None \
                and query_teacher.group4 is not None and query_teacher.group5 is not None and \
                query_teacher.group6 is not None and query_teacher.group7 is not None and \
                query_teacher.group8 is None and query_teacher.group9 is None and query_teacher.group10 is None:
            if query_teacher.group1 == i.id:
                return 'Bu grda ustoz uje bor'
            elif query_teacher.group2 == i.id:
                return 'Bu grda ustoz uje bor'
            elif query_teacher.group3 == i.id:
                return 'Bu grda ustoz uje bor'
            elif query_teacher.group4 == i.id:
                return 'Bu grda ustoz uje bor'
            elif query_teacher.group5 == i.id:
                return 'Bu grda ustoz uje bor'
            elif query_teacher.group6 == i.id:
                return 'Bu grda ustoz uje bor'
            elif query_teacher.group7 == i.id:
                return 'Bu grda ustoz uje bor'
            else:
                Teachers.query.filter_by(id=teacher_id).update({'group8': i.id})
                db.session.commit()
                Groups.query.filter_by(id=group_id).update({'teacher_1': query_teacher.id, 'teacher_name': query_teacher.name,
                     'teacher_surname': query_teacher.surname})
                db.session.commit()


        elif query_teacher.group1 is not None and query_teacher.group2 is not None and query_teacher.group3 is not None \
                and query_teacher.group4 is not None and query_teacher.group5 is not None and \
                query_teacher.group6 is not None and query_teacher.group7 is not None and \
                query_teacher.group8 is not None and query_teacher.group9 is None and query_teacher.group10 is None:
            if query_teacher.group1 == i.id:
                return 'Bu grda ustoz uje bor'
            elif query_teacher.group2 == i.id:
                return 'Bu grda ustoz uje bor'
            elif query_teacher.group3 == i.id:
                return 'Bu grda ustoz uje bor'
            elif query_teacher.group4 == i.id:
                return 'Bu grda ustoz uje bor'
            elif query_teacher.group5 == i.id:
                return 'Bu grda ustoz uje bor'
            elif query_teacher.group6 == i.id:
                return 'Bu grda ustoz uje bor'
            elif query_teacher.group7 == i.id:
                return 'Bu grda ustoz uje bor'
            elif query_teacher.group8 == i.id:
                return 'Bu grda ustoz uje bor'
            else:
                Teachers.query.filter_by(id=teacher_id).update({'group9': i.id})
                db.session.commit()
                Groups.query.filter_by(id=group_id).update({'teacher_1': query_teacher.id, 'teacher_name': query_teacher.name,
                     'teacher_surname': query_teacher.surname})
                db.session.commit()

        elif query_teacher.group1 is not None and query_teacher.group2 is not None and query_teacher.group3 is not None \
                and query_teacher.group4 is not None and query_teacher.group5 is not None and \
                query_teacher.group6 is not None and query_teacher.group7 is not None and \
                query_teacher.group8 is not None and query_teacher.group9 is not None and query_teacher.group10 is None:
            if query_teacher.group1 == i.id:
                return 'Bu grda ustoz uje bor'
            elif query_teacher.group2 == i.id:
                return 'Bu grda ustoz uje bor'
            elif query_teacher.group3 == i.id:
                return 'Bu grda ustoz uje bor'
            elif query_teacher.group4 == i.id:
                return 'Bu grda ustoz uje bor'
            elif query_teacher.group5 == i.id:
                return 'Bu grda ustoz uje bor'
            elif query_teacher.group6 == i.id:
                return 'Bu grda ustoz uje bor'
            elif query_teacher.group7 == i.id:
                return 'Bu grda ustoz uje bor'
            elif query_teacher.group8 == i.id:
                return 'Bu grda ustoz uje bor'
            elif query_teacher.group9 == i.id:
                return 'Bu grda ustoz uje bor'
            else:
                Teachers.query.filter_by(id=teacher_id).update({'group10': i.id})
                db.session.commit()
                Groups.query.filter_by(id=group_id).update({'teacher_1': query_teacher.id, 'teacher_name': query_teacher.name,
                     'teacher_surname': query_teacher.surname})
                db.session.commit()
    if group_for.location == 1:
        return redirect(url_for('inside_of_group',id=group_id))
    elif group_for.location == 2:
        return redirect(url_for('inside_of_group2',id=group_id))



