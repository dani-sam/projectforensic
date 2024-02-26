from flask import *
from public import public
from admin import admin
from staff import staff
from police import police
from court import court


app = Flask(__name__)

app.register_blueprint(public)
app.register_blueprint(admin)
app.register_blueprint(staff)
app.register_blueprint(police)
app.register_blueprint(court)



app.secret_key="wdfvb"
app.run(debug=True,port=5678)