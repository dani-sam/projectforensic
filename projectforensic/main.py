from flask import *
from public import public
from admin import admin
from staff import staff


app = Flask(__name__)

app.register_blueprint(public)
app.register_blueprint(admin)
app.register_blueprint(staff)



app.secret_key="wdfvb"
app.run(debug=True,port=5678)