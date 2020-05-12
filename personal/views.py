from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect ,csrf_exempt
import sys
import requests
import json 
from django.conf import settings
import subprocess
import pathlib
##subprocess.call(["python","file"])

# Create your views here.

def test(request):
	return render(request,'personal/test.html')


@csrf_protect
def Query(request):
	file_dir = str(pathlib.Path(__file__).parent.absolute())+'/classification_model'
	data=request.POST
	input_data=data["feedback"]
	data = []
	with open(file_dir+'/data/small_samples.json') as jf:
		data = json.load(jf)
		jf.close()
	data.append({
		'comments':input_data,
		'category':'train delay'
		})
	with open(file_dir+'/data/small_samples.json', 'w') as jf:
		json.dump(data, jf)
		jf.close()
	cmd = ['python', file_dir+'/predict.py']
	subprocess.check_call(cmd)

	with open(file_dir+'/data/small_samples_prediction.json') as jf:
		data = json.load(jf)
		jf.close()
	predict = data[data.__len__() - 1]['new_prediction']

	return render(request,'personal/show.html', {'dep':str(predict)})

















# from django.shortcuts import render, redirect
# from django.db import connection
# from django.views.decorators.csrf import csrf_protect ,csrf_exempt
# import shlex, subprocess
# import os,sys
# import json
# import time
# import re
	
# # Create your views here.


# def index(request):
# 	return render(request,'personal/home.html') 

# def discard(request, contact):
# 	with connection.cursor() as cursor:
# 		cursor.execute("delete from feedback where phone_no='{}'".format(contact))
# 	return redirect('/index')

# def admin_home(request):
# 	with connection.cursor() as cursor:
# 		cursor.execute("SELECT timestamp, class, data from feedback limit 5")
# 		alld = list(cursor.fetchall())
# 		for i in range(alld.__len__()):
# 			alld[i] = list(alld[i])
# 		cursor.execute("SELECT timestamp, class, data from feedback where status=\"unresolved\" limit 5")
# 		unresolved = list(cursor.fetchall())
# 		for i in range(unresolved.__len__()):
# 			unresolved[i] = list(unresolved[i])
# 		cursor.execute("SELECT timestamp, class, data from feedback where status=\"resolved\" limit 5")
# 		resolved = list(cursor.fetchall())
# 		for i in range(resolved.__len__()):
# 			resolved[i] = list(resolved[i])
# 		cursor.execute("SELECT timestamp, class, data from feedback where status=\"queued\" limit 5")
# 		queued = list(cursor.fetchall())
# 		for i in range(queued.__len__()):
# 			queued[i] = list(queued[i])
# 		cursor.execute("SELECT count(*) from feedback")
# 		temp = list(cursor.fetchone())
# 		count = []
# 		count.append(temp[0])
# 		cursor.execute("SELECT count(*) from feedback where status=\"resolved\"")
# 		temp = list(cursor.fetchone())
# 		count.append(temp[0])
# 		cursor.execute("SELECT count(*) from feedback where status=\"queued\"")
# 		temp = list(cursor.fetchone())
# 		count.append(temp[0])
# 		cursor.execute("SELECT count(*) from feedback where status=\"unresolved\"")
# 		temp = list(cursor.fetchone())
# 		count.append(temp[0])
# 	return render(request,'personal/admin_home.html', {'all':alld, 'unr':unresolved, 'res':resolved, 'que':queued, 'count':count})

# def analyse(request):
# 	return render(request,'personal/analyse.html')

# def complaint_detail(request):
# 	with connection.cursor() as cursor:
# 		cursor.execute("SELECT timestamp, class,division_id,zone_id, phone_no, email,status, data from feedback where user_id=1")
# 		data = list(cursor.fetchone())
# 		cursor.execute("SELECT div_name from divisions where division_id={}".format(data[2]))
# 		data[2] = list(cursor.fetchone())
# 		data[2] = data[2][0]
# 		cursor.execute("SELECT zone_name from zones where zone_id={}".format(data[3]))
# 		data[3] = list(cursor.fetchone())
# 		data[3] = data[3][0]
# 	return render(request,'personal/complaint_detail.html', {'data':data})
# @csrf_protect
# def login1(request):
# 	data=request.POST
# 	email=data.get('email')
# 	password=data.get('password')
# 	print(email,password)
# 	if(email=="" or password==""):
# 		return render(request,'personal/home.html')
# 	with connection.cursor() as cursor:
# 		cursor.execute("SELECT * FROM gms WHERE email='{0}' and password='{1}'".format(email, password))
# 		abc = cursor.fetchone()
# 	request.session['id'] = abc[0]
# 	request.session['name'] = abc[2]
# 	return render(request,'personal/admin_home.html')
 	


