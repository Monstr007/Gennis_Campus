from app import app, render_template, redirect, request, url_for, get_current_user, get_current_teacher, or_, db
from models import Groups, Teachers, Student, Student_cash, Bank, Overhead, Capital_expenditure, \
    All_Capital_Expenditure, \
    All_overhead, Teacher_cash, Withdrawal, All_withdrawal
from datetime import datetime

now = datetime.now()


@app.route('/all_groups2')
def all_groups2():
    user = get_current_user()
    try:
        if not user.gazalkent_admin and not user.director:
            return redirect(url_for('home'))
    except AttributeError:
        return redirect(url_for('home'))
    groups = Groups.query.order_by('id').all()
    for group in groups:
        teacher = Teachers.query.filter_by(id=group.teacher_1).first()
        return render_template('Groups/Groups2.html', teacher_1=teacher, groups=groups, user=user)
    return render_template('Groups/Groups2.html', groups=groups, user=user)


@app.route('/Groups_without_teacher2')
def group_without_teacher2():
    user = get_current_user()
    try:
        if not user.gazalkent_admin and not user.director:
            return redirect(url_for('home'))
    except AttributeError:
        return redirect(url_for('home'))
    groups = Groups.query.filter_by(teacher_1=0).all()
    return render_template('Groups/Without Teacher2.html', user=user, groups=groups)


@app.route('/inside_of_group2/<int:id>', methods=['POST', 'GET'])
def inside_of_group2(id):
    user = get_current_user()
    try:
        if not user.gazalkent_admin and not user.director:
            return redirect(url_for('home'))
    except AttributeError:
        return redirect(url_for('home'))
    groups = Groups.query.filter_by(id=id).all()
    experts = Teachers.query.filter_by(teacher=True).all()
    for group in groups:
        student = Student.query.filter(
            or_(Student.group1 == group.id, Student.group2 == group.id, Student.group3 == group.id))
        return render_template('Groups/Inside of Group2.html', students=student, groups=groups, user=user,
                               teachers=experts)
    return render_template('Groups/Inside of Group2.html', groups=groups, user=user, teachers=experts)


@app.route('/teacher_result', methods=['POST', 'GET'])
def teacher_result():
    user = get_current_user()
    try:
        if not user.gazalkent_admin and not user.director and not user.xojakent_admin:
            return redirect(url_for('home'))
    except AttributeError:
        return redirect(url_for('home'))
    teacher = Teacher_cash.query.order_by('id').all()
    bank = Bank.query.order_by('id').all()
    return render_template('payment/teacher_result.html', user=user, teacher=teacher, bank=bank)


@app.route('/calculate/<id>', methods=['POST'])
def calculate(id):
    user = get_current_user()
    try:
        if not user.gazalkent_admin and not user.director and not user.xojakent_admin:
            return redirect(url_for('home'))
    except AttributeError:
        return redirect(url_for('home'))
    money = int(request.form.get('pay'))
    old = Student.query.filter_by(id=id).all()
    data = datetime.now()
    for sum in old:
        pul = sum.money
        total = pul + money
        Student.query.filter_by(id=id).update({"money": total})
        qosh = Bank.cash + money
        Bank.query.filter_by(id=1).update({'cash': qosh})
        add = Student_cash(student_id=id, debt=pul, payment=money, result=total, payment_data=data, username=sum.username,
                           student_name=sum.name, student_surname=sum.surname)
        add.add()
        return redirect(url_for('payment'))


@app.route('/salary_give/<id>', methods=['POST'])
def salary_give(id):
    user = get_current_user()
    try:
        if not user.gazalkent_admin and not user.director and not user.xojakent_admin:
            return redirect(url_for('home'))
    except AttributeError:
        return redirect(url_for('home'))
    salary = int(request.form.get('teacher_salary'))
    teacher = Teachers.query.filter_by(id=id).first()
    all = teacher.salary - salary
    Teachers.query.filter_by(id=id).update({'salary': all})
    Teachers.query.filter_by(id=id).update({'salary': all})
    add = Teacher_cash(teacher_id=teacher.id, teacher_name=teacher.name, teacher_surname=teacher.surname,
                       username=teacher.username, payment=salary, payment_data=now, salary=teacher.salary, result=all)
    db.session.add(add)
    db.session.commit()
    bank = Bank.query.filter_by(id=1).first()
    total = bank.cash - salary
    Bank.query.filter_by(id=1).update({'cash': total})
    db.session.commit()
    return redirect(url_for('teacher_result'))


