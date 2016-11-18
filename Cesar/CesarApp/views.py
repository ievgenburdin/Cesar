from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

def valid(getKey):
    if getKey =="":
        key = 0
        return(key)
    getKey = int(getKey)
    if getKey > 26:
        key = getKey % 26
    elif getKey < (-26):
        key = getKey % -26
    else:
        key = getKey
    return(key)


def encryption(decrypted, key):
    temp_crypted = []
    for i in range(len(decrypted)):
        asciiCode = (ord(decrypted[i]))
        if decrypted[i].isalpha():
            if asciiCode + key > 122 and 97 <= asciiCode <= 122:
                overflow = 96 + ((asciiCode + key) - 122)
                symbol = chr(overflow)
            elif asciiCode + key < 97 and 97 <= asciiCode <= 122:
                overflow = 123 - (97 - (asciiCode + key))
                symbol = chr(overflow)
            elif asciiCode + key > 90 and 65 <= asciiCode <= 90:
                overflow = 64 + ((asciiCode + key) - 90)
                symbol = chr(overflow)
            elif asciiCode + key < 65 and 65 <= asciiCode <= 90:
                overflow = 91 - (65 - (asciiCode + key))
                symbol = chr(overflow)
            else:
                symbol = chr(asciiCode + key)
        else:
            symbol = decrypted[i]
        temp_crypted.append(symbol)
    crypted = ''.join(temp_crypted)
    return(crypted)


def cesar_page(request):
    return render_to_response('index.html')


@csrf_exempt
def encrypt(request):
    if request.method == "POST":
        get_data = json.loads(request.body.decode('utf-8'))
        data = {}
        data['result'] = encryption(get_data['word'], valid(get_data['key']))
    return HttpResponse(json.dumps(data), content_type="application/json")


@csrf_exempt
def decrypt(request):
    if request.method == "POST":
        get_data = json.loads(request.body.decode('utf-8'))
        data = {}
        data['result'] = encryption(get_data['word'], -valid(get_data['key']))
    return HttpResponse(json.dumps(data), content_type="application/json")


@csrf_exempt
def info(request):
    if request.method == "POST":
        get_data = json.loads(request.body.decode('utf-8'))
        symbolList = get_data['word']
        length = len(symbolList)
        numberList = []
        for i in range(length):
            i_number = 0
            for n in range(length):
                if symbolList[n] == symbolList[i]:
                    i_number += 1
            numberList.append(i_number)
        data = {}
        data['number'] = numberList
        data['word'] = symbolList
    return HttpResponse(json.dumps(data), content_type="application/json")

