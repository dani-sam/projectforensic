from flask import *
from database import *
import uuid
from blk import *
from datetime import date,datetime
import  datetime




staff=Blueprint("staff",__name__)
@staff.route("/stf_home")
def stf_hm():
	sid=session['sid']
	if 'action' in request.args:
		action=request.args['action']
		print(action)
	else:
		action=None

	if action=="add":
		q="select * from attendance where fs_id='%s' and date=curdate()"%(sid)
		res=select(q)
		print(res)
		if res:
			flash("Attendance Already Marked")
			return redirect(url_for('staff.stf_hm'))
		else:
			q="insert into attendance values(null,'%s','Present',curdate())"%(sid)
			insert(q)
			flash("Attendance Added")
			return redirect(url_for('staff.stf_hm'))
	return	render_template("staff_home.html")
	

@staff.route("staff_view_case")
def stf_vw_cse():
	data1={}
	q="select * from add_crime "
	ids=select(q)
	data1['x']=ids
	return render_template("staff_view_case.html", data1=data1)



@staff.route("stff_view_allocated_cases")
def stff_view_allocated_cases():
	data1={}
	sid=session['sid']
	q="SELECT * FROM add_crime INNER JOIN `assign_staff` USING(crime_num) where fs_id='%s'"%(sid)
	print(q)
	ids=select(q)
	data1['x']=ids

	if 'action' in request.args:
		action=request.args['action']
		aid=request.args['aid']
		cid=request.args['cid']
		print(action)
	else:
		action=None

	if action=="complete":
		q="update add_crime set status='COLLECTION COMPLETED' where crime_num='%s'"%(aid)
		update(q)
		print(q)
		q="update assign_staff set status='COLLECTION COMPLETED' where crime_num='%s'"%(aid)
		update(q)
		flash("updated....!")
		return redirect(url_for('staff.stff_view_allocated_cases'))
	
	if action=="completeddd":
		q="update add_crime set status='EXAMINATION COMPLETED' where crime_num='%s'"%(aid)
		update(q)
		print(q)
		q="update assign_staff set status='EXAMINATION COMPLETED' where crime_num='%s'"%(aid)
		update(q)
		flash("updated....!")
		return redirect(url_for('staff.stff_view_allocated_cases'))
	return render_template("stff_view_allocated_cases.html", data1=data1)



@staff.route("/staff_profile_updation", methods=['post','get'])
def stf_pr_up():
	data={}
	sid=session['sid']
	x="select * from add_forensic_staff inner join login using(login_id) where fs_id='%s'"%(sid) 
	res=select(x)
	if res:
		data['h']=res
		logid=res[0]['login_id']
	if 'register' in request.form:
		gen=request.form['r1']
		st=request.form['state']
		dis=request.form['district']
		city=request.form['city']
		addr=request.form['addr']
		pincode=request.form['pin']
		alt_ph=request.form['num1']
		passw=request.form['pass']
		pics=request.files['pic']
		path='static/'+str(uuid.uuid4())+pics.filename
		pics.save(path)
		q="update add_forensic_staff set gender='%s', state='%s',district='%s',city='%s',address='%s',pincode='%s',alt_phone='%s', photo='%s' where fs_id='%s'"%(gen,st,dis,city,addr,pincode,alt_ph,path,sid)
		update(q)
		q1="update login set password='%s' where login_id='%s'"%(passw,logid)
		update(q1)
		return redirect(url_for('staff.stf_pr_up'))
	return render_template("staff_profile_updation.html",data=data)


@staff.route("/stff_evi_btn", methods=['post','get'])
def stf_ev_bt():
	cid=request.args['cid']
	if 'evi' in request.form:
		return redirect(url_for('staff.stf_chs_evi',cid=cid))
	if 'digievi' in request.form:
		return redirect(url_for('staff.digitalevi',cid=cid))
	return render_template("staff_evi_button.html")



