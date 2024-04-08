from flask import Flask,Blueprint,render_template,url_for,request,redirect,flash,session
from database import *

public=Blueprint('public',__name__)
@public.route("/")
def index():
	return render_template("home.html")

@public.route("/login", methods=['post','get'])
def log_form():
	if 'login' in request.form:
		username=request.form['uname']
		password=request.form['pass']	
		q="SELECT * FROM login WHERE username='%s' AND PASSWORD='%s'"%(username,password)
		res=select(q)
		print('================',q)

		if res:
			utype=res[0]['usertype']
			
			session['lid']=res[0]['login_id']
			if utype=='admin':
				flash("LOGIN SUCCESSFULLY")
				return redirect(url_for('admin.adm_home'))
			elif utype=='POLICE':
				q="SELECT * FROM police_station where login_id='%s'"%(session['lid'])
				res=select(q)
				if res:
					session['pid']=res[0]['station_num']
					session['sn']=res[0]['station_name']
				flash("LOGIN SUCCESSFULLY")
				return redirect(url_for('police.pol_home'))
			elif utype=='COURT':
				q="select * from court where login_id='%s'"%(session['lid'])
				res=select(q)
				if res:
					session['cid']=res[0]['court_id']
				flash("LOGIN SUCCESSFULLY")
				return redirect(url_for('court.crt_hom'))
			elif utype=='FORENSIC STAFF':
				print('================')
				q="select * from add_forensic_staff where login_id='%s'"%(session['lid'])

				res=select(q)
				if res:
					session['sid']=res[0]['fs_id']
				flash("LOGIN SUCCESSFULLY")
				return redirect(url_for('staff.stf_hm'))
		else:
			flash("INVALID USERNAME OR PASSWORD")

	return render_template("login.html")



@public.route("/police_registration",methods=['post','get'])
def police_registration():
	if 'register' in request.form:
		reg_num=request.form['reg_num']
		zone=request.form['zone']
		dis=request.form['district']
		city=request.form['city']
		pin=request.form['pincode']
		st_name=request.form['stname']
		addr=request.form['adr']
		email=request.form['email']
		ph1=request.form['num1']
		ph2=request.form['altnum']
		rety_pass=request.form['pass1']
		username=request.form['uname']
		password=request.form['pass']

		q1="SELECT * FROM login WHERE username='%s'"%(username) 
		res=select(q1)
		if res:
			flash("EXISTING USERNAME")
			
		else:
			q="INSERT INTO login values(NULL,'%s','%s','POLICE')"%(username,password)
			ids=insert(q)
			qq="INSERT INTO police_station values(NULL,'%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','pending')"%(ids,reg_num,zone,dis,city,pin,st_name,addr,email,ph1,ph2)
			insert(qq)
			flash("REGISTER SUCCESSFULLY")
			return redirect(url_for("public.log_form"))
	return render_template("police_registration.html")



@public.route("/court_registration",methods=['post','get'])
def court_reg():
	if 'reg' in request.form:
		reg_num=request.form['regnum']
		crt_name=request.form['cname']
		ty_court=request.form['ty_court']
		state=request.form['state']
		dist=request.form['dis']
		addr=request.form['addr']
		pin=request.form['pin']
		mail=request.form['mail']
		of_phone=request.form['phone1']
		al_phone=request.form['phone2']
		of_name=request.form['name']
		rety_pass=request.form['pass1']
		username=request.form['uname']
		password=request.form['pass']
		q2="SELECT * FROM login WHERE username='%s'"%(username) 
		print(q2)
		res=select(q2)
		if res:
			flash("EXISTING USERNAME")
		else:
			q1="INSERT INTO login VALUES(NULL,'%s','%s','COURT')"%(username,password)
			ids=insert(q1)
			q2="INSERT INTO court VALUES(NULL,'%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','pending')"%(ids,crt_name,reg_num,ty_court,state,dist,addr,pin,mail,of_phone,al_phone,of_name)
			print(q2)
			insert(q2)
			flash("REGISTER SUCCESSFULLY")
			return redirect(url_for("public.log_form"))
	return render_template("court_registration.html")








