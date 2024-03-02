from flask import *
from database import *

staff = Blueprint('staff',__name__)

@staff.route('/staff_home')
def userHome():
    return render_template('staff_pages/staff_home.html')

@staff.route('/attendance',methods=['get','post'])
def staffAttendance():
    if 'submit' in request.form:
        date=request.form['date']
        sTime=request.form['start_time']
        eTime=request.form['end_time']
        q1="insert into attendence values(null,'%s','%s','%s','%s')"%(session['staff_id'],date,sTime,eTime)
        insert(q1)
        return redirect(url_for('staff.staffAttendance'))
    return render_template('staff_pages/attendence.html')