@staff.route("/digital_evidence", methods=['post','get'])
def digitalevi():
	cid=request.args['cid']
	sid=session['sid']
	if 'submit' in request.form:
		ad=request.files['ad']
		vd=request.files['vd']
		path='static/'+str(uuid.uuid4())+ad.filename
		ad.save(path)
		path1='static/'+str(uuid.uuid4())+vd.filename
		vd.save(path1)
		q="insert into video_audio values(null,'%s','%s','%s','%s',now(),'pending')"%(sid,cid,path,path1)
		insert(q)
		flash("ADDED SUCCESSFULLY.....!")
		return redirect(url_for('staff.stf_ev_bt',cid=cid))
	return render_template("staff_enter_digital_evidence.html")




@staff.route("/stff_chs_evi", methods=['post','get'])
def stf_chs_evi():
	cid=request.args['cid']
	if 'fing' in request.form:
		return redirect(url_for('staff.staff_enter_fing',cid=cid))
	if 'foot' in request.form:
		return redirect(url_for('staff.stf_ent_ft',cid=cid))

	if 'hair' in request.form:
		return redirect(url_for('staff.stf_ent_hair',cid=cid))

	if 'teeth' in request.form:
		return redirect(url_for('staff.stf_ent_teeth',cid=cid))

	if 'bones' in request.form:
		return redirect(url_for('staff.stf_ent_bon',cid=cid))

	if 'post_mortem' in request.form:
		return redirect(url_for('staff.stf_ent_pst_chnges',cid=cid))



	return render_template("staff_choose_evi.html")



@staff.route("/staff_enter_fin", methods=['post','get'])
def staff_enter_fing():
	cid=request.args['cid']
	sid=session['sid']
	if 'sub' in request.form:
		patt=request.form['pattern']
		ref=request.form['ref_point']
		meth=request.form['meth_coll']
		info=request.form['adinfo']
		image=request.files['img']

		path='static/'+str(uuid.uuid4())+image.filename
		image.save(path)

		q="INSERT INTO fingerprint VALUES(NULL,'%s','%s','%s','%s','%s','%s','%s',now(),'pending')"%(cid,sid,patt,ref,meth,info,path)
		insert(q)
		flash("INSERTED SUCCESSFULLY")
		return redirect(url_for('staff.stf_chs_evi',cid=cid))
	return render_template("staff_enter_fing.html")




@staff.route("/staff_enter_foot", methods=['get','post'])
def stf_ent_ft():
	cid=request.args['cid']
	sid=session['sid']
	if 'submit' in request.form:
		len_right_ft=request.form['len_rgt_foot']
		len_left_ft=request.form['len_lft_foot']
		wdt_right_ft=request.form['wdt_rgt_foot']
		wdt_left_ft=request.form['wdt_lft_foot']
		add_inf=request.form['add_info']
		heigh=request.form['height']
		gen=request.form['gender']

		q="INSERT INTO footprint VALUES(NULL,'%s','%s','%s','%s','%s','%s','%s','%s','%s',now(),'pending')"%(cid,sid,len_left_ft,wdt_left_ft,len_right_ft,wdt_right_ft,add_inf,heigh,gen)
		insert(q)
		flash("INSERTED SUCCESSFULLY")
		return redirect(url_for('staff.stf_chs_evi',cid=cid))
	return render_template("staff_enter_foot.html")


@staff.route("/staff_enter_hair", methods=['get','post'])
def stf_ent_hair():
	cid=request.args['cid']
	sid=session['sid']
	if 'hair_sub' in  request.form:
		med_cor_cuti=request.form['medcorcuti']
		diameter_med=request.form['dia_medu']
		diameter_hair=request.form['dia_hair']
		which_part=request.form['which_part']
		barr=request.form['r1']
		animal_or_human=request.form['animalorman']
		gender=request.form['gnd']

		q1="INSERT INTO hair_test VALUES(NULL,'%s','%s','%s','%s','%s','%s','%s','%s','%s','pending')"%(cid,sid,med_cor_cuti,diameter_med,diameter_hair,which_part,barr,animal_or_human,gender)
		insert(q1)
		flash("INSERTED SUCCESSFULLY")
		return redirect(url_for('staff.stf_chs_evi',cid=cid))
	return render_template("staff_enter_hair.html")




