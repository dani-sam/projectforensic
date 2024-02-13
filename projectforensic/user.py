from flask import *

user = Blueprint('user',__name__)

@user.route('/user_home')
def userHome():
    return render_template('user_pages/user_home.html')