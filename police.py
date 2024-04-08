from flask import *
from database import *
from blk import *

police=Blueprint('police',__name__)

@police.route("/police_home")
def pol_home():
	return render_template("police_home.html")
@police.route("/police_report")
def police_report():

	data={}
	# case_num=request.args['case_num']
	# session['case_num']=case_num
	# cid=session['cid']
	q1="select * from add_crime where station_num='%s'"%(session['pid'])
	# q1="SELECT * FROM `request_evidence` INNER JOIN`add_crime` USING(`case_num`) WHERE `case_num`='%s'"%(session['case_num'])
	res1=select(q1)
	if res1:
		session['crime_num1']=res1[0]['crime_num']
		print(session['crime_num1'])
		# ///////////////////////////////////////fetching values from block///////////////////////


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
					if int(decoded_input[1]['crime_no']) == int(session['crime_num1']):
						res.append(decoded_input[1])
		except Exception as e:
			print("", e)
		data['view']=res
		print("/////////",res)
		if res:
			q1="SELECT * FROM fingerprint inner join add_crime using(crime_num) where f_status='verified' and crime_num='%s' "%(res[0]['crime_no'])
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
					if int(decoded_input[1]['crime_no']) == int(session['crime_num1']):
						res.append(decoded_input[1])
		except Exception as e:
			print("", e)
		data['view']=res
		print("/////////",res)
		if res:
			q2="SELECT * FROM footprint inner join add_crime using(crime_num) where ft_status='verified'and crime_num='%s' "%(res[0]['crime_no'])
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
					if int(decoded_input[1]['crime_no']) == int(session['crime_num1']):
						res.append(decoded_input[1])
		except Exception as e:
			print("", e)
		data['view']=res
		print("/////////",res)
		if res:
			q3="SELECT * FROM hair_test inner join add_crime using(crime_num) where ht_status='verified'and crime_num='%s' "%(res[0]['crime_no'])
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
					if int(decoded_input[1]['crime_no']) == int(session['crime_num1']):
						res.append(decoded_input[1])
		except Exception as e:
			print("", e)
		data['view']=res
		print("/////////",res)
		if res:
			q4="SELECT * FROM teeth inner join add_crime using(crime_num) where t_status='verified'and crime_num='%s' "%(res[0]['crime_no'])
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
					if int(decoded_input[1]['crime_no']) == int(session['crime_num1']):
						res.append(decoded_input[1])
		except Exception as e:
			print("", e)
		data['view']=res
		print("/////////",res)
		if res:
			q5="SELECT * FROM post_mortem inner join add_crime using(crime_num) where pm_status='verified'and crime_num='%s' "%(res[0]['crime_no'])
			data['post_mortems']=select(q5)
	# ////////////////////////////////post_mortem-END////////////////////////////////////////////

	# ///////////////////////////////////////fetching values from block--end///////////////////////


			
	return render_template("police_report.html",data=data)

# @police.route("/police_report")
# def police_report():
# 	data={}
# 	q="select * from add_crime where station_num='%s'"%(session['pid'])
# 	res=select(q)
# 	if res:
# 		cid=res[0]['crime_num']
# 		q1="select * from fingerprint where crime_num='%s'"%(cid)
# 		data['fingerprints']=select(q1)
		
# 		q2="select * from footprint where crime_num='%s'"%(cid)
# 		data['footprints']=select(q2)
		
# 		q3="select * from hair_test where crime_num='%s'"%(cid)
# 		data['hair_tests']=select(q3)
		

# 		q4="select * from teeth where crime_num='%s'"%(cid)
# 		data['teeths']=select(q4)
		

# 		q5="select * from post_mortem where crime_num='%s'"%(cid)
# 		data['post_mortems']=select(q5)
	

			
# 	return render_template("police_report.html",data=data)






@police.route("/add_crime", methods=['get','post'])
def pol_add_crm():
	data={}
	pid=session['pid']
	sn=session['sn']
	data['sn']=sn
	if 'add_crime' in request.form:
		firstname=request.form['fname']
		lastname=request.form['lname']
		designation=request.form['desi']
		case_num=request.form['case_num']
		ty_crime=request.form['crime']
		lat=request.form['latit']
		lon=request.form['longi']

		q="INSERT INTO add_crime VALUES(NULL,'%s','%s','%s','%s','%s','%s','%s','%s','pending',curdate())"%(pid,firstname,lastname,designation,case_num,ty_crime,lat,lon)
		insert(q)
		flash("CRIME ADDED")
		return redirect(url_for("police.pol_home"))
	return render_template("police_add_crime.html",data=data)


@police.route("/view_crime")
def pol_view_crm():
	data={}
	pid=session['pid']
	q1="select * , concat(fname,' ',lname) as name from add_crime where station_num='%s'"%(pid)
	ids1=select(q1)
	data['i']=ids1
	return render_template("police_view_crime.html",data=data)




	



