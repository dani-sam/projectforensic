from flask import *
from database import *
import random
import uuid
from blk import *
from datetime import date,datetime
import  datetime

import smtplib
from email.mime.text import MIMEText
from flask_mail import Mail

admin=Blueprint('admin',__name__)

# ///////////////////////////////////////fetching values from block///////////////////////
@admin.route("/admin_evidence_report")
def admin_evidence_report():
	data={}

	with open(compiled_contract_path) as file:
		contract_json = json.load(file)  # load contract info as JSON
		contract_abi = contract_json['abi']  # fetch contract's abi - necessary to call its functions
	contract = web3.eth.contract(address=deployed_contract_address, abi=contract_abi)
	blocknumber = web3.eth.get_block_number()
	res = []
	try:
		for i in range(blocknumber, 0, -1):
			a = web3.eth.get_transaction_by_block(i, 0)
			decoded_input = contract.decode_function_input(a['input'])
			print(decoded_input)
			if str(decoded_input[0]) == "<Function add_fingerprint(uint256,uint256,uint256,string,string,string,string,string,string)>":
				# if int(decoded_input[1]['court_id']) == int(session['cid']):
					res.append(decoded_input[1])
	except Exception as e:
		print("", e)
	data['view']=res
	print("/////////",res)
	if res:
		q1="SELECT * FROM fingerprint inner join add_crime using(crime_num) where f_status='verified'"
		data['fingerprints']=select(q1)
# ////////////////////////////////fingerprint-end////////////////////////////////////////////


# ////////////////////////////////footprint////////////////////////////////////////////////
	with open(compiled_contract_path) as file:
		contract_json = json.load(file)  # load contract info as JSON
		contract_abi = contract_json['abi']  # fetch contract's abi - necessary to call its functions
	contract = web3.eth.contract(address=deployed_contract_address, abi=contract_abi)
	blocknumber = web3.eth.get_block_number()
	res = []
	try:
		for i in range(blocknumber, 0, -1):
			a = web3.eth.get_transaction_by_block(i, 0)
			decoded_input = contract.decode_function_input(a['input'])
			print(decoded_input)
			if str(decoded_input[0]) == "<Function add_footprint(uint256,uint256,uint256,string,string,string,string,string,string,string,string)>":
				# if int(decoded_input[1]['court_id']) == int(session['cid']):
					res.append(decoded_input[1])
	except Exception as e:
		print("", e)
	data['view']=res
	print("/////////",res)
	if res:
		q2="SELECT * FROM footprint inner join add_crime using(crime_num) where ft_status='verified'"
		data['footprints']=select(q2)
# ////////////////////////////////footprint-END////////////////////////////////////////////



# ////////////////////////////////hair-test////////////////////////////////////////////////
	with open(compiled_contract_path) as file:
		contract_json = json.load(file)  # load contract info as JSON
		contract_abi = contract_json['abi']  # fetch contract's abi - necessary to call its functions
	contract = web3.eth.contract(address=deployed_contract_address, abi=contract_abi)
	blocknumber = web3.eth.get_block_number()
	res = []
	try:
		for i in range(blocknumber, 0, -1):
			a = web3.eth.get_transaction_by_block(i, 0)
			decoded_input = contract.decode_function_input(a['input'])
			print(decoded_input)
			if str(decoded_input[0]) == "<Function add_hairtest(uint256,uint256,uint256,string,string,string,string,string,string,string)>":
				# if int(decoded_input[1]['court_id']) == int(session['cid']):
					res.append(decoded_input[1])
	except Exception as e:
		print("", e)
	data['view']=res
	print("/////////",res)
	if res:
		q3="SELECT * FROM hair_test inner join add_crime using(crime_num) where ht_status='verified'"
		data['hair_tests']=select(q3)
# ////////////////////////////////hair-test-END////////////////////////////////////////////



