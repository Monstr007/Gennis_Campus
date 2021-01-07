from app import app, get_current_user, or_, db, url_for, redirect, render_template, request, get_current_teacher
from models import Student, Groups, Teachers, All_groups


@app.route('/delete_teacher1/<int:id><int:gr>')
def delete_teacher1(id,gr):
    user = get_current_user()
    try:
        if not user.xojakent_admin and not user.director and not user.gazalkent_admin:
            return redirect(url_for('home'))
    except AttributeError:
        return redirect(url_for('home'))
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
    Groups.query.filter_by(teacher_1=gr,id=id).update({'teacher_1': 0,'teacher_name':'','teacher_surname':''})
    db.session.commit()
    gr_location = Groups.query.filter_by(id=gr).first()
    if user.locations == 1:
        return redirect(url_for('manage',id=id))
    elif user.locations == 2:
        return redirect(url_for('manage',id=id))


@app.route('/delete_student_q/<int:id>/<int:teacher_id>/<int:gr_id>', methods=['POST', 'GET'])
def delete_student_q(id, teacher_id, gr_id):
    user = get_current_user()
    try:
        if not user.xojakent_admin and not user.director and not user.gazalkent_admin:
            return redirect(url_for('home'))
    except AttributeError:
        return redirect(url_for('home'))
    num = 1
    calc = Groups.number_students - num
    Groups.query.filter_by(id=gr_id).update({'number_students':calc})
    db.session.commit()
    gr_location = Groups.query.filter_by(id=gr_id).first()
    students = Student.query.filter(or_(Student.group1 == gr_id, Student.group2 == gr_id, Student.group3 == gr_id))
    groups_n1 = Groups.query.filter_by(id=gr_id).all()
    for q in groups_n1:
        for i in students:
            if i.group1 == gr_id:
                if i.subject_1 == "":
                    Student.query.filter_by(group1=gr_id, id=id).update({'group1': i.group2,
                                                                         'group2': i.group3,
                                                                         'group3': None,
                                                                         'subject_1': q.subject})
                    db.session.commit()
                if i.subject_2 == "":
                    Student.query.filter_by(group1=gr_id, id=id).update({'group1': i.group2,
                                                                         'group2': i.group3,
                                                                         'group3': None,
                                                                         'subject_2': q.subject})
                    db.session.commit()
                if i.subject_3 == "":
                    Student.query.filter_by(group1=gr_id, id=id).update({'group1': i.group2,
                                                                         'group2': i.group3,
                                                                         'group3': None,
                                                                         'subject_3': q.subject})
                    db.session.commit()

            if i.group2 == gr_id:
                if i.subject_1 == "":
                    Student.query.filter_by(group2=gr_id, id=id).update({'group2': i.group3,
                                                                         'group3': None,
                                                                         'subject_1': q.subject})
                    db.session.commit()
                if i.subject_2 == "":
                    Student.query.filter_by(group2=gr_id, id=id).update({'group2': i.group3,
                                                                         'group3': None,
                                                                         'subject_2': q.subject})
                    db.session.commit()
                if i.subject_3 == "":
                    Student.query.filter_by(group2=gr_id, id=id).update({'group2': i.group3,
                                                                         'group3': None,
                                                                         'subject_3': q.subject})
                    db.session.commit()
            if i.group3 == gr_id:
                if i.subject_1 == "":
                    Student.query.filter_by(group3=gr_id, id=id).update({'group3': None,
                                                                         'subject_1': q.subject})
                    db.session.commit()
                if i.subject_2 == "":
                    Student.query.filter_by(group3=gr_id, id=id).update({'group3': None,
                                                                         'subject_2': q.subject})
                    db.session.commit()
                if i.subject_3 == "":
                    Student.query.filter_by(group3=gr_id, id=id).update({'group3': None,
                                                                         'subject_3': q.subject})
                    db.session.commit()
    if gr_location == 1:
        return redirect(url_for('all_groups'))
    elif gr_location == 2:
        return redirect(url_for('all_groups2'))


