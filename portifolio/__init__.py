import os
from flask import Flask
from flask_mail import Mail, Message

app = Flask(__name__)

app.config['SECRET_KEY'] = '45ca2defb01cc7f0b122f36e6ca22e9d'

base_dir = os.path.abspath(os.path.dirname(__file__))

# Configuração do Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'  # ou outro servidor SMTP
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = 'contatopauloricardopg@gmail.com'
app.config['MAIL_PASSWORD'] = 'lkqs wuow rlpz huww'  # use senha de app (não sua senha pessoal)

mail = Mail(app)

from portifolio import routes