# ////////////////////////////////teeth////////////////////////////////////////////////
	with open(compiled_contract_path) as file:
		contract_json = json.load(file)  # load contract info as JSON
		contract_abi = contract_json['abi']  # fetch contract's abi - necessary to call its functions
	contract = web3.eth.contract(address=deployed_contract_address, abi=contract_abi)
	blocknumber = web3.eth.get_block_number()
	res = []
	try:
		for i in range(blocknumber, 0, -1):
			a = web3.eth.get_transaction_by_block(i, 0)
			decoded_input = contract.decode_function_input(a['input'])
			print(decoded_input)
			if str(decoded_input[0]) == "<Function add_teeth(uint256,uint256,uint256,string,string,string,string,string,string,string,string)>":
				# if int(decoded_input[1]['court_id']) == int(session['cid']):
					res.append(decoded_input[1])
	except Exception as e:
		print("", e)
	data['view']=res
	print("/////////",res)
	if res:
		q4="SELECT * FROM teeth inner join add_crime using(crime_num) where t_status='verified'"
		data['teeths']=select(q4)
# ////////////////////////////////teeth-END////////////////////////////////////////////

	

# ////////////////////////////////post_mortem////////////////////////////////////////////////
	with open(compiled_contract_path) as file:
		contract_json = json.load(file)  # load contract info as JSON
		contract_abi = contract_json['abi']  # fetch contract's abi - necessary to call its functions
	contract = web3.eth.contract(address=deployed_contract_address, abi=contract_abi)
	blocknumber = web3.eth.get_block_number()
	res = []
	try:
		for i in range(blocknumber, 0, -1):
			a = web3.eth.get_transaction_by_block(i, 0)
			decoded_input = contract.decode_function_input(a['input'])
			print(decoded_input)
			if str(decoded_input[0]) == "<Function add_post_mortem(uint256,uint256,uint256,string,string,string,string,string,string,string)>":
				# if int(decoded_input[1]['court_id']) == int(session['cid']):
					res.append(decoded_input[1])
	except Exception as e:
		print("", e)
	data['view']=res
	print("/////////",res)
	if res:
		q5="SELECT * FROM post_mortem inner join add_crime using(crime_num) where pm_status='verified'"
		data['post_mortems']=select(q5)
# ////////////////////////////////post_mortem-END////////////////////////////////////////////

		
	return render_template("admin_evidence_report.html",data=data)
# ///////////////////////////////////////fetching values from block--end///////////////////////



@admin.route("/admin_home")

def adm_home():
	return render_template("admin_home.html")


@admin.route("/admin_add_staff",methods=['post','get'])
def admin_add_forensic_staff():
	data={}
	num=random.randint(000000,1000000)
	print(num)
	if 'register' in request.form:
		fname=request.form['fname']
		lname=request.form['lname']
		gender=request.form['r1']
		dob=request.form['DOB']
		state=request.form['state']
		dis=request.form['district']
		city=request.form['city']
		add=request.form['addr']
		pin=request.form['pin']
		phone=request.form['num']
		alt_ph=request.form['num1']
		email1=request.form['email']
		doj=request.form['doj']
		photo=request.files['pic']
		path='static/'+str(uuid.uuid4())+photo.filename
		photo.save(path)

		q="INSERT INTO `login` VALUES(NULL,'%s','%s','FORENSIC STAFF')"%(num,dob)
		ids=insert(q)
		q1="INSERT INTO add_forensic_staff VALUES(NULL,'%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(ids,fname,lname,gender,dob,state,dis,city,add,pin,phone,alt_ph,email1,doj,path)
		insert(q1)


		num1=str(num)
		dob1=str(dob)

		pwd="DEAR "+ fname+",\n YOUR TEMPORARY USERNAME AND PASSWORD .......!"+"\nUSERNAME : "+num1+"\nPASSWORD : "+dob1+""

		try:
		
			gmail = smtplib.SMTP('smtp.gmail.com', 587)
			gmail.ehlo()
			gmail.starttls()
			gmail.login('teambrightmart@gmail.com','wluwtslqrxalyqpg')
		except Exception as e:
			print("Couldn't setup email!!"+str(e))

		pwd = MIMEText(pwd)

		pwd['Subject'] = 'Confirmation'

		pwd['To'] = email1

		pwd['From'] = 'sngistoutpass@gmail.com'

		try:
			gmail.send_message(pwd)

			flash("EMAIL SENED SUCCESFULLY")



		except Exception as e:
			print("COULDN'T SEND EMAIL", str(e))
		else:
			flash('ADDED...')
		return redirect(url_for('admin.admin_add_forensic_staff'))
	return render_template("admin_add_forensic_staff.html",data=data)




