from flask import *
from database import *

court = Blueprint('court',__name__)

@court.route('/court_home')
def courtHome():
    return render_template('court_pages/court_home.html')

@court.route('/request_evidence',methods=['get','post'])
def requestEvidence():
    data={}
    d="select * from cases" 
    data['cases']=select(d)

    if 'submit' in request.form:
        caseId=request.form['case_id']
        evdType=request.form['evd_type']
        description=request.form['desc']
        status=request.form['status']
        q1="insert into request_evidence  values(null,'%s','%s','%s','%s')"%(caseId,evdType,description,status)
        insert(q1)
        return redirect(url_for('court.requestEvidence'))
    return render_template('court_pages/requestEvidence.html',data=data)