@staff.route("/staff_enter_teeth", methods=['post','get'])
def stf_ent_teeth():
	cid=request.args['cid']
	sid=session['sid']
	if 'teeth_sub' in request.form:
		root_diver=request.form['r1']
		appear=request.form['r2']
		color=request.form['r3']
		edge=request.form['r4']
		tem_Per= request.form['tempOrPer']
		tem= request.form['temp_type_teeth']
		perm=request.form['per_type_teeth']

		q2="INSERT INTO teeth VALUES(NULL,'%s','%s','%s','%s','%s','%s','%s','%s','%s', now(),'pending')"%(cid,sid,root_diver,appear,color,edge,tem_Per,tem,perm)
		insert(q2)
		flash("INSERTED SUCCESSFULLY")
		return redirect(url_for('staff.stf_chs_evi',cid=cid))
	return render_template("staff_enter_teeth.html")



@staff.route("/staff_enter_post_mortem", methods=['post','get'])
def stf_ent_pst_chnges():
	cid=request.args['cid']
	sid=session['sid']
	if 'post_changes' in request.form:
		temperature=request.form['temper']
		#change_in_eye=request.form['']
		livor_mortis=request.form['staining']
		degr=request.form['rb']
		death_hors=request.form['death_hrs']
		deg_time=request.form['dgTime']

		q5="INSERT INTO post_mortem VALUES(NULL,'%s','%s','%s','0','%s','%s','%s','%s',now(),'pending')"%(cid,sid,temperature,livor_mortis,degr,death_hors,deg_time)
		insert(q5)
		flash("INSERTED SUCCESSFULLY")
		return redirect(url_for('staff.stf_chs_evi',cid=cid))
	return render_template("staff_enter_postmortem_changes.html")




@staff.route("/staff_enter_bones", methods=['get','post'])
def stf_ent_bon():
	return render_template("staff_enter_bones.html")


@staff.route("/staff_add_attendance", methods=['get','post'])
def staff_add_attendance():
	data={}
	return render_template("staff_add_attendance.html",data=data)




@staff.route("/admin_assign_staff_for_examination", methods=['get','post'])
def admin_assign_staff_for_examination():
	data={}
	ids=request.args['ids']
	return render_template("admin_assign_staff_for_examination.html",data=data)





@staff.route("/staff_evi_verify", methods=['post','get'])
def staff_evi_verify():
	data={}
	cid=request.args['cid']
	q="select * from video_audio where crime_num='%s'"%(cid)
	data['video_audios']=select(q)	
	
	if 'verify_evi' in request.form:
		return redirect(url_for('staff.staff_view_evi',cid=cid))


	
	if 'verify_digievi' in request.form:
		qry="UPDATE `video_audio` SET `va_status`='pending' WHERE `crime_num`='"+cid+"'"
		update(qry)
		return redirect(url_for('staff.staff_verify_digital_evidence',cid=cid))
	return render_template("staff_evi_verify.html",data=data)




@staff.route("/staff_view_evi", methods=['post','get'])
def staff_view_evi():
	data={}
	cid=request.args['cid']
	q1="select * from fingerprint where crime_num='%s'"%(cid)
	data['fingerprints']=select(q1)
	if 'verify_fing' in request.form:
		return redirect(url_for('staff.staff_verify_fing',cid=cid))


	q2="select * from footprint where crime_num='%s'"%(cid)
	data['footprints']=select(q2)
	if 'verify_foot' in request.form:
		return redirect(url_for('staff.staff_verify_foot',cid=cid))

	q3="select * from hair_test where crime_num='%s'"%(cid)
	data['hair_tests']=select(q3)
	if 'verify_hair' in request.form:
		return redirect(url_for('staff.staff_verify_hair',cid=cid))


	q4="select * from teeth where crime_num='%s'"%(cid)
	data['teeths']=select(q4)
	if 'verify_teeth' in request.form:
		return redirect(url_for('staff.staff_verify_teeth',cid=cid))


	q5="select * from post_mortem where crime_num='%s'"%(cid)
	data['post_mortems']=select(q5)
	if 'verify_post_mortem' in request.form:
		return redirect(url_for('staff.staff_verify_post_moterm',cid=cid))



	return render_template("staff_view_evi.html",data=data)