@admin.route("/admin_view_forensic_staff", methods=['post','get'])
def admin_view_staff():
	data={}
	q2="SELECT *, concat(fname,' ',lname) as name FROM add_forensic_staff"
	ids1=select(q2)
	data['i']=ids1

	if 'action' in request.args:
		action=request.args['action']
		id=request.args['id']
	else:
		action=None

	if action=="delete":
		q="delete from add_forensic_staff where login_id='%s'"%(id)
		delete(q)
		q="delete from login where login_id='%s'"%(id)
		delete(q)
		return redirect(url_for('admin.admin_view_staff'))
	

	return render_template("admin_view_staff.html",data=data)


@admin.route("/admin_view_reg_police", methods=['post','get'])
def admin_view_pol():
	data1={}
	q3="SELECT * FROM police_station"
	ids2=select(q3)
	data1['i']=ids2

	if 'action' in request.args:
		action=request.args['action']
		id=request.args['id']
	else:
		action=None

	if action=="delete":
		q1="delete from police_station where login_id='%s'"%(id)
		delete(q1)
		q1="delete from login where login_id='%s'"%(id)
		delete(q1)
		flash("DELETTED SUCCESSFULLY")
		return redirect(url_for('admin.admin_view_pol'))
	
	if action=="accept":
		q1="update police_station set status='accept' where login_id='%s'"%(id)
		delete(q1)
		flash("Accepted SUCCESSFULLY")
		return redirect(url_for('admin.admin_view_pol'))
	return render_template("admin_view_police.html",data1=data1)


@admin.route("/admin_view_crimes", methods=['post','get'])
def admin_view_crimes():
	data1={}
	q3="SELECT police_station.*,add_crime.*,add_crime.status as st FROM police_station INNER JOIN `add_crime` on add_crime.station_num=police_station.station_num GROUP BY police_station.`station_num`"
	
	ids2=select(q3)
	data1['i']=ids2
	print(ids2)
	return render_template("admin_view_crimes.html",data1=data1)

@admin.route("/admin_view_reg_court", methods=['post','get'])
def admin_view_reg_court():
	data1={}
	q3="SELECT * FROM court"
	ids2=select(q3)
	data1['i']=ids2

	if 'action' in request.args:
		action=request.args['action']
		id=request.args['id']
	else:
		action=None

	if action=="delete":
		q1="delete from court where login_id='%s'"%(id)
		delete(q1)
		q1="delete from login where login_id='%s'"%(id)
		delete(q1)
		flash("DELETTED SUCCESSFULLY")
		return redirect(url_for('admin.admin_view_reg_court'))
	
	if action=="accept":
		q1="update court set status='accept' where login_id='%s'"%(id)
		update(q1)
		flash("ACCEPTED SUCCESSFULLY")
		return redirect(url_for('admin.admin_view_reg_court'))
	
	return render_template("admin_view_reg_court.html",data1=data1)



@admin.route("/admin_view_crimess", methods=['post','get'])
def admin_view_crimess():
	data={}
	id=request.args['id']
	qr="select *,concat(fname,' ',lname)  as name from add_crime inner join police_station using (station_num) where station_num='%s'"%(id)
	ids=select(qr)
	data['k']=ids
	print(ids)

	# if 'allocate' in request.form:
	# 	return redirect(url_for('admin.admin_assign_staff'))
	return render_template("admin_view_crimess.html",data=data)


@admin.route("/admin_view_crime", methods=['post','get'])
def adm_vw_crm():
	data={}
	qr="select *,concat(fname,' ',lname)  as name, add_crime.status as st  from add_crime inner join police_station using (station_num)"
	print(qr)
	ids=select(qr)
	data['k']=ids
	print(ids)
	return render_template("admin_view_crime.html",data=data)




