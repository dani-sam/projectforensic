from flask import *

staff = Blueprint('staff',__name__)

@staff.route('/user_home')
def userHome():
    return render_template('staff_pages/staff_home.html')