@staff.route("/staff_verify_fing", methods=['post','get'])
def staff_verify_fing():
	data={}
	cid=request.args['cid']
	session['cid']=cid
	q="select * from fingerprint inner join assign_staff using(crime_num) where assign_staff.fs_id='%s'"%(session['sid'])
	print(q)
	r=select(q)
	data['x']=r
	if "action" in request.args:
		action=request.args['action']
	else:
		action=None

	if action=="verify":
		q="select * from fingerprint where crime_num='%s'"%(cid)
		res=select(q)
		if res:
			d=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
			with open(compiled_contract_path) as file:
				contract_json = json.load(file)  # load contract info as JSON
				contract_abi = contract_json['abi']  # fetch contract's abi - necessary to call its functions
			contract = web3.eth.contract(address=deployed_contract_address, abi=contract_abi)
			id=web3.eth.get_block_number()
			message = contract.functions.add_fingerprint(int(id),int(session['cid']),int(session['sid']),res[0]['pattern'],res[0]['ref_point'],res[0]['met_of_coll'],res[0]['add_info'],res[0]['image'],d).transact()
			q="update fingerprint set f_status='verified' where crime_num='%s'"%(cid)
			update(q)
			flash("verified successfully")
			return redirect(url_for('staff.stf_hm',cid=cid))
		
	return render_template("staff_verify_fing.html",data=data)




@staff.route("/staff_verify_foot", methods=['post','get'])
def staff_verify_foot():
	data={}
	cid=request.args['cid']
	session['cid']=cid
	q="select * from footprint inner join assign_staff using(crime_num) where assign_staff.fs_id='%s'"%(session['sid'])
	print(q)
	r=select(q)
	data['x']=r
	if "action" in request.args:
		action=request.args['action']
	else:
		action=None

	if action=="verify":
		q="select * from footprint where crime_num='%s'"%(cid)
		res=select(q)
		if res:
			d=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
			with open(compiled_contract_path) as file:
				contract_json = json.load(file)  # load contract info as JSON
				contract_abi = contract_json['abi']  # fetch contract's abi - necessary to call its functions
			contract = web3.eth.contract(address=deployed_contract_address, abi=contract_abi)
			id=web3.eth.get_block_number()
			message = contract.functions.add_footprint(int(id),int(session['cid']),int(session['sid']),res[0]['left_len'],res[0]['left_width'],res[0]['right_len'],res[0]['right_width'],res[0]['add_info'],res[0]['height'],res[0]['gender'],d).transact()
			q="update footprint set ft_status='verified' where crime_num='%s'"%(cid)
			update(q)
			flash("verified successfully")
			return redirect(url_for('staff.stf_hm',cid=cid))
		
	return render_template("staff_verify_foot.html",data=data)





@staff.route("/staff_verify_hair", methods=['post','get'])
def staff_verify_hair():
	data={}
	cid=request.args['cid']
	session['cid']=cid
	q="select * from hair_test inner join assign_staff using(crime_num) where assign_staff.fs_id='%s'"%(session['sid'])
	print(q)
	r=select(q)
	data['x']=r
	if "action" in request.args:
		action=request.args['action']
	else:
		action=None

	if action=="verify":
		q="select * from hair_test where crime_num='%s'"%(cid)
		res=select(q)
		if res:
			# d=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
			with open(compiled_contract_path) as file:
				contract_json = json.load(file)  # load contract info as JSON
				contract_abi = contract_json['abi']  # fetch contract's abi - necessary to call its functions
			contract = web3.eth.contract(address=deployed_contract_address, abi=contract_abi)
			id=web3.eth.get_block_number()
			message = contract.functions.add_hairtest(int(id),int(session['cid']),int(session['sid']),res[0]['hair_fiber'],res[0]['dia_medu'],res[0]['dia_hair'],res[0]['which_part'],res[0]['pre_barr_bodies'],res[0]['animal_or_human'],res[0]['gender']).transact()
			q="update hair_test set ht_status='verified' where crime_num='%s'"%(cid)
			update(q)
			flash("verified successfully")
			return redirect(url_for('staff.stf_hm',cid=cid))
		
	return render_template("staff_verify_hair.html",data=data)