@app.route('/create_group', methods=['POST', 'GET'])
def create_group():
    teacher = get_current_teacher()
    user = get_current_user()
    try:
        if not user.xojakent_admin and not user.gazalkent_admin and not user.director:
            return redirect(url_for('home'))
    except AttributeError:
        return redirect(url_for('home'))
    if request.method == 'POST':
        name = request.form.get("name")
        teachers = request.form.get("teacher")
        group_location = request.form.get('location')
        type_of_course = request.form.get('type_of_course')
        cost = request.form.get('cost')
        if group_location == "xojakent":
            group_location = 1
            num = 1
            groups_num = All_groups.all_groups + num
            All_groups.query.filter_by(id=1).update({'all_groups': groups_num})
            db.session.commit()
            teach = Teachers.query.filter_by(id=teachers).first()
            total = teach.number_groups + num
            Teachers.query.filter_by(id=teachers).update({'number_groups':total})
            db.session.commit()
        elif group_location == "gazalkent":
            group_location = 2
            num = 1
            groups_num = All_groups.all_groups + num
            All_groups.query.filter_by(id=1).update({'all_groups': groups_num})
            db.session.commit()
            teach = Teachers.query.filter_by(id=teachers).first()
            total = teach.number_groups + num
            Teachers.query.filter_by(id=teachers).update({'number_groups': total})
            db.session.commit()
        teacher_id = Teachers.query.filter_by(id=teachers).first()
        teacher_name = Teachers.query.filter_by(id=teachers).first()
        teacher_surname = Teachers.query.filter_by(id=teachers).first()
        if user.director:
            add = Groups(name=name, teacher_1=teacher_id.id, location=group_location, subject=teacher_id.subject,
                         cost=cost,
                         teacher_name=teacher_name.name, teacher_surname=teacher_surname.surname,
                         type_of_course=type_of_course)
            db.session.add(add)
        else:
            add = Groups(name=name, teacher_1=teacher_id.id, location=user.locations, subject=teacher_id.subject,
                         cost=cost,
                         teacher_name=teacher_name.name, teacher_surname=teacher_surname.surname,
                         type_of_course=type_of_course)
            db.session.add(add)
        show = Groups.query.filter_by(name=name).all()
        teachers1 = Teachers.query.filter_by(id=teachers).all()
        query_teacher = Teachers.query.filter_by(id=teachers).first()

        for i in show:
            if query_teacher.group1 is None and query_teacher.group2 is None and query_teacher.group3 is None and \
                    query_teacher.group4 is None and query_teacher.group5 is None and \
                    query_teacher.group6 is None and query_teacher.group7 is None and \
                    query_teacher.group8 is None and query_teacher.group9 is None and query_teacher.group10 is None:
                Teachers.query.filter_by(id=teachers).update({'group1': i.id})


            elif query_teacher.group1 is not None and query_teacher.group2 is None and query_teacher.group3 is None \
                    and query_teacher.group4 is None and query_teacher.group5 is None and \
                    query_teacher.group6 is None and query_teacher.group7 is None and \
                    query_teacher.group8 is None and query_teacher.group9 is None and query_teacher.group10 is None:
                if query_teacher.group1 == i.id:
                    return 'Bu grda ustoz uje bor'
                else:
                    Teachers.query.filter_by(id=teachers).update({'group2': i.id})


            elif query_teacher.group1 is not None and query_teacher.group2 is not None and query_teacher.group3 is None \
                    and query_teacher.group4 is None and query_teacher.group5 is None and \
                    query_teacher.group6 is None and query_teacher.group7 is None and \
                    query_teacher.group8 is None and query_teacher.group9 is None and query_teacher.group10 is None:
                if query_teacher.group1 == i.id:
                    return 'Bu grda ustoz uje bor'
                elif query_teacher.group2 == i.id:
                    return 'Bu grda ustoz uje bor'

                else:
                    Teachers.query.filter_by(id=teachers).update({'group3': i.id})


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
                    Teachers.query.filter_by(id=teachers).update({'group4': i.id})


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
                    Teachers.query.filter_by(id=teachers).update({'group5': i.id})


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
                    Teachers.query.filter_by(id=teachers).update({'group6': i.id})


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
                    Teachers.query.filter_by(id=teachers).update({'group7': i.id})


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
                    Teachers.query.filter_by(id=teachers).update({'group8': i.id})


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
                    Teachers.query.filter_by(id=teachers).update({'group9': i.id})


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
                    Teachers.query.filter_by(id=teachers).update({'group10': i.id})
        calc = Student.query.filter_by(for_group=True).all()
        calculate = len(calc)
        Groups.query.filter_by(name=name).update({'number_students': calculate})
        query = Student.query.filter_by(for_group=True).first()
        for q in teachers1:
            for i in show:
                if query.group1 is None and query.group2 is None and query.group3 is None:
                    if q.subject == query.subject_1:
                        Student.query.filter_by(for_group=True).update(
                            {'group1': i.id,'for_group':False, 'subject_1': None})


                    elif q.subject == query.subject_2:
                        Student.query.filter_by(for_group=True).update(
                            {'group1': i.id,'for_group':False, 'subject_2': None})


                    elif q.subject == query.subject_3:
                        Student.query.filter_by(for_group=True).update(
                            {'group1': i.id,'for_group':False,  'subject_3': None})


                elif query.group1 is not None and query.group2 is None and query.group3 is None:
                    if query.group1 == i.id:
                        return 'Bu gruppa band'
                    else:
                        if q.subject == query.subject_1:
                            Student.query.filter_by(for_group=True).update(
                                {'group2': i.id,'for_group':False,  'subject_1': None})


                        elif q.subject == query.subject_2:
                            Student.query.filter_by(for_group=True).update(
                                {'group2': i.id,'for_group':False,  'subject_2': None})


                        elif q.subject == query.subject_3:
                            Student.query.filter_by(for_group=True).update(
                                {'group2': i.id,'for_group':False,  'subject_3': None})


                elif query.group1 is not None and query.group2 is not None and query.group3 is None:
                    if query.group1 == i.id:
                        return 'Bu gruppa band'
                    elif query.group2 == i.id:
                        return 'Bu gruppa band'
                    else:
                        if q.subject == query.subject_1:
                            Student.query.filter_by(for_group=True).update(
                                {'group3': i.id,'for_group':False,  'subject_1': None})

                        elif q.subject == query.subject_2:
                            Student.query.filter_by(for_group=True).update(
                                {'group3': i.id, 'for_group':False, 'subject_2': None})


                        elif q.subject == query.subject_3:
                            Student.query.filter_by(for_group=True).update(
                                {'group3': i.id,'for_group':False,  'subject_3': None})




    experts = Teachers.query.filter_by(teacher=True).all()
    student1 = Student.query.filter_by(for_group=True).all()
    student = Student.query.filter_by(for_group=True).first()
    db.session.commit()
    return render_template('Groups/create group.html', user=user, teachers=experts, student1=student1, teacher=teacher,
                           student=student)


@app.route('/check/<check_id>', methods=["POST"])
def check1(check_id):
    completed = request.get_json()['completed']
    todo_id = Student.query.get(check_id)
    todo_id.for_group = completed
    db.session.commit()
    return redirect(url_for('create_group'))


@app.route('/groups')
def groups():
    user = get_current_user()
    try:
        if not user.xojakent_admin and not user.director and not user.gazalkent_admin:
            return redirect(url_for('home'))
    except AttributeError:
        return redirect(url_for('home'))
    return render_template('Groups/create group.html')
