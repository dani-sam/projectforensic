from flask import Flask
from public import public
from admin import admin
from police import police
from court import court
from staff import staff

import smtplib
from email.mime.text import MIMEText
from flask_mail import Mail

app=Flask(__name__)
app.secret_key="hello"
app.register_blueprint(public)
app.register_blueprint(admin, url_prefix='/admin')
app.register_blueprint(police, url_prefix='/police')
app.register_blueprint(court,url_prefix='/court')
app.register_blueprint(staff, url_prefix='/staff')

mail=Mail(app)
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'sngistoutpass@gmail.com'
app.config['MAIL_PASSWORD'] = 'izgqjuqneorhokje'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True


app.run(debug=True,port=5053)