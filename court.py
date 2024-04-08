from flask import *
from database import *
from blk import *

court=Blueprint('court',__name__)
@court.route("/court_home")


def crt_hom():
	return render_template("court_home.html")


# @court.route("/crt_req_evi", methods=['post','get'])
# def court_req_evid():

# 	cid=session['cid']
# 	if 'req' in request.form:
# 		case_num=request.form['cas_no']
# 		# q="select * from add_crime"
# 		# res=select(q)
# 		# if res:
# 		# 	for i in res:
# 		# 		snum=i['case_num']
# 		# 		print(snum)
# 		# 		print(case_num)
# 		# 		if snum==case_num:
# 		q="select * from request_evidence where case_num='%s' and court_id='%s'"%(case_num,cid)
# 		r=select(q)
# 		# if r:
# 		# 	flash("Request Already Send")
# 		# 	return redirect(url_for('court.crt_hom'))
# 		if r:
# 			q1="INSERT INTO request_evidence VALUES(NULL,'%s','%s','pending')"%(case_num, cid)
# 			insert(q1)
# 			lo="update add_crime set status='pending' where case_num='%s'"%(case_num)
# 			update(lo)
# 			flash("REQUEST SEND SUCCESSFULLY")
# 			return redirect(url_for('court.crt_hom'))
# 				# else:
# 				# 	flash("INVALID CASE DETAILS")
# 				# 	return redirect(url_for('court.crt_hom'))
# 	return render_template("court_req_eveidence.html")



@court.route("/crt_req_evi", methods=['POST', 'GET'])
def court_req_evid():
    cid = session.get('cid')
    
    if 'req' in request.form:
        case_num = request.form.get('cas_no')
        q = "SELECT * FROM request_evidence WHERE case_num='%s' AND court_id='%s'" % (case_num, cid)
        r = select(q)
        
        if not r:
            q1 = "INSERT INTO request_evidence VALUES (NULL, '%s', '%s', 'pending')" % (case_num, cid)
            insert(q1)
            lo = "UPDATE add_crime SET status='pending' WHERE case_num='%s'" % case_num
            update(lo)
            flash("REQUEST SENT SUCCESSFULLY")
        else:
            flash("REQUEST SENT SUCCESSFULLY")

        return redirect(url_for('court.crt_hom'))

    return render_template("court_req_eveidence.html")



@court.route("/crt_view_request")
def crt_view_request():
	data={}
	cid=session['cid']
	# q="SELECT *,request_evidence.status as st FROM `request_evidence` INNER JOIN `add_crime` USING(case_num) where court_id='%s'"%(cid)
	# res=select(q)
	# data['req']=res
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
			if str(decoded_input[0]) == "<Function add_request_evidence(uint256,uint256,uint256,string,string)>":
				if int(decoded_input[1]['court_id']) == int(session['cid']):
					res.append(decoded_input[1])
	except Exception as e:
		print("", e)
	data['view']=res

	print(res)
	if res:
		q="SELECT * FROM `request_evidence` INNER JOIN `add_crime` USING(case_num) where court_id='%s' and `request_evidence`.`STATUS`='Accepted'"%(cid)
		res1=select(q)
		print(res1,"000000000")
		data['views']=res1
		data['case_num']=res1[0]['case_num']
		data['status']=res1[0]['status']
				
	return render_template("crt_view_request.html",data=data)


@court.route("/crt_view_evidences")
def crt_view_evidences():
	data={}
	case_num=request.args['case_num']
	session['case_num']=case_num
	cid=session['cid']
	q1="SELECT * FROM `request_evidence` INNER JOIN`add_crime` USING(`case_num`) WHERE `case_num`='%s'"%(session['case_num'])
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


			
	return render_template("crt_view_evidences.html",data=data)


@court.route("/crt_view_digital_evidence", methods=['post','get'])
def crt_view_digital_evidence():
	data={}
	case_num=request.args['case_num']
	session['case_num']=case_num
	cid=session['cid']
	q1="SELECT * FROM `request_evidence` INNER JOIN`add_crime` USING(`case_num`) WHERE `case_num`='%s'"%(session['case_num'])
	res1=select(q1)
	if res1:
		session['crime_num1']=res1[0]['crime_num']
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
			jk="select * from video_audio where crime_num='%s'"%(session['crime_num1'])
			data['jk']=select(jk)
	return render_template("crt_view_digital_evidence.html",data=data)