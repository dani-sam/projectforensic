from flask import *
from database import *

admin = Blueprint('admin',__name__)

@admin.route('/admin_home')
def adminHome():
    return render_template('admin_pages/admin_home.html')

@admin.route('/manage_staff')
def manageStaff():
    if 'submit' in request.form:
        name=request.form['name']
        position=request.form['position']
        gender=request.form['gender']
        email=request.form['email_id']
        place=request.form['place']
        district=request.form['district']
        state=request.form['state']
        contactNo=request.form['contact_no']
        photo=request.form['photo']
        username=request.form['username']
        password=request.form['password']




    return render_template('/admin_pages/manage_staff.html')