from django.shortcuts import render, render_to_response
from django.http import HttpResponse
import datetime
from django.template.loader import get_template
from django.views.decorators.csrf import csrf_exempt
from django.conf.urls.static import static
import json

def cesar_page(request):
    return render_to_response('index.html')
	
@csrf_exempt
def crypting(request):
	if request.method == "POST":
		get_data = json.loads(request.body.decode('utf-8'))
		
		decrypted = get_data['word']
		key = int(get_data['key'])

		if get_data['type'] == "decrypting":
			to_neg = -1
			key = key * to_neg

		length = len(decrypted)
		temp_crypted = []
		number = []
		for i in range(length):

			temp_num = 0
			for n in range(length):
				if decrypted[i] == decrypted[n]:
					temp_num += 1

			x = (ord(decrypted[i]))
			if 97 <= x <= 122 or 65 <= x <= 90:
				if x + key > 122 and 97 <= x <= 122 : 
					overflow = 96 + ((x + key) - 122)
					s = chr(overflow)           
				elif x + key < 97 and 97 <= x <= 122 : 
					overflow = 123 - (97 - (x + key))
					s = chr(overflow)
				elif x + key > 90 and 65 <= x <= 90 : 
					overflow = 64 + ((x + key) - 90)
					s = chr(overflow)
				elif x + key < 65 and 65 <= x <= 90 : 
					overflow = 91 - (65 - (x + key))
					s = chr(overflow)
				else:
					s = chr(x + key)
			else:
				s = decrypted[i]

			number.append(temp_num)			
			temp_crypted.append(s)
			
		crypted = ''.join(temp_crypted)
		
		data = {}
		data['result'] = crypted
		data['number'] = number
		data['temp_cr'] = temp_crypted
		

	return HttpResponse(json.dumps(data), content_type = "application/json")

@csrf_exempt
def info(request):
	if request.method == "POST":
		get_data = json.loads(request.body.decode('utf-8'))
		print(get_data);
		decrypted = get_data['word']
		length = len(decrypted)
		number = []

		for i in range(length):
			temp_num = 0
			for n in range(length):
				if decrypted[n] == decrypted[i]:
					temp_num += 1
					
			number.append(temp_num)
		data = {}
		
		data['number'] = number
		data['word'] = decrypted

	return HttpResponse(json.dumps(data), content_type = "application/json")