@app.route('/overhead', methods=['POST', 'GET'])
def overhead():
    user = get_current_user()
    try:
        if not user.gazalkent_admin and not user.director and not user.xojakent_admin:
            return redirect(url_for('home'))
    except AttributeError:
        return redirect(url_for('home'))
    if request.method == 'POST':
        reason = request.form.get('reason')
        amount = request.form.get('amount')
        sums = int(request.form.get('sum'))
        now = datetime.now()
        save = Overhead(reason=reason, quantity=amount, sum=sums, payed_data=now)
        db.session.add(save)
        db.session.commit()
        sum = All_overhead.query.filter_by(id=1).first()
        total = sum.total_sum + sums
        All_overhead.query.filter_by(id=1).update({'total_sum': total})
        db.session.commit()
        return redirect(url_for('overhead'))
    over = Overhead.query.order_by('id').all()
    all_over = All_overhead.query.order_by('id').all()
    return render_template('payment/overhead.html', user=user, over=over, all_over=all_over)


@app.route('/capital', methods=['POST', 'GET'])
def capital():
    user = get_current_user()
    try:
        if not user.gazalkent_admin and not user.director and not user.xojakent_admin:
            return redirect(url_for('home'))
    except AttributeError:
        return redirect(url_for('home'))
    if request.method == 'POST':
        name_item = request.form.get('name_item')
        number_item = int(request.form.get('number_item'))
        sums = int(request.form.get('amount_item'))
        now = datetime.now()
        save = Capital_expenditure(item=name_item, number_items=number_item, amount_item=sums, bought_data=now)
        db.session.add(save)
        db.session.commit()
        sum = All_Capital_Expenditure.query.filter_by(id=1).first()
        total = sum.total_sum + sums
        All_Capital_Expenditure.query.filter_by(id=1).update({'total_sum': total})
        db.session.commit()
        return redirect(url_for('capital'))

    capitals = Capital_expenditure.query.order_by('id').all()
    all_capitals = All_Capital_Expenditure.query.order_by('id').all()
    return render_template('payment/capital.html', user=user, capitals=capitals, all_capitals=all_capitals)


@app.route('/payment')
def payment():
    user = get_current_user()
    try:
        if not user.gazalkent_admin and not user.director and not user.xojakent_admin:
            return redirect(url_for('home'))
    except AttributeError:
        return redirect(url_for('home'))
    info = Student_cash.query.order_by('id').all()
    bank = Bank.query.order_by('id').all()
    for student in info:
        student_cash = Student.query.filter_by(id=student.student_id)
        return render_template('payment/payment.html', student=student_cash, user=user, info=info, bank=bank)
    return render_template('payment/payment.html', user=user, info=info, bank=bank)


@app.route('/pay', methods=['POST'])
def pay_result():
    user = get_current_user()
    try:
        if not user.gazalkent_admin and not user.director and not user.xojakent_admin:
            return redirect(url_for('home'))
    except AttributeError:
        return redirect(url_for('home'))
    payment = request.form.get('payment')
    name1 = request.form.get('payment').upper()
    surname1 = request.form.get('payment').upper()
    number1 = request.form.get('payment')
    usernames = Student.query.filter_by(username=payment).all()
    for username in usernames:
        if username.username == payment:
            return render_template('payment/pay result.html', gmails=usernames, user=user)
    names = Student.query.filter_by(name=name1).all()
    for name in names:
        if name.name == name1:
            return render_template('payment/pay_name.html', user=user, names=names)
    surnames = Student.query.filter_by(surname=surname1).all()
    for surname in surnames:
        if surname.surname == surname1:
            return render_template('payment/pay_surname.html', user=user, surnames=surnames)
    numbers = Student.query.filter_by(phone=number1).all()
    for number in numbers:
        if number.phone == number1:
            return render_template('payment/pay_phone.html', user=user, number=numbers)


@app.route('/teacher_search', methods=['POST'])
def teacher_search():
    user = get_current_user()
    try:
        if not user.gazalkent_admin and not user.director and not user.xojakent_admin:
            return redirect(url_for('home'))
    except AttributeError:
        return redirect(url_for('home'))
    payment = request.form.get('teacher_payment')
    name1 = request.form.get('teacher_payment').upper()
    surname1 = request.form.get('teacher_payment').upper()
    number1 = request.form.get('teacher_payment')
    gmails = Teachers.query.filter_by(username=payment).all()
    for gmail in gmails:
        if gmail.username == payment:
            return render_template('payment/payment_teacher.html', gmails=gmails, user=user)
    names = Teachers.query.filter_by(name=name1).all()
    for name in names:
        if name.name == name1:
            return render_template('payment/teacher_name.html', user=user, names=names)
    surnames = Teachers.query.filter_by(surname=surname1).all()
    for surname in surnames:
        if surname.surname == surname1:
            return render_template('payment/teacher_surname.html', user=user, surnames=surnames)
    numbers = Teachers.query.filter_by(phone=number1).all()
    for number in numbers:
        if number.phone == number1:
            return render_template('payment/teacher_phone.html', user=user, number=numbers)


