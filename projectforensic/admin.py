import uuid
from flask import *
from database import *

admin = Blueprint('admin',__name__)

@admin.route('/admin_home')
def adminHome():
    return render_template('admin_pages/admin_home.html')

@admin.route('/manage_staff',methods=['get','post'])
def manageStaff():
    data={}
    q1 = "select * from staff"
    data['staff']=select(q1)
    if 'submit' in request.form:
        name=request.form['name']
        position=request.form['position']
        gender=request.form['gender']
        email=request.form['email_id']
        place=request.form['place']
        district=request.form['district']
        state=request.form['state']
        contactNo=request.form['contact_no']
        photo=request.files['photo'] 
        path='static/staff'+str(uuid.uuid4())+photo.filename
        photo.save(path)
        username=request.form['username']  
        password=request.form['password']
        q1="insert into login values(null,'%s','%s','staff')"%(username,password)
        res = insert(q1)
        q2="insert into staff values(null,'%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(name,position,gender,email,place,district,state,contactNo,path,res)
        insert(q2)
        return redirect(url_for('admin.manageStaff'))
    
    return render_template('admin_pages/manage_staff.html',data=data)
    
@admin.route('/police_register',methods=['get','post'])
def policeRegister():
    if 'submit' in request.form:
        policeStation=request.form['police_station']
        place=request.form['place']
        contactNo=request.form['contact_no']
        email=request.form['email_id']
        departmentType=request.form['dept_type']
        username=request.form['username']  
        password=request.form['password']
        q1="insert into login values(null,'%s','%s','police')"%(username,password)
        res = insert(q1)
        q2="insert into police values(null,'%s','%s','%s','%s','%s','%s')"%(policeStation,place,contactNo,email,departmentType,res)
        insert(q2)
        return redirect(url_for('admin.policeRegister'))
    return render_template('admin_pages/policeRegister.html')

@admin.route('/court_register',methods=['get','post'])
def courtRegister():
    if 'submit' in request.form:
        courtName=request.form['court_name']
        courtType=request.form['court_type']
        place=request.form['place']
        district=request.form['district']
        state=request.form['state']
        email=request.form['email_id']
        contactNO=request.form['contact_no']
        username=request.form['username']
        password=request.form['password']
        q1="insert into login values(null,'%s','%s','court')"%(username,password)
        res = insert(q1)
        q2="insert into court values(null,'%s','%s','%s','%s','%s','%s','%s','%s')"%(courtName,courtType,place,district,state,email,contactNO,res)
        insert(q2)
        return redirect(url_for('admin.courtRegister'))
    return render_template('admin_pages/courtRegister.html')

@admin.route('/view_police')
def viewPolice():
    data={}
    q1 = "select * from police"
    data['police']=select(q1)
    return render_template('admin_pages/viewPolice.html',data=data)


@admin.route('/view_court')
def viewCourt():
    data={}
    q1 = "select * from court"
    data['court']=select(q1)
    return render_template('admin_pages/viewCourt.html',data=data)


@admin.route('/view_cases')
def viewCases():
    data={}
    q1 = "select * from cases"
    data['cases']=select(q1)
    return render_template('admin_pages/view_Case.html',data=data)


@admin.route('/assign_collect',methods=['get','post'])
def assignCollect():
    data={}
    d="select * from staff" 
    data['staff']=select(d)
    if 'submit' in request.form:
        forensicStaffId=request.form['ft_id']
        cid=request.args['caseid']
        q2="insert into allocate_staff values(null,'%s','%s','pending','collect')"%(forensicStaffId,cid)
        insert(q2)
        return redirect(url_for('admin.assignCollect'))

    return render_template('admin_pages/asg_collect.html',data=data)
