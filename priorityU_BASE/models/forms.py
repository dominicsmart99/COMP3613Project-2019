from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, TimeField
from wtforms.validators import InputRequired, Email, Length

class LoginForm(FlaskForm):
    username = StringField('username', validators=[InputRequired(), Length(min=4,max=15)])
    password = PasswordField('password', validators=[InputRequired(),Length(min=8, max=30)])
    remember = BooleanField('remember me')  

class RegisterForm(FlaskForm):
    email = StringField('email', validators=[InputRequired(), Email(message='Invalid Email'), Length(max=50)])
    username = StringField('username', validators=[InputRequired(), Length(min=4,max=15)])
    password = PasswordField('password', validators=[InputRequired(),Length(min=8, max=30)])
    university = StringField('university', validators=[InputRequired(), Length(min=4,max=70)])

class NewCourseForm(FlaskForm):
    code = StringField('Course Code', validators=[InputRequired(), Length(min=8, max=8, message="Course Code Invalid")])
    title = StringField('Course Title', validators=[InputRequired(), Length(min=4, max=50, message="Course Title Invalid")])
    lecturer = StringField('Lecturer', validators=[InputRequired(), Length(min=2, max=50, message="Lecturer Name Invalid")])
    location = StringField('Location', validators=[InputRequired(), Length(min=2, max=20, message="Location Invalid")])

class AddClassForm(FlaskForm):
    classTime = TimeField('classTime')
    lecturer = StringField('lecturer', validators=[Length(min=0, max=50, message="Lecturer Name Invalid")])
    classType = StringField('classType', validators=[InputRequired(), Length(min=3, max=20, message="Class Type Invalid")])