@admin.route("/admin_view_evi_req", methods=['post','get'])
def admin_view_evidence_req():
	data={}
	q="SELECT *,request_evidence.status as st FROM request_evidence INNER JOIN court USING(court_id) INNER JOIN add_crime USING(case_num)"
	res=select(q)
	data['evidence']= res


	if 'action' in request.args:
		action=request.args['action']
		id=request.args['id']
	else:
		action=None

	if action=="accept":
		q1="update request_evidence set status='Accepted' where req_ev_no='%s'"%(id)
		update(q1)
		q1="select * from request_evidence where req_ev_no='%s'"%(id)
		print(q1)
		res=select(q1)
		print(res[0]['court_id'])
		print(res[0]['case_num'])
		print(res[0]['status'])
		d=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
		with open(compiled_contract_path) as file:
			contract_json = json.load(file)  # load contract info as JSON
			contract_abi = contract_json['abi']  # fetch contract's abi - necessary to call its functions
		contract = web3.eth.contract(address=deployed_contract_address, abi=contract_abi)
		id=web3.eth.get_block_number()
		
		message = contract.functions.add_request_evidence(int(id),int(res[0]['court_id']),int(res[0]['case_num']),res[0]['status'],d).transact()
		print(message)
		flash("ACCEPTED....!")
		return redirect(url_for('admin.admin_view_evidence_req'))
	return render_template("admin_view_court_req.html",data=data)



@admin.route("/admin_assign_staff", methods=['post','get'])
def admin_assign_staff():
	data={}
	ids=request.args['ids']
	q="SELECT * FROM add_forensic_staff INNER JOIN `attendance` USING(fs_id) INNER JOIN `login` USING(login_id)"
	print(q)
	res=select(q)
	
	if res:
		for i in res:
			fs_id=i['fs_id']
			print(fs_id)
			# q="SELECT * FROM add_forensic_staff INNER JOIN `attendance` USING(fs_id) INNER JOIN `login` USING(login_id) where fs_id not in(select fs_id from assign_staff )"
			q="SELECT * FROM add_forensic_staff INNER JOIN `attendance` USING(fs_id) INNER JOIN `login` USING(login_id) WHERE `attendance`.`date`=CURDATE() AND fs_id NOT IN(SELECT fs_id FROM assign_staff WHERE `assign_staff`.`status` !='COLLECTION COMPLETED' )"
			data['staff']=select(q)
			print("))))",q)
	if 'assign' in request.form:
		stf=request.form['stf']
		q="select * from assign_staff where status='pending' and fs_id='%s'"%(stf)
		res=select(q)
		if res:
			flash("Already Assigned...!")

		else:
			q="insert into assign_staff values(null,'%s','%s','pending')"%(stf,ids)
			insert(q)
			q="update add_crime set status='ASSIGN STAFF FOR COLLECTION' where crime_num='%s'"%(ids)
			update(q)
			flash("Assigned....!")
			return redirect(url_for('admin.admin_view_crimes'))
	return render_template("admin_assign_staff.html",data=data)


@admin.route("/admin_assign_staff_for_examination", methods=['get','post'])
def admin_assign_staff_for_examination():
	data={}
	ids=request.args['ids']
	q="SELECT * FROM add_forensic_staff INNER JOIN `attendance` USING(fs_id) INNER JOIN `login` USING(login_id) ORDER BY RAND()"
	res=select(q)
	# data['staff']=res
	if res:
		for i in res:
			fs_id=i['fs_id']
			print(fs_id)
			# q="SELECT * FROM add_forensic_staff INNER JOIN `attendance` USING(fs_id) INNER JOIN `login` USING(login_id) where fs_id not in(select fs_id from assign_staff ) ORDER BY RAND()"
			q="SELECT * FROM add_forensic_staff INNER JOIN `attendance` USING(fs_id) INNER JOIN `login` USING(login_id) WHERE `attendance`.`date`=CURDATE() AND fs_id NOT IN(SELECT fs_id FROM assign_staff WHERE `assign_staff`.`status` NOT  LIKE '%COLLECTION' ) ORDER BY RAND()"
			print(q)
			data['staff']=select(q)
			print("))))",q)
	if 'assign' in request.form:
		stf=request.form['stf']
		q="select * from assign_staff where status='pending' and fs_id='%s'"%(stf)
		res=select(q)
		if res:
			flash("Already Assigned...!")

		else:
			q="insert into assign_staff values(null,'%s','%s','ASSIGN STAFF FOR EXAMINATION')"%(stf,ids)
			insert(q)
			q="update add_crime set status='ASSIGN STAFF FOR EXAMINATION' where crime_num='%s'"%(ids)
			update(q)
			flash("Assigned....!")
			return redirect(url_for('admin.adm_vw_crm'))
	return render_template("admin_assign_staff_for_examination.html",data=data)




@admin.route("/admin_print_report", methods=['post','get'])
def admin_print_report():
	data={}
	
	return render_template("admin_print_report.html",data=data)