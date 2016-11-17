from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json


def cesar_page(request):
    return render_to_response('index.html')


@csrf_exempt
def crypting(request):
    if request.method == "POST":
        get_data = json.loads(request.body.decode('utf-8'))

        decrypted = get_data['word']
        if get_data['key'] =="":
            key = 0
        else:
            key = int(get_data['key'])

        if key > 25:
            key = key % 26
        elif key < (-25):
            key = key % 26

        temp_crypted = []
        for i in range(len(decrypted)):
            x = (ord(decrypted[i]))
            if decrypted[i].isalpha():
                if x + key > 122 and 97 <= x <= 122:
                    overflow = 96 + ((x + key) - 122)
                    s = chr(overflow)
                elif x + key < 97 and 97 <= x <= 122:
                    overflow = 123 - (97 - (x + key))
                    s = chr(overflow)
                elif x + key > 90 and 65 <= x <= 90:
                    overflow = 64 + ((x + key) - 90)
                    s = chr(overflow)
                elif x + key < 65 and 65 <= x <= 90:
                    overflow = 91 - (65 - (x + key))
                    s = chr(overflow)
                else:
                    s = chr(x + key)
            else:
                s = decrypted[i]

            temp_crypted.append(s)
        crypted = ''.join(temp_crypted)

        data = {}
        data['result'] = crypted

    return HttpResponse(json.dumps(data), content_type="application/json")


@csrf_exempt
def decrypting(request):
    if request.method == "POST":
        get_data = json.loads(request.body.decode('utf-8'))

        decrypted = get_data['word']
        key = int(get_data['key'])

        if key > 25:
            key = (key % 26)* -1
        elif key < (-25):
            key = (key % 26)* -1

        length = len(decrypted)
        temp_crypted = []

        for i in range(length):
            x = (ord(decrypted[i]))
            if decrypted[i].isalpha():
                if x + key > 122 and 97 <= x <= 122:
                    overflow = 96 + ((x + key) - 122)
                    s = chr(overflow)
                elif x + key < 97 and 97 <= x <= 122:
                    overflow = 123 - (97 - (x + key))
                    s = chr(overflow)
                elif x + key > 90 and 65 <= x <= 90:
                    overflow = 64 + ((x + key) - 90)
                    s = chr(overflow)
                elif x + key < 65 and 65 <= x <= 90:
                    overflow = 91 - (65 - (x + key))
                    s = chr(overflow)
                else:
                    s = chr(x + key)
            else:
                s = decrypted[i]

            temp_crypted.append(s)
        crypted = ''.join(temp_crypted)

        data = {}
        data['result'] = crypted

    return HttpResponse(json.dumps(data), content_type="application/json")


@csrf_exempt
def info(request):
    if request.method == "POST":
        get_data = json.loads(request.body.decode('utf-8'))
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

    return HttpResponse(json.dumps(data), content_type="application/json")
