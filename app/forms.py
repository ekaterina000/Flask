from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectField
from wtforms.validators import InputRequired

class UserForm(FlaskForm):
    login = StringField('Логин', validators=[InputRequired()])
    email = StringField('Email', validators=[InputRequired()])
    password = PasswordField('Пароль', validators=[InputRequired()])
    confirm_password = PasswordField('Подтвердите пароль', validators=[InputRequired()])
    gender = SelectField('Пол', choices=[('M', 'Мужской'), ('F', 'Женский')])
