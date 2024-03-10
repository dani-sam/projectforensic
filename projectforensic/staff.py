from flask import *
from database import *

staff = Blueprint('staff',__name__)

@staff.route('/staff_home')
def userHome():
    return render_template('staff_pages/staff_home.html')

@staff.route('/update_profile')
def updateProfile():
    data={}
    q1 = "select * from staff where ft_id='%s'"%(session['staff_id'])
    data['staff']=select(q1)
    return render_template('staff_pages/update_profile.html',data=data)

@staff.route('/attendance',methods=['get','post'])
def staffAttendance():
    if 'submit' in request.form:
        date=request.form['date']
        sTime=request.form['start_time']
        eTime=request.form['end_time']
        q1="insert into attendance values(null,'%s','%s','%s','%s')"%(session['staff_id'],date,sTime,eTime)
        insert(q1)
        return redirect(url_for('staff.staffAttendance'))
    return render_template('staff_pages/attendance.html')

@staff.route('/fingerprint')
def fingerprint():
    return render_template('staff_pages/fingerprint.html')

@staff.route('/footprint')
def footprint():
    return render_template('staff_pages/footprint.html')

@staff.route('/hair_test')
def hairTest():
    return render_template('staff_pages/hair_test.html')

@staff.route('/video_audio')
def video_audio():
    return render_template('staff_pages/video_audio.html')

@staff.route('/teeth')
def teeth():
    return render_template('staff_pages/teeth.html')

@staff.route('/post_mortem')
def postMortem():
    return render_template('staff_pages/post_mortem.html')