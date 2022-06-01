from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length, EqualTo

class LoginForm(FlaskForm):
    username = StringField('username', validators=[InputRequired(),
                                                   Length(min=4, max=15)],
                           render_kw={"placeholder": "Username", "autofocus": ""})
    password = PasswordField('password', validators=[InputRequired(),
                                                     Length(min=8, max=80)], render_kw={"placeholder": "Password"})
    remember = BooleanField('Remember Me')


# class RegisterForm(FlaskForm):
#     email = StringField('Email Address', validators=[InputRequired(), Email(message='Invalid email'),
#                                                      Length(max=50)], render_kw={"placeholder": "Email Address"})
#     username = StringField('Username', validators=[InputRequired(),
#                                                    Length(min=4, max=15)],
#                            render_kw={"placeholder": "Username", "autofocus": ""})
#     password = PasswordField('Password', validators=[InputRequired(),
#                                                      Length(min=8, max=80),
#                                                      EqualTo('confirm', message='Passwords must match')],
#                              render_kw={"placeholder": "Password"})
#     confirm = PasswordField('Repeat Password', render_kw={"placeholder": "Repeat Password"})