from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError


class FormContato(FlaskForm):
    username = StringField('Seu Nome', validators=[DataRequired()])
    email = StringField('Seu Email', validators=[DataRequired(), Email()])
    corpo = TextAreaField('Sua Mensagem', validators=[DataRequired()])
    botao_submit = SubmitField('Enviar')