@app.route('/study_students')
def students_loc_1():
    user = get_current_user()
    try:
        if not user.gazalkent_admin and not user.director and not user.xojakent_admin:
            return redirect(url_for('home'))
    except AttributeError:
        return redirect(url_for('home'))
    students = Student.query.order_by('id').all()
    return render_template('student/student_loc_1.html', user=user, students=students)


@app.route('/study_students2')
def students_loc_2():
    user = get_current_user()
    try:
        if not user.gazalkent_admin and not user.director and not user.xojakent_admin:
            return redirect(url_for('home'))
    except AttributeError:
        return redirect(url_for('home'))
    students = Student.query.order_by('id').all()
    return render_template('student/student_loc_2.html', user=user, students=students)


@app.route('/search_student', methods=['POST'])
def search_student():
    user = get_current_user()
    try:
        if not user.gazalkent_admin and not user.director and not user.xojakent_admin:
            return redirect(url_for('home'))
    except AttributeError:
        return redirect(url_for('home'))
    else:
        if user.xojakent_admin or user.director:
            username1 = request.form.get('student')
            name1 = request.form.get('student').upper()
            surname1 = request.form.get('student').upper()
            number1 = request.form.get('student')
            usernames = Student.query.filter_by(username=username1).all()
            for username in usernames:
                if username.username == username1:
                    return render_template('student/search_by_username.html', user=user, usernames=usernames)
            surnames = Student.query.filter_by(surname=surname1).all()
            for surname in surnames:
                if surname.surname == surname1:
                    return render_template('student/search_by_surname.html', user=user, surnames=surnames)
            names = Student.query.filter_by(name=name1).all()
            for name in names:
                if name.name == name1:
                    return render_template('student/search_by_name.html', user=user, names=names)
            numbers = Student.query.filter_by(phone=number1).all()
            for number in numbers:
                if number.phone == number1:
                    return render_template('student/search_by_phone.html', numbers=numbers, user=user)
        elif user.gazalkent_admin or user.director:
            username1 = request.form.get('student')
            name1 = request.form.get('student').upper()
            surname1 = request.form.get('student').upper()
            number1 = request.form.get('student')
            usernames = Student.query.filter_by(username=username1).all()
            for username in usernames:
                if username.username == username1:
                    return render_template('student/search_by_username2.html', usernames=usernames, user=user)
            surnames = Student.query.filter_by(surname=surname1).all()
            for surname in surnames:
                if surname.surname == surname1:
                    return render_template('student/search_by_surname2.html', surnames=surnames, user=user)
            names = Student.query.filter_by(name=name1).all()
            for name in names:
                if name.name == name1:
                    return render_template('student/search_by_name2.html', user=user, names=names)
            numbers = Student.query.filter_by(phone=number1).all()
            for number in numbers:
                if number.phone == number1:
                    return render_template('student/search_by_phone2.html', user=user, numbers=numbers)


@app.route('/withdrawal',methods=['POST','GET'])
def withdrawal():
    user = get_current_user()
    try:
        if not user.gazalkent_admin and not user.director and not user.xojakent_admin:
            return redirect(url_for('home'))
    except AttributeError:
        return redirect(url_for('home'))
    if request.method == "POST":
        who = request.form.get('who')
        why = request.form.get('why')
        sum = int(request.form.get('amount'))
        add = Withdrawal(who=who, why=why, amount=sum, date=now)
        db.session.add(add)
        witdh = All_withdrawal.query.filter_by(id=1).first()
        all = witdh.total_sum + sum
        All_withdrawal.query.filter_by(id=1).update({'total_sum': all})
        db.session.commit()
        return redirect(url_for('withdrawal'))
    withdrawals = Withdrawal.query.order_by('id').all()
    all_withdrawal = All_withdrawal.query.order_by('id').all()
    return render_template('payment/withdrawal.html',user=user,withdrawals=withdrawals,all_withdrawal=all_withdrawal)


@app.route('/student_debts')
def student_debts():
    user = get_current_user()
    try:
        if not user.gazalkent_admin and not user.director and not user.xojakent_admin:
            return redirect(url_for('home'))
    except AttributeError:
        return redirect(url_for('home'))
    debts = Student.query.order_by('id').all()
    return render_template('student/students_with_debts.html',user=user,debts=debts)