# @csrf_protect
# def complain(request):
# 	# input_file = open("handle.txt", "r") 
# 	# input_data = input_file.read()
# 	request_response = request.POST
# 	input_data = request_response["complaint"]
# 	name = request_response["firstname"]
# 	# print(name)
# 	contact = request_response["contact"]
# 	# print(contact)
# 	email = request_response["email"]
# 	# print(email)
# 	flag = 0
# 	words = input_data.split()
# 	length = len(words)
# 	for x in range(0,length):
# 		# print(words[x])
# 		if re.match('[0-9]{10}',words[x]):
# 			# print(words[x])
# 			api_response = request.get('https://api.railwayapi.com/v2/pnr-status/pnr/'+words[x]+'/apikey/rggo4dtabx/')
# 			time.sleep(1)
# 			api_response_json = api_response.json()
# 			response_code = api_response_json["response_code"]
# 			if response_code==200:
# 				print(words[x])
# 				station_code = api_response_json["from_station"]["code"]
# 				with connection.cursor() as cursor:
# 					cursor.execute("SELECT * FROM stations where station_code like '%{}%'".format(station_code))
# 					query_output = cursor.fetchone()
# 					if query_output != None:
# 						station_id = query_output[0]
# 						station_name = query_output[1]
# 						station_code = query_output[2]
# 						division_name = query_output[3]
# 						division_code = query_output[4]
# 						zone_name = query_output[5]
# 						zone_code = query_output[6]
# 						# cursor.execute("SELECT zone_id FROM zones where zone_name ='{}'".format(zone_name))
# 						# subquery_output = cursor.fetchone()[0]
# 						# zone_id= subquery_output
# 						cursor.execute("SELECT division_id FROM divisions where div_name ='{}'".format(division_name))
# 						subquery_output = cursor.fetchone()
# 						division_id = subquery_output[0]
# 						# print(zone_id)
# 						cursor.execute("INSERT INTO feedback(station_id,division_id,username,email,phone_no,data) VALUES ('{0}','{1}','{2}','{3}','{4}','{5}')".format(station_id,division_id,name,email,contact,input_data))
# 				flag = 1
# 	for x in range(0,length):
# 		if flag == 1:
# 			break
# 		elif re.match('[0-9]{5}$',words[x]):
# 			# https://api.railwayapi.com/v2/route/train/'+words[x]+'/apikey/rggo4dtabx/
# 			api_response = request.get('https://api.railwayapi.com/v2/route/train/'+words[x]+'/apikey/rggo4dtabx/')
# 			time.sleep(1)
# 			api_response_json = api_response.json()
# 			response_code = api_response_json["response_code"]
# 			if response_code==200:
# 				print(words[x])
# 				station_code = api_response_json["route"][0]["station"]["code"]
# 				# print(station_code)
# 				with connection.cursor() as cursor:
# 					cursor.execute("SELECT * FROM stations where station_code like '%{}%'".format(station_code))
# 					query_output = cursor.fetchone()
# 					if query_output != None:
# 						station_id = query_output[0]
# 						station_name = query_output[1]
# 						station_code = query_output[2]
# 						division_name = query_output[3]
# 						division_code = query_output[4]
# 						zone_name = query_output[5]
# 						zone_code = query_output[6]
# 						# cursor.execute("SELECT zone_id FROM zones where zone_name ='{}'".format(zone_name))
# 						# subquery_output = cursor.fetchone()[0]
# 						# zone_id= subquery_output
# 						cursor.execute("SELECT division_id FROM divisions where div_name ='{}'".format(division_name))
# 						subquery_output = cursor.fetchone()
# 						division_id = subquery_output[0]
# 						# print(zone_id)
# 						cursor.execute("INSERT INTO feedback(station_id,division_id,username,email,phone_no,data) VALUES ('{0}','{1}','{2}','{3}','{4}','{5}')".format(station_id,division_id,name,email,contact,input_data))
# 				flag = 1
# 				break
# 	for x in range(0,length):
# 		if flag == 1:
# 			break
# 		elif len(words[x]) > 4:
# 			with connection.cursor() as cursor:
# 				cursor.execute("SELECT * FROM stations where station_name like '%{}%'".format(words[x]))
# 				query_output = cursor.fetchone()
# 				if query_output != None:
# 					station_id = query_output[0]
# 					station_name = query_output[1]
# 					station_code = query_output[2]
# 					division_name = query_output[3]
# 					division_code = query_output[4]
# 					zone_name = query_output[5]
# 					zone_code = query_output[6]
# 					# cursor.execute("SELECT zone_id FROM zones where zone_name ='{}'".format(zone_name))
# 					# subquery_output = cursor.fetchone()[0]
# 					# zone_id= subquery_output
# 					cursor.execute("SELECT division_id FROM divisions where div_name ='{}'".format(division_name))
# 					subquery_output = cursor.fetchone()
# 					division_id = subquery_output[0]
# 					# print(zone_id)
# 					cursor.execute("INSERT INTO feedback(station_id,division_id,username,email,phone_no,data) VALUES ('{0}','{1}','{2}','{3}','{4}','{5}')".format(station_id,division_id,name,email,contact,input_data))
# 	for x in range(0,length):
# 		if flag == 1:
# 			break
# 		elif len(words[x]) <= 4 and len(words[x]) >= 2 and not(words[x] =="is" or words[x] =="at" or words[x] =="was" or words[x] =="were" or words[x] =="in" or words[x] =="to" or words[x] =="and" or words[x] =="from" or words[x] =="my" or words[x] =="can"):
# 			with connection.cursor() as cursor:
# 				cursor.execute("SELECT * FROM stations where station_code = '{}'".format(words[x]))
# 				query_output = cursor.fetchone()
# 				if query_output != None:
# 					station_id = query_output[0]
# 					station_name = query_output[1]
# 					station_code = query_output[2]
# 					division_name = query_output[3]
# 					division_code = query_output[4]
# 					zone_name = query_output[5]
# 					zone_code = query_output[6]
# 					# cursor.execute("SELECT zone_id FROM zones where zone_name ='{}'".format(zone_name))
# 					# subquery_output = cursor.fetchone()[0]
# 					# zone_id= subquery_output
# 					cursor.execute("SELECT division_id FROM divisions where div_name ='{}'".format(division_name))
# 					subquery_output = cursor.fetchone()
# 					division_id = subquery_output[0]
# 					# print(zone_id)
# 					cursor.execute("INSERT INTO feedback(station_id,division_id,username,email,phone_no,data) VALUES ('{0}','{1}','{2}','{3}','{4}','{5}')".format(station_id,division_id,name,email,contact,input_data))
# 	return render(request,'personal/home.html')


