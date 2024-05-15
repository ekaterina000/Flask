from . import flask_app
from flask import make_response
import random
import MySQLdb

from flask import render_template, request, session, redirect, url_for
from app.forms import UserForm

@flask_app.route("/moz")
def set_cookie():
    user_agent = request.headers.get('User-Agent')
    if 'Mozilla' in user_agent:
        flag = random.randint(1, 100)
        response = make_response("<h1>Welcome to the website!</h1>")
        response.set_cookie('flag', str(flag))
        return response\

@flask_app.route("/user/<name>")
def hello_user(name):
    return '<h2>Hello, {}</h2>'.format(name)

@flask_app.route("/user_info")
def info():
    user_ip = request.remote_addr
    user_agent = request.headers.get('User-Agent')
    return '<h2>Your IP address is {}</h2><h2>Your browser is {}</h2>'.format(user_ip, user_agent)

@flask_app.route("/")
def index():
    print('test')
    user = {"username": "Kate"}
    return render_template("index.html", user=user)

@flask_app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


@flask_app.route('/form', methods=['GET', 'POST'])
def form():
    form = UserForm()

    if request.method == 'POST' and form.validate_on_submit():
        session['login'] = form.login.data
        session['email'] = form.email.data
        session['gender'] = form.gender.data

        # Создать соединение с базой данных
        conn = MySQLdb.connect(host='your_host', user='your_user', passwd='your_password', db='your_database')

        # Создать курсор для выполнения запросов
        cursor = conn.cursor()

        # Вставить данные пользователя в базу данных
        query = "INSERT INTO users (login, email, gender) VALUES (%s, %s, %s)"
        values = (session['login'], session['email'], session['gender'])
        cursor.execute(query, values)

        # Подтвердить изменения в базе данных
        conn.commit()

        # Закрыть соединение и курсор
        cursor.close()
        conn.close()

        return redirect(url_for('profile'))

    return render_template('form.html', form=form)


@flask_app.route('/profile', methods=['GET', 'POST'])
def profile():
    if request.method == 'POST':
        session['login'] = request.form.get('login')
        session['email'] = request.form.get('email')
        session['gender'] = request.form.get('gender')
        return redirect(url_for('profile'))

    login = session.get('login')
    email = session.get('email')
    gender = session.get('gender')

    return render_template('profile.html', login=login, email=email, gender=gender)

@flask_app.route('/confirm_auth')
def confirm():

def send_mail(to, subject, template, **kwargs):
    