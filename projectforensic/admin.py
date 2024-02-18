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
    

 