# def test(request):
# 	query = "Congrats"
# 	data = []
# 	with open('/home/ritesh/Mains/Projects/SIH 2018/mulc_2-20200511T024735Z-001/railways_twitter/personal/mulc_2/data/small_samples.json') as jf:
# 		data = json.load(jf)
# 		jf.close()
# 	data.append({
# 		'comments':query,
# 		'category':'train delay'
# 		})
# 	with open('/home/ritesh/Mains/Projects/SIH 2018/mulc_2-20200511T024735Z-001/railways_twitter/personal/mulc_2/data/small_samples.json', 'w') as jf:
# 		json.dump(data, jf)
# 		jf.close()
# 	cmd = ['python', './mulc_2/predict.py']
# 	# subprocess.Popen(['activate', 'tensorflow'])
# 	# subprocess.Popen(cmd).wait()
# 	subprocess.check_call(["python", "/home/ritesh/Mains/Projects/SIH 2018/mulc_2-20200511T024735Z-001/railways_twitter/personal/mulc_2/predict.py"])
# 	# p = subprocess.Popen([sys.executable, 'D:\mulc_2\predict.py'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
# 	# filename = 'D:\mulc_2\predict.py'
# 	# p = subprocess.check_call([filename, 'D:\mulc_2\parameters.json'])
# 	# a = os.system("D:\mulc_2\predict.py D:\mulc_2\parameters.json")
# 	# print(a)
# 	# time.sleep(40)
# 	a="a"
# 	with open('/home/ritesh/Mains/Projects/SIH 2018/mulc_2-20200511T024735Z-001/railways_twitter/personal/mulc_2/data/small_samples_prediction.json') as jf:
# 		data = json.load(jf)
# 		jf.close()
# 	predict = data[data.__len__() - 1]['new_prediction']
# 	with open('basics.txt', 'w') as f:
# 		f.write(str(predict))
# 		f.close()
# 	return render(request,'personal/home.html')