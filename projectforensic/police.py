import uuid
from flask import *
from database import *

police = Blueprint('police',__name__)


@police.route('/police_home')
def userHome():
    return render_template('police_pages/police_home.html')

@police.route('/add_case',methods=['get','post'])
def addCase():
    if 'submit' in request.form:
        polId=request.form['police_id']
        date=request.form['date']
        time=request.form['time']
        place=request.form['place']
        caseType=request.form['case_type']
        photo=request.files['case_photo']
        path='static/casePhoto'+str(uuid.uuid4())+photo.filename
        photo.save(path)
        latitude=request.form['latitude']
        longitude=request.form['longitude']
        detailOfEvents=request.form['detail_of_event']
        summary=request.form['summary']
        reportOfficer=request.form['report_officer']

        q1="insert into cases values(null,'%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(polId,date,time,place,caseType,path,latitude,longitude,detailOfEvents,summary,reportOfficer)
        insert(q1)
        return redirect(url_for('police.addCase'))
    return render_template('police_pages/addCase.html')

@police.route('/view_case')
def viewCase():
    data={}
    q1 = "select * from cases"
    data['cases']=select(q1)
    return render_template('police_pages/viewCase.html',data=data)