@staff.route("/staff_verify_teeth", methods=['post','get'])
def staff_verify_teeth():
	data={}
	cid=request.args['cid']
	session['cid']=cid
	q="select * from teeth inner join assign_staff using(crime_num) where assign_staff.fs_id='%s'"%(session['sid'])
	print(q)
	r=select(q)
	data['x']=r
	if "action" in request.args:
		action=request.args['action']
	else:
		action=None

	if action=="verify":
		q="select * from teeth where crime_num='%s'"%(cid)
		res=select(q)
		if res:
			d=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
			with open(compiled_contract_path) as file:
				contract_json = json.load(file)  # load contract info as JSON
				contract_abi = contract_json['abi']  # fetch contract's abi - necessary to call its functions
			contract = web3.eth.contract(address=deployed_contract_address, abi=contract_abi)
			id=web3.eth.get_block_number()
			message = contract.functions.add_teeth(int(id),int(session['cid']),int(session['sid']),res[0]['root_diver'],res[0]['appear'],res[0]['color'],res[0]['edge'],res[0]['teeth_ident'],res[0]['temp_typ_teeth'],res[0]['per_typ_teeth'],d).transact()
			q="update teeth set t_status='verified' where crime_num='%s'"%(cid)
			update(q)
			flash("verified successfully")
			return redirect(url_for('staff.stf_hm',cid=cid))
		
	return render_template("staff_verify_teeth.html",data=data)






# @staff.route("/staff_verify_bones", methods=['post','get'])
# def staff_verify_bones():		
# 	return render_template("staff_verify_bones.html",data=data)




@staff.route("/staff_verify_post_moterm", methods=['post','get'])
def staff_verify_post_moterm():
	data={}
	cid=request.args['cid']
	session['cid']=cid
	q="select * from post_mortem inner join assign_staff using(crime_num) where assign_staff.fs_id='%s'"%(session['sid'])
	print(q)
	r=select(q)
	data['x']=r
	if "action" in request.args:
		action=request.args['action']
	else:
		action=None

	if action=="verify":
		q="select * from post_mortem where crime_num='%s'"%(cid)
		res=select(q)
		if res:
			d=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
			with open(compiled_contract_path) as file:
				contract_json = json.load(file)  # load contract info as JSON
				contract_abi = contract_json['abi']  # fetch contract's abi - necessary to call its functions
			contract = web3.eth.contract(address=deployed_contract_address, abi=contract_abi)
			id=web3.eth.get_block_number()
			message = contract.functions.add_post_mortem(int(id),int(session['cid']),int(session['sid']),res[0]['body_temp'],res[0]['changes_in_eye'],res[0]['livor_mortis'],res[0]['degradation'],res[0]['time_snc_death_in_hrs'],res[0]['degradation_time'],d).transact()
			q="update post_mortem set pm_status='verified' where crime_num='%s'"%(cid)
			update(q)
			flash("verified successfully")
			return redirect(url_for('staff.stf_hm',cid=cid))
		
	return render_template("staff_verify_post_moterm.html",data=data)







@staff.route("/staff_verify_digital_evidence", methods=['post','get'])
def staff_verify_digital_evidence():
	data={}
	cid=request.args['cid']
	session['cid']=cid
	q="select * from video_audio inner join assign_staff using(crime_num) where assign_staff.fs_id='%s'"%(session['sid'])
	print(q)
	r=select(q)
	data['x']=r
	if "action" in request.args:
		action=request.args['action']
	else:
		action=None

	if action=="verify":
		kk="update video_audio set va_status='verified' where crime_num='%s'"%(cid)
		update(kk)

		q="select * from video_audio where crime_num='%s'"%(cid)
		res=select(q)
		if res:
			d=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
			with open(compiled_contract_path) as file:
				contract_json = json.load(file)  # load contract info as JSON
				contract_abi = contract_json['abi']  # fetch contract's abi - necessary to call its functions
			contract = web3.eth.contract(address=deployed_contract_address, abi=contract_abi)
			id=web3.eth.get_block_number()
			message = contract.functions.add_video_audio(int(id),int(session['cid']),int(session['sid']),res[0]['audio'],res[0]['video'],d).transact()
			flash("added successfully")
			return redirect(url_for('staff.stf_hm',cid=cid))
	return render_template("staff_verify_digital_evidence.